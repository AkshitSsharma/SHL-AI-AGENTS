import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_reply(query, results):

    prompt = f"""
    User hiring request:
    {query}

    Recommended SHL assessments:
    {results}

    Explain naturally why these SHL assessments fit.
    Use ONLY the provided assessment data.
    Keep the response concise and recruiter-friendly.
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content