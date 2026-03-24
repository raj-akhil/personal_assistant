
## 🗂️ Folder Structure

personal_assistant/
├── main.py # Main Python script
├── personal_data.txt # Your private profile (ignored by Git)
├── .gitignore # Ensures sensitive files aren't pushed
├── requirements.txt # Python dependencies
└── README.md # This file

## 📄 personal_data.txt Format

You must manually create a file called `personal_data.txt` in the project root.

### ✍️ Example Format:

Name: Amal
Age: 28
Occupation: Senior Data Engineer at NHS
Hobbies: Science, logic, building personal AI tools, plasma experiments
Personality: Curious, skeptical, clever, honest, Gen Z vibe
Goals: Become a thought leader in data science and AI



Feel free to expand this file with any information you'd want your assistant to "know".

---

## 🧪 How It Works

When you run `main.py`:

1. It checks if Ollama is running.
2. If not, it starts the LLM model (like `llama3`) automatically.
3. Loads your `personal_data.txt` into memory.
4. Opens a command-line chat loop where you can ask questions like:
   - "What's my job?"
   - "What do I like?"
   - "What's a good birthday gift for me?"

---

## 🛠️ Installation

### 1. Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and set up
- A model pulled (e.g. `ollama pull llama3`)
- Git (optional)

### 2. Install Dependencies

```bash
pip install -r requirements.txt