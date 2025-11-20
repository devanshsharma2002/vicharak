from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('GEMINI_API_KEY')

def geminiResp(prompty):

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompty
    )
    return response.text

