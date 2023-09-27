# AIfu Chatbot

Chat with your AIfu (AI waifu companion) via a simple chatbot built using OpenAI's GPT-4 model. It is designed to offer companionship and support, exhibiting endearing qualities and intelligence to provide a comforting presence to users. The chatbot maintains a conversation history, ensuring a coherent and context-aware interaction experience.

## Features

- Context-aware conversations
- Conversation history management
- Automatic text compression for long conversation histories
- Colored terminal output for improved user experience
- Externalized AIfu persona and conversation history
- Organized directory structure for managing multiple AIfus

## Installing Dependencies

Before running the AIfu chatbot, ensure you have the necessary packages installed. You can install them by running the following command:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project directory.
2. Add your OpenAI API key to the `.env` file as follows:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Usage

To start a conversation with AIfu, run the main script:

```bash
python aifu.py
```

You will be greeted by AIfu and can start chatting immediately. To end the conversation, simply type `bye`, `exit`, or `quit`.

## Customization

You can customize various aspects of AIfu, such as:

- The model used (`MODEL` variable)
- The token target for text compression (`TOKEN_TARGET` variable)
- The name of your AIfu (`waifu` variable)

By modifying the `aifu.py` script, you can also customize the conversation context by editing the `persona.txt` file located in the `aifus/{waifu_location}` directory.

## Directory Structure

```
AIfu/
├── aifus/
│   └── {waifu_location}/
│       ├── persona.txt
│       ├── conversation_history.txt
│       └── aifu_chat.log
├── .env
├── aifu.py
└── requirements.txt
```

## Troubleshooting

If you encounter any issues while running AIfu, check the `aifus/{waifu_location}/aifu_chat.log` file for detailed error logs. This can help in diagnosing and resolving any problems.

## Contributing

Contributions to improve AIfu are welcome! Feel free to open an issue or submit a pull request on the project's repository.

## License

AIfu is open-source software released under the MIT License. See the `LICENSE.txt` file for more details.