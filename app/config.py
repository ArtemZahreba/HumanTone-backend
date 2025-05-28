import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HUGGINGFACE_API_TOKEN = os.getenv('HF_API_TOKEN')

