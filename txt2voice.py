from gtts import gTTS
import os

class TextToSpeech:
    
    def save_to_mp3(self,word):
        if os.path.exists(f'cache/{word}.mp3'):
            return f'cache/{word}.mp3'
        else:
            tts = gTTS(text=word, lang='en-uk')
            tts.save(f'cache/{word}.mp3')
            return f'cache/{word}.mp3'