   
import subprocess
import requests
import time
from ollama import Client
import ollama


OLLAMA_HOST = 'http://localhost:11434'
MODEL_NAME = 'deepseek-r1:7b'  # or whatever you've pulled like 'olama:5.3'

# --- STEP 1: Check if Ollama is running ---
def is_ollama_running():
    try:
        r = requests.get(f'{OLLAMA_HOST}')
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# --- STEP 2: Start Ollama if not running ---
def start_ollama_server():
    print("⚙️ Starting Ollama server...")
    # Option 1: start `ollama serve` in background
    #subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Option 2: to start specific model immediately:
    subprocess.Popen(["ollama", "run", MODEL_NAME], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for it to start listening
    while True:
        if is_ollama_running():
            print("✅ Ollama is now running!")
            return
        time.sleep(1)
    raise RuntimeError("❌ Ollama failed to start in time.")

# --- STEP 3: Ask with personal context ---
def load_personal_info():
    with open("personal_data.txt", "r", encoding="utf-8") as f:
        return f.read()

def ask_about_me(client, personal_info, question):
    prompt = f"""
You are a helpful assistant that knows everything about the person described below.

== PERSONAL INFORMATION ==
{personal_info}
== QUESTION ==
{question}

Please answer as if you personally know them well.
"""

    response = client.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    print("🤖:", response['message']['content'])



def ensure_model_exists(model_name):
    try:
        ollama.show(model_name)
    except ollama.ResponseError:
        print(f"📥 Model '{model_name}' not found. Downloading now...")
        ollama.pull(model_name)
        print("✅ Download complete!")    
        
        
        
# --- STEP 4: Main interactive loop ---
def main():
    # Start ollama if needed
    if not is_ollama_running():
        start_ollama_server()

    client = Client(host=OLLAMA_HOST)
    personal_info = load_personal_info()
    ensure_model_exists(MODEL_NAME)
    print("🧠 Ask me anything about YOU. Type 'exit' to quit.")
    while True:
        user_input = input("🧑 You: ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("👋 Bye!")
            break
        ask_about_me(client, personal_info, user_input)
if __name__ == "__main__":
    main()    