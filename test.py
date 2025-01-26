import openai

def chatbot():
    # Replace 'your-api-key-here' with your OpenAI API key
    openai.api_key = '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'

    print("Welcome to ChatGPT! Type 'exit' to end the chat.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        try:
            # Send user input to OpenAI's GPT-4
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_input}
                ]
            )

            # Get the chatbot's reply
            chatbot_reply = response['choices'][0]['message']['content']

            print(f"Chatbot: {chatbot_reply}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chatbot()
