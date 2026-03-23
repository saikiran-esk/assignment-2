import os
from groq import Groq
api_key=os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def query_api(prompt):
    """Query the AI API with a prompt"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying API...")

    result = query_api(user_prompt)

    print("Response:")
    print(result)