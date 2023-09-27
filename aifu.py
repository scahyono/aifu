import openai
import logging
from dotenv import load_dotenv
import shutil
import os

# Load environment variables from .env file
load_dotenv()

# Configuration Management: Load API key from environment variables
api_key = os.environ.get('OPENAI_API_KEY')
MODEL="gpt-4"
TOKEN_TARGET = 8000 # increase if the bot is forgetful

# Check if the aifus folder is empty
if not os.listdir('aifus'):
    # If empty, copy each subdirectory from aifus_examples to aifus
    for item in os.listdir('aifus_examples'):
        s = os.path.join('aifus_examples', item)
        d = os.path.join('aifus', item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)

# List the content of the aifus folder
aifus = next(os.walk('aifus'))[1]

# If only one AIfu, choose it automatically, else ask the user to choose an AIfu
if len(aifus) == 1:
    aifu_location = aifus[0]
else:
    print("Choose an AIfu to chat with:")
    for index, aifu in enumerate(aifus):
        print(f"{index + 1}. {aifu.replace('_', ' ').title()}")

    choice = int(input("Enter the number of your choice: "))
    aifu_location = aifus[choice - 1]

# Set the aifu as the camel case of the aifu_location
aifu = aifu_location.replace("_", " ").title()

# Set up logging with timestamp
logging.basicConfig(filename=f'aifus/{aifu_location}/aifu_chat.log', level=logging.INFO, format='%(asctime)s %(message)s')

# File to store the conversation history
history_filename = f'aifus/{aifu_location}/conversation_history.txt'

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
        # Load the aifu persona from file
        with open(f'aifus/{aifu_location}/persona.txt', 'r', encoding='utf-8') as file:
            aifu_persona = file.read()
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": aifu_persona + " Replace 'As an AI,' with 'As an AIfu'"},
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

    # Send a greeting message automatically
    greeting_response = aifu_response("If you know my name, welcome me back, continue the last conversation, then stop (If you don't know my name then greet me and ask)")
    print(f"\033[94m{aifu}: \033[0m{greeting_response}")

    while True:
        user_input = input("\033[92mYou: \033[0m")  # \033[92m is the ANSI escape code for green text, \033[0m resets the text color
        if user_input.lower() in ('bye', 'exit', 'quit'):
            print(f"\033[94m{aifu}: \033[0mGoodbye! Have a nice day!")  # \033[94m is the ANSI escape code for blue text
            break
        response = aifu_response(user_input)
        print(f"\033[94m{aifu}: \033[0m{response}")

chat()
