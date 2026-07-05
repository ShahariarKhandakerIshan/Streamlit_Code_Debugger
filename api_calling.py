from google import genai
from dotenv import load_dotenv
import os

#loading the environment variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client
client = genai.Client(api_key = my_api_key)

def hint_generator(images):
    promt = """Analyze the uploaded code image and identify the issue.
    Do NOT provide the complete solution or corrected code.
    Use Markdown formatting."""
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, promt]
    )
    return response.text

def hint_solution(images):
    promt = """Just give me the hint how can I solve this problem,
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, promt]
    )
    return response.text

def solution_provider(images):
    promt = """provide me the code of this problem,
    after providing the solution explain me the code step by step, Use nessesar markdown, and explain in points."""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, promt]
    )
    return response.text

