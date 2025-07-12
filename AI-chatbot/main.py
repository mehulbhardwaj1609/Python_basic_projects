import os
from openai import OpenAI

key = "" #openai api key

client = OpenAI(api_key=key)
messages = []

def completion(message):
    global messages
    messages.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        messages = messages,
        model = "gpt-3.5-turbo")
    
    message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }

    messages.append(message)
    print(f"Jarvis : {message['content']}")


if __name__ == "__main__":
    print(f"Jarvis : Hi I am Jarvis, your AI assistant. How can I help you today?")
    while True:
        user_quetsions = input()
        print(f"You : {user_quetsions}")
        completion(user_quetsions)