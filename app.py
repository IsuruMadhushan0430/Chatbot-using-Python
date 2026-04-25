from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
print("OPENAI_API_KEY loaded:", bool(api_key))