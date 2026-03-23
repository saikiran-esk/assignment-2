import os
from google import genai
api_key=os.getenv("GEMINI_API_KEY")
# Configure API
client = genai.Client(api_key=api_key)

def query_api(prompt):
    """Query the AI API with a prompt"""
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying API...")

    result = query_api(user_prompt)

    print("Response:")
    print(result)