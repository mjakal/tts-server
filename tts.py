import pyttsx
from time import sleep

# Default speech rate - you can edit this value
DEFAULT_RATE = 180
STATUS = { "busy": False }


# Get pyttsx engine instance
def get_engine():
    engine = pyttsx.init()
        
    return engine


# Set busy flag to True on utterance start
def on_tts_start(name):
    STATUS["busy"] = True


# Set busy flag to False on utterance end
def on_tts_end(name, completed):
   sleep(0.5) # We have to give pyttsx some space to successfully reinitialize
   STATUS["busy"] = False


# Get the list of installed voices
def get_tts_voices():
    engine = get_engine()
    voices = engine.getProperty('voices')
    voice_names = []
    
    for voice in voices:
        voice_names.append(voice.name)
    
    return voice_names


# Read text
def speak_text(voice = "", text = "", rate = DEFAULT_RATE):
    engine = get_engine()
    voices = engine.getProperty('voices')
    rate = int(rate)
    
    status = STATUS["busy"]

    # Check if tts engine is busy
    if status:
        return

    # Set voice
    if voice:
        for item in voices:
            if item.name == voice:
                voice_id = item.id
                engine.setProperty('voice', voice_id)
                break

    # Set speech rate
    if rate:
        engine.setProperty('rate', rate)

    engine.connect('started-utterance', on_tts_start)
    engine.connect('finished-utterance', on_tts_end)

    engine.say(text)
    engine.runAndWait()


# Stop reading
def stop_speaking():
    engine = get_engine()

    engine.stop()