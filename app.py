import pyttsx
from flask import Flask, render_template, request, jsonify, g

app = Flask(__name__)


def get_engine():
    engine = getattr(g, '_engine', None)
    if engine is None:
        engine = g._engine = pyttsx.init()
    return engine


@app.route('/')
def index():
    # engine = get_engine()
    # engine.say("testing this shit")
    # engine.runAndWait()
    return render_template("index.html")


@app.route('/speak', methods=["POST"])
def speak():
    voice = request.form["voice"]
    text = request.form["text"]

    if voice and text:
        engine = get_engine()
        engine.say(text)
        engine.runAndWait()

        return jsonify({'success': 'valid data'})
    
    return jsonify({'error': 'missing data'})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)