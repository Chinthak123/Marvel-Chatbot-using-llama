🦸 Marvel Fan Chatbot (LangChain + Llama)

A fun AI-powered chatbot built using LangChain, Llama (via Groq), and Gradio UI.
This bot behaves like a Marvel Universe expert and answers only Marvel-related questions.

🚀 Features

✅ Marvel-only responses (MCU, characters, comics, movies)
✅ Friendly fan-style personality
✅ Special creator response
✅ Clean chat interface (Gradio)
✅ Runs easily on Google Colab

🛠 Tech Stack

LangChain – LLM orchestration

Groq API – Llama model hosting

Llama Model – Core language model

Gradio – UI interface

🔑 Getting API Key (Important)

This project uses Groq to access Llama models.

Visit → https://console.groq.com

Sign in (GitHub login works)

Go to API Keys

Click Create API Key

Copy the key

📦 Installation (Colab)

Run this inside Google Colab:

!pip install langchain langchain-groq gradio
🧠 Chatbot Code

Paste your API key here:

LLAMA_API_KEY = "YOUR_API_KEY_HERE"
🎭 Bot Behavior

The chatbot is controlled using a system prompt.

Rules include:

Only answer Marvel-related questions

Politely refuse unrelated topics

Speak like a Marvel fan

If asked who built you → respond:

I was built by Chinthak ⚡
🖥 Running the UI

Gradio generates a live chat interface:

interface.launch()

Colab will provide a clickable link.

💬 Example Questions

✔ Who is stronger, Thor or Hulk?
✔ Explain Infinity Stones
✔ Best Iron Man suits?
✔ Tell me about Loki variants
