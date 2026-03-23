import os
from huggingface_hub import InferenceClient

# It is generally best practice to use environment variables for API tokens.
api_key= os.environ.get("HUGGINGFACE_API_KEY")
client = InferenceClient(token=api_key)

def query_api(prompt):
    try:
       
        messages = [{"role": "user", "content": prompt}]
        
        response = client.chat_completion(
            messages=messages,
            model="Qwen/Qwen2.5-72B-Instruct", # Switched to a well-supported default model
            max_tokens=100
        )

        if not response or not response.choices:
            return "Error: No response from model"
            
        return response.choices[0].message.content

    except Exception as e:
        import traceback
        traceback.print_exc() # Print full stack trace to the console for easier debugging
        return f"Error: {repr(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)