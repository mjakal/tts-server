import pyttsx
from flask import Flask, render_template, g
# from flask import g

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)