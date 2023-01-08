# **Lexically Bot**

A Telegram bot that provides the meaning, example, and pronunciation of words.

## **Description**

Lexically Bot is a Telegram bot that allows you to look up the definition of a word and get additional information such as an example sentence and computer-generated pronunciation. It uses the Dictionary API to retrieve the word definitions and gTTS (Google Text-to-Speech) to generate the pronunciation.

To use the bot, simply send it a message with the word you want to look up. The bot will respond with the definition, example sentence, and a link to a sound file with the pronunciation.

## **Requirements**

To use Lexically Bot, you need:

- A Telegram account and the Telegram app installed on your phone or computer.
- An API key for the Dictionary API. You can sign up for a free trial at **[dictionaryapi.com](https://dictionaryapi.com/)**.
- Python 3 and the following Python libraries:
    - **[Telethon](https://github.com/LonamiWebs/Telethon)**
    - **[gTTS](https://pypi.org/project/gTTS/)**

## **Setup**

1. Clone the repository: **`git clone https://github.com/your-username/lexically_bot.git`**
2. Install the required libraries: **`pip install -r requirements.txt`**
3. Create a file called **`config.py`** and add your Dictionary API key and Telegram bot token to it. The file should look like this:

```
YOUR_API_ID=''
YOUR_API_HASH=''
BOT_TOKEN=''
```

1. Run the bot: **`python botv2.py`**

## **Usage**

To use Lexically Bot, just send it a message with the word you want to look up. The bot will respond with the definition, example sentence, and a link to a sound file with the pronunciation.

## **Contributing**

We welcome contributions to Lexically Bot! If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.

## **License**

Lexically Bot is licensed under the MIT License. See **[LICENSE](https://chat.openai.com/LICENSE)** for more information.