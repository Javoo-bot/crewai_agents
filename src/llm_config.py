import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Instancia única y global del LLM
my_llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="groq/gemma2-9b-it",
    temperature=0.2,
    max_tokens=500
)
