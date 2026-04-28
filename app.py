import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from src.agent import get_siggy_response
from src.knowledge import get_ritual_knowledge_tool

app = Flask(__name__)

# Eagerly initialize the HuggingFace model during server boot.
# This prevents the first user request from timing out (100s limit on Railway) 
# while the 130MB model downloads.
print("Pre-loading HuggingFace Embedding Model...")
get_ritual_knowledge_tool()
print("Model loaded successfully!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
        
    try:
        response = get_siggy_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
