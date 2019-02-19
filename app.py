import pyttsx
from flask import Flask, render_template, request, jsonify, g

app = Flask(__name__)


# Get pyttsx engine instance
def get_engine():
    engine = getattr(g, '_engine', None)
    if engine is None:
        engine = g._engine = pyttsx.init()
    
    return engine


# Get index page
@app.route('/')
def index():
    return render_template("index.html")


# Get voices api
@app.route('/api/v1/voices')
def get_tts_voices():
    engine = get_engine()
    voices = engine.getProperty('voices')
    voice_names = []
    
    engine.say("")
    engine.runAndWait()

    for voice in voices:
        voice_names.append(voice.name)
    
    return jsonify(voice_names)


# Speak text api
@app.route('/api/v1/speak', methods=["POST"])
def speak():
    voice_data = request.form["voice"]
    text_data = request.form["text"]

    if voice_data and text_data:
        engine = get_engine()
        voices = engine.getProperty('voices')

        for voice in voices:
            if voice.name == voice_data:
                engine.setProperty('voice', voice.id)
                break

        engine.say(text_data)
        engine.runAndWait()

        return jsonify({'success': 'valid data'})
    
    return jsonify({'error': 'missing data'})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)