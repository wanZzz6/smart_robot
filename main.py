from flask import Flask
from flask import render_template
from audio_bp import audio_recognize



app = Flask(__name__)  # type:Flask
app.register_blueprint(audio_recognize.au_bp)

@app.route("/")
def index():
    return render_template("index.html")

app.run("localhost", 5000, debug=True)
