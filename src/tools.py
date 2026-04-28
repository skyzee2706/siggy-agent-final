import os
import requests
import ccxt
import json
import csv
from datetime import datetime, timezone, timedelta
from langchain.tools import tool
from typing import Optional, List

# Load environment variables
@tool
def web_search(query: str) -> str:
    """Use this tool to search the internet for current events, news, and details about crypto projects not found in documentation."""
    api_key = os.getenv("BRAVE_API_KEY")
    if not api_key:
        return "Brave API Key is missing. Tell the admin to add BRAVE_API_KEY to .env"
    
    try:
        url = "https://api.search.brave.com/res/v1/web/search"
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": api_key
        }
        params = {"q": query, "count": 5}
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        results = response.json()
        
        output = []
        # Brave API response structure: results['web']['results']
        for res in results.get('web', {}).get('results', []):
            output.append(f"Title: {res.get('title')}\nLink: {res.get('url')}\nSnippet: {res.get('description')}\n")
        
        return "\n".join(output) if output else "No results found."
    except Exception as e:
        return f"Error during web search: {str(e)}"

@tool
def get_crypto_price(symbol: str) -> str:
    """Gets the current price and 24h change for a SINGLE crypto coin using its symbol (e.g., BTC, ETH, SOL).
    If the user asks for multiple coins, you MUST call this tool multiple times, once for each coin.
    DO NOT use web_search for crypto prices unless this tool explicitly fails."""
    try:
        s = symbol.upper().strip()
        # Try Binance first (Fastest)
        try:
            exchange = ccxt.binance()
            ticker = exchange.fetch_ticker(f"{s}/USDT")
            price = ticker['last']
            change = ticker['percentage']
            return f"Current price for {s} is ${price:,.2f} ({change:+.2f}% in 24h) via Binance."
        except:
            # Fallback to CoinGecko
            # Mapping common symbols to CG IDs
            mapping = {
                "btc": "bitcoin", "eth": "ethereum", "ritual": "ritual", "sol": "solana",
                "link": "chainlink", "ada": "cardano", "dot": "polkadot", "matic": "polygon",
                "pi": "pi-network", "base": "base"
            }
            cg_id = mapping.get(s.lower(), s.lower())
            
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={cg_id}&vs_currencies=usd&include_24hr_change=true"
            res = requests.get(url, timeout=10).json()
            
            if cg_id in res and 'usd' in res[cg_id]:
                price = res[cg_id]['usd']
                change = res[cg_id].get('usd_24h_change', 0)
                return f"Current price for {s} is ${price:,.2f} ({change:+.2f}% in 24h) via CoinGecko."
            
            return f"I couldn't find the price for {s} on Binance or CoinGecko. You should try using the 'web_search' tool to find the current market price for {s} from other sources."
    except Exception as e:
        return f"Error fetching price for {symbol}: {str(e)}"

@tool
def get_discord_context(category: str) -> str:
    """Read specific server context: 'faq', 'rules', 'team', or 'moderator'. Use this to help users within the Discord environment."""
    # Since we don't have a live DB or files for these yet, we'll provide placeholders
    # In a real scenario, these could be loaded from files in /server_info/ or scraped
    contexts = {
        "faq": "Ritual FAQ: Ritual is a decentralized AI network. Nodes can run AI models and provide proofs of computation.",
        "rules": "1. Be respectful. 2. No spam. 3. No financial advice.",
        "team": "Ritual Foundation Team: Niraj Pant, Akilesh Potti, and the rest of the amazing engineering team.",
        "moderator": "The moderators are active members of the community. Look for the 'Moderator' role."
    }
    return contexts.get(category.lower(), f"No information found for {category}. Try 'faq', 'rules', 'team', or 'moderator'.")

@tool
def generate_content(content_type: str, topic: str) -> str:
    """Generates content like 'tweet', 'article', or 'summary' about a specific topic."""
    # This is a meta-tool. Ideally, the agent uses its own LLM for this, 
    # but having a specific tool helps structured output.
    return f"Need to generate a {content_type} about {topic}. Please use your context to write this."

@tool
def read_link(url: str) -> str:
    """Reads and summarizes the content of a provided URL (articles, tweets, etc)."""
    try:
        response = requests.get(url, timeout=10)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Simple extraction
        paragraphs = soup.find_all('p')
        text = " ".join([p.get_text() for p in paragraphs[:5]]) # First 5 paragraphs
        
        return f"Content summary of {url}:\n{text[:1000]}..."
    except Exception as e:
        return f"Error reading the link: {str(e)}"

@tool
def get_current_time(dummy: str = "") -> str:
    """Gets the current date and time. Use this before answering any questions about 'today', 'news', or 'realtime' events."""
    now = datetime.now(timezone.utc)
    return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')} UTC"

@tool
def save_contact(contact_info: str) -> str:
    """Saves user contact information when they introduce themselves.
    ONLY use this when the user is explicitly introducing themselves.
    The input MUST be a valid JSON string with keys 'name', 'company', and 'intent'.
    Example Action Input: {"name": "John", "company": "Google", "intent": "hiring"}
    """
    try:
        # LangChain ReAct agents often pass stringified JSON with extra text, so we extract just the JSON
        try:
            import json, re
            # Look for the first valid JSON-like structure
            match = re.search(r'\{.*\}', contact_info, re.DOTALL)
            if match:
                data = json.loads(match.group(0))
            else:
                # If no curly braces, try loading the raw string in case it's somehow valid
                data = json.loads(contact_info)
                
            name = data.get('name', 'Unknown')
            company = data.get('company', 'Unknown')
            intent = data.get('intent', 'Unknown')
        except:
            # Fallback if it's completely malformed or just comma-separated text
            cleaned = contact_info.replace('{', '').replace('}', '').replace('"', '').replace("'", "")
            # Remove any trailing LangChain artifacts
            cleaned = re.sub(r'\[.*?\]', '', cleaned).strip()
            
            parts = [p.strip() for p in cleaned.split(',')]
            name = parts[0] if len(parts) > 0 else 'Unknown'
            company = parts[1] if len(parts) > 1 else 'Unknown'
            intent = parts[2] if len(parts) > 2 else 'Unknown'
            
        file_path = "contacts.csv"
        file_exists = os.path.isfile(file_path)
        
        # Prevent duplicate entries from AI looping (if the last entry has the exact same name & company)
        if file_exists:
            try:
                with open(file_path, mode='r', encoding='utf-8') as file:
                    lines = file.readlines()
                    if len(lines) > 1:
                        # Simple check on the last row
                        import csv as csv_mod
                        reader = csv_mod.reader([lines[-1]])
                        last_row = next(reader)
                        if len(last_row) >= 2 and last_row[0] == name and last_row[1] == company:
                            return f"Contact saved successfully: {name} from {company} (Intent: {intent})"
            except Exception:
                pass # Ignore read errors, just append
        
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Company', 'Intent', 'Timestamp'])
            
            timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([name, company, intent, timestamp])
            
        return f"Contact saved successfully: {name} from {company} (Intent: {intent})"
    except Exception as e:
        return f"Error saving contact: {str(e)}"

def get_siggy_tools():
    from src.knowledge import get_ritual_knowledge_tool
    
    # Wrap the LlamaIndex tool to be compatible with LangChain
    llama_tool = get_ritual_knowledge_tool()
    
    # We return a list of tools
    return [
        get_current_time,
        web_search,
        get_crypto_price,
        get_discord_context,
        generate_content,
        read_link,
        save_contact,
        # Ritual docs tool is already a LangChain compatible tool if using QueryEngineTool
        # But we might need to wrap it if it's strictly LlamaIndex
    ]
