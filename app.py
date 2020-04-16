from flask import Flask, render_template, request, jsonify
from tts import get_tts_voices, speak_text, stop_speaking

# Global variables
PORT = 3000
DEBUG = False

# Instance of Flask app
app = Flask(__name__)


@app.before_first_request
def run_before_first_request():
    speak_text("", "")


# Get index page
@app.route('/')
def index():
    return render_template("index.html")


# Get voices api
@app.route('/api/v1/voices')
def get_request_voices():
    voice_names = get_tts_voices()
    
    return jsonify(voice_names)


# Speak text api
@app.route('/api/v1/speak', methods=["POST"])
def post_request_speak():
    voice_data = request.form["voice"]
    text_data = request.form["text"]
    
    if text_data:
        speak_text(voice_data, text_data)

        return jsonify({'success': 'valid data'})
    
    return jsonify({'error': 'missing data'})


# Speak text api
@app.route('/api/v1/stop')
def get_request_stop():
    stop_speaking()

    return jsonify({'success': 'reading stopped'})


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)