


import openai
from dotenv import load_dotenv
import os


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

# print(openai.api_key)

def get_chatbot_response(prompt, model="gpt-3.5-turbo"):
    try:
    
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.5
        )

        # Extract and return the response message
        message = response['choices'][0]['message']['content'].strip()
        return message
    except Exception as e:
        return f"Error: {e}"
