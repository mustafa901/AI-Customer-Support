import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    messages = []
    print("Welcome to the AI Chatbot! Type 'quit', 'exit', or 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})
        response = chat_with_gpt(messages)
        print("Chatbot: ", response)
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
