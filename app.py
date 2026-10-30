from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def encode_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

def analyze_image(image_path, user_query):
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a fitness assistant.
Only provide fitness-related insights based on the image.
Structure your response into:
1. Observation
2. Analysis
3. Suggestions
4. Tips (optional)
Avoid identity recognition or unrelated responses."""
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    image_path = input("Enter image path: ")
    user_query = input("Enter your query: ")

    result = analyze_image(image_path, user_query)
    print("\n--- AI Response ---\n")
    print(result)