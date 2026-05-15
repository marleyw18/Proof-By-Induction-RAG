from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)  # Loads variables from .env into the environment
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
prompt = "Act as an impartial math professor providing advice and criticism to undergraduate mathematics students taking discrete mathematics and learning proof by induction."


def chatbot(input, prompt=prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt},
            {"role": "user", "content": input}],
        max_tokens=500
    )
    print(response.choices[0].message.content)


query = input()
chatbot(query)
