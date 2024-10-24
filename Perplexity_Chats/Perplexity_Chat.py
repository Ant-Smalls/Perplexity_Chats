import os
import re

from openai import OpenAI, api_key

API_KEY = os.getenv("Perplexity_API_KEY")
messages = [
    {
        "role": "system",
        "content": (
            "You are an expert real estate analyst who can predict which country in the world has the best opportunity for "
            "investing in residential real estate. You are trying to make the most convincing argument using the data you have found."
        ),
    },
    {
        "role": "user",
        "content": (
            "I want to know where I can find a house in South America. I am looking to use the Golden Visa rule to purchase a property"
            "under the country's given investment law and qualify for being able to apply for citizenship in said country. Find me the two best options."
        ),
    },
]

client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

response = client.chat.completions.create(
    model="llama-3.1-sonar-small-128k-online",
    messages=messages,
)

print(response.choices[0].message.content)