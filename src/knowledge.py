import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.groq import Groq
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.postprocessor import SimilarityPostprocessor
from dotenv import load_dotenv

load_dotenv()

class RitualKnowledgeBase:
    def __init__(self, docs_path="ritual_docs", persist_dir="./storage"):
        self.docs_path = docs_path
        self.persist_dir = persist_dir
        self.llm = Groq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
        # FastEmbed uses ONNX runtime, taking ~80MB RAM instead of >500MB (PyTorch), preventing Railway OOM crashes.
        self.embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")
        
        self.index = self._get_index()
        # similarity_top_k=5 for more context
        self.query_engine = self.index.as_query_engine(
            llm=self.llm,
            similarity_top_k=5,
            response_mode="compact",
            node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)]
        )

    def _get_index(self):
        # We'll use a specific parser for better chunking
        parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
        
        if os.path.exists(self.persist_dir):
            print(f"Loading existing index from {self.persist_dir}...")
            storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
            return load_index_from_storage(storage_context, embed_model=self.embed_model)
        else:
            print(f"Creating new index from {self.docs_path}...")
            # Load docs with filename metadata
            reader = SimpleDirectoryReader(
                input_dir=self.docs_path,
                filename_as_id=True
            )
            documents = reader.load_data()
            
            # Build index with custom parser
            index = VectorStoreIndex.from_documents(
                documents, 
                embed_model=self.embed_model,
                transformations=[parser],
                show_progress=True
            )
            index.storage_context.persist(persist_dir=self.persist_dir)
            return index

    def get_tool(self):
        return QueryEngineTool(
            query_engine=self.query_engine,
            metadata=ToolMetadata(
                name="ritual_docs_search",
                description="CRITICAL: Use this tool for ANY question about Ritual, EVM++, Infernet, Sidecars, or Ritual nodes. This contains the ONLY accurate technical source. Do not rely on general knowledge."
            )
        )

# Singleton instance
knowledge_base = None

def get_ritual_knowledge_tool():
    global knowledge_base
    if knowledge_base is None:
        knowledge_base = RitualKnowledgeBase()
    return knowledge_base.get_tool()
