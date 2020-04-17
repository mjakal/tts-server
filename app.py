from flask import Flask, render_template, request, jsonify
from tts import get_tts_voices, get_engine_status, speak_text, stop_speaking

# Global variables
PORT = 4000
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
    voice_data = request.form.get("voice", "")
    text_data = request.form.get("text", None)
    
    if text_data:
        engine_status = get_engine_status()

        # Check if tts engine is currently in use
        if engine_status["busy"]:
            return jsonify({'warning': 'Engine currently busy, please wait...'})
        
        speak_text(voice_data, text_data)

        return jsonify({'success': 'reading text'})
    
    return jsonify({'error': 'Text param not set.'})


# Speak text api
@app.route('/api/v1/stop')
def get_request_stop():
    stop_speaking()

    return jsonify({'success': 'reading stopped'})


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)