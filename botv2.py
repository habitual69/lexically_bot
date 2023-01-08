from config import BOT_TOKEN, YOUR_API_HASH, YOUR_API_ID
from telethon import TelegramClient, events
import asyncio
from word import WordDefiner
from txt2voice import TextToSpeech
import os

client = TelegramClient('lexically_bot', api_id=YOUR_API_ID, api_hash=YOUR_API_HASH).start(bot_token=BOT_TOKEN)
client.parse_mode='html'


@client.on(events.NewMessage)
async def handler(event):
    word = event.message.text
    definer = WordDefiner()
    definition, example = definer.get_definition(word)
    if definition==None and example==None:
        await event.respond(f"<i>The meaning of the word <b>{word}</b> not found</b>")
    else:
        await event.respond(f"<b>Meaning:<b/> <i>{definition}<i/>\n<b>Example:</b> <i>{example}</i>")
        sound=TextToSpeech()
        path=sound.save_to_mp3(word)
        if os.path.exists(f'cache/{word}.mp3'):
            await client.send_file(event.chat_id, path,caption='<b>Pronunciation</b>')
        else:
            await event.respond("Pronunciation audio not available")

client.start()
client.run_until_disconnected()
