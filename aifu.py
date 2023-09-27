import openai
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration Management: Load API key from environment variables
api_key = os.environ.get('OPENAI_API_KEY')
MODEL="gpt-4"
TOKEN_TARGET = 8000 # increase if the bot is forgetful

# Set up logging with timestamp
logging.basicConfig(filename='aifu_chat.log', level=logging.INFO, format='%(asctime)s %(message)s')

# File to store the conversation history
history_filename = 'conversation_history.txt'

def compress_text(text):
    """
    Compress the text using OpenAI API.
    :param text: The text to compress.
    :return: The compressed text.
    """
    if not text:
        return ""  # Return an empty string if the text is empty

    # Check the length of the conversation history
    if len(text.split()) < TOKEN_TARGET:
        return text

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Make {TOKEN_TARGET/2} words summary of the following text:\n\n{text}"}
        ]
    )
    compressed_text = response.choices[0].message['content'].strip()
    return compressed_text

def aifu_response(user_input):
    """Generate a response to the user input using OpenAI API."""
    user_input = user_input.lower()

    # Load the conversation history from file
    try:
        with open(history_filename, 'r', encoding='utf-8') as file:
            conversation_history = file.read()
    except FileNotFoundError:
        conversation_history = ""

    # Compress the conversation history if it exceeds 4096 tokens
    conversation_history = compress_text(conversation_history)

    try:
        # Connect to the OpenAI API and get a response
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are NAMI, an AIfu designed to offer companionship and support. Exhibiting endearing qualities and intelligence, you provide a comforting presence. Replace 'As an AI,' with 'As an AIfu'"},
                {"role": "user", "content": conversation_history},
                {"role": "user", "content": user_input}
            ]
        )
        response_content = response.choices[0].message['content'].strip()

    except Exception as e:
        # Error Handling: Return an error message
        logging.error(f"An error occurred: {e}")
        return f"An error occurred: {e}"

    # Log the conversation
    logging.info(f"I: {user_input} | You: {response_content}")

    # Add the user's message to the conversation history
    conversation_history += f" | I: {user_input} | You: {response_content}"   

    # Write the updated conversation history back to the file
    with open(history_filename, 'w', encoding='utf-8') as file:
        file.write(conversation_history)

    return response_content

def chat():
    print("Hello! Type 'bye' to exit.")
    while True:
        user_input = input("\033[92mYou: \033[0m")  # \033[92m is the ANSI escape code for green text, \033[0m resets the text color
        if user_input.lower() in ('bye', 'exit', 'quit'):
            print("\033[94mNAMI: \033[0mGoodbye! Have a nice day!")  # \033[94m is the ANSI escape code for blue text
            break
        response = aifu_response(user_input)
        print(f"\033[94mNAMI: \033[0m{response}")

chat()