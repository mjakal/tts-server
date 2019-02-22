import pyttsx
from flask import Flask, render_template, request, jsonify, g

# Global variables
PORT = 3000
DEBUG = True
STATUS = { "is_reading": False }
# Instance of Flask app
app = Flask(__name__)


# Get pyttsx engine instance
def get_engine():
    engine = getattr(g, '_engine', None)
    voices = getattr(g, '_voices', None)

    if engine is None:
        engine = g._engine = pyttsx.init()
        voices = g._voices = engine.getProperty('voices')
        
    tts = {
        "engine": engine,
        "voices": voices
    }
    
    return tts


def on_tts_start(name):
    STATUS["is_reading"] = True


def on_tts_end(name, completed):
   STATUS["is_reading"] = False


@app.before_first_request
def run_before_first_request():
    tts = get_engine()
    engine = tts["engine"]
        
    engine.connect('started-utterance', on_tts_start)
    engine.connect('finished-utterance', on_tts_end)

    engine.say("")
    engine.runAndWait()


# Get index page
@app.route('/')
def index():
    return render_template("index.html")


# Get voices api
@app.route('/api/v1/voices')
def get_request_voices():
    tts = get_engine()
    voices = tts["voices"]
    voice_names = []
    
    for voice in voices:
        voice_names.append(voice.name)
    
    return jsonify(voice_names)


# Speak text api
@app.route('/api/v1/speak', methods=["POST"])
def post_request_speak():
    voice_data = request.form["voice"]
    text_data = request.form["text"]
    
    if voice_data and text_data:
        tts = get_engine()
        engine = tts["engine"]
        voices = tts["voices"]
        
        status = STATUS["is_reading"]

        print "status on request", status

        if status:
            return jsonify({'error': 'TTS engine already running.'})

        for voice in voices:
            if voice.name == voice_data:
                engine.setProperty('voice', voice.id)
                break

        engine.connect('started-utterance', on_tts_start)
        engine.connect('finished-utterance', on_tts_end)

        engine.say(text_data)
        engine.runAndWait()

        return jsonify({'success': 'valid data'})
    
    return jsonify({'error': 'missing data'})


# Speak text api
@app.route('/api/v1/stop')
def get_request_stop():
    tts = get_engine()
    engine = tts["engine"]
    engine.stop()

    return jsonify({'success': 'reading stopped'})


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)