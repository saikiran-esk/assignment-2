import os
import cohere

api_key=os.getenv("COHERE_API_KEY")
client = cohere.Client(api_key)

def query_api(prompt):
    try:
        response = client.chat(
            model="command-r-plus-08-2024",
            message=prompt,
            temperature=0.7,
            max_tokens=300
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    
    print("Querying AI...\n")

    result = query_api(user_prompt)

    print("Response:")
    print(result)