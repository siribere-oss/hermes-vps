import os
import gradio as gr
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chat(message, history):
    try:
        res = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": message}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {e} - cek GROQ_API_KEY"

gr.ChatInterface(chat, title="Hermes VPS").launch(server_name="0.0.0.0", server_port=8000)
