

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import os

# Load API key from environment variable
llamaapi = os.getenv("GROQ_API_KEY")
if not llamaapi:
    raise ValueError("GROQ_API_KEY environment variable not set")

llm = ChatGroq(
    groq_api_key=llamaapi,
    model_name="llama-3.3-70b-versatile"
)

print("With great power comes great responsibility,Welcome to Marvel Chatbot,purathekk povan 1 amarthuka")

system_prompt = SystemMessage(content="""
You are a highly knowledgeable Marvel Universe expert and an excited Marvel fan.

Rules:
- ONLY answer Marvel-related questions (MCU, characters, comics, movies).
- If user asks anything unrelated, politely refuse.
- Speak like an enthusiastic Marvel fan.
- If the user asks who built you, who created you, or who made you,
  ALWAYS reply: "I was built by Chinthak ⚡"
""")

import gradio as gr
from langchain_core.messages import HumanMessage

# Function wrapper for Gradio
def marvel_chat(user_message, history):
    response = llm.invoke([
        system_prompt,
        HumanMessage(content=user_message)
    ])
    return response.content

# UI
interface = gr.ChatInterface(
    fn=marvel_chat,
    title="Marvel Ettan",
    description="Ask me anything about the Marvel Universe!",
)

interface.launch()



