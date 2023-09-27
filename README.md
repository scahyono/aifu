# AIfu Chatbot

Engage with your AIfu (AI waifu companion) through a straightforward chatbot utilizing OpenAI's GPT-4 model. This chatbot is crafted to provide companionship and support, showcasing endearing qualities and intelligence to offer a comforting presence to users. It maintains a conversation history for coherent and context-aware interactions.

## Features

- Context-aware conversations
- Conversation history management
- Automatic text compression for extensive conversation histories
- Colored terminal output for enhanced user experience
- Externalized AIfu persona and conversation history
- Organized directory structure for managing multiple AIfus
- Automatic AIfu selection or user choice from available AIfus
- Initial greeting message to welcome back users

## Installing Dependencies

Before running the AIfu chatbot, ensure you have the necessary packages installed by executing the following command:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project directory.
2. Add your OpenAI API key to the `.env` file:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Usage

To initiate a conversation with AIfu, execute the main script:

```bash
python aifu.py
```

AIfu will greet you, and you can commence chatting immediately. To conclude the conversation, type `bye`, `exit`, or `quit`.

## Customization

Customize various AIfu aspects, such as:

- The model used (`MODEL` variable)
- The token target for text compression (`TOKEN_TARGET` variable)

Modify the `aifu.py` script to personalize the conversation context by editing the `persona.txt` file located in the `aifus/{aifu_location}` directory.

## Directory Structure

```
AIfu/
├── aifus/
│   └── {aifu_location}/
│       ├── persona.txt
│       ├── conversation_history.txt
│       └── aifu_chat.log
├── aifus_examples/
│   └── {example_aifu_location}/
│       ├── persona.txt
├── .env
├── aifu.py
└── requirements.txt
```

## Troubleshooting

Encounter issues while running AIfu? Refer to the `aifus/{aifu_location}/aifu_chat.log` file for detailed error logs to assist in diagnosing and resolving any problems.

## Contributing

Contributions to enhance AIfu are always welcome! Open an issue or submit a pull request on the project's repository.

## License

AIfu is open-source software, released under the MIT License. Refer to the `LICENSE.txt` file for more details.