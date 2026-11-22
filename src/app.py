from flask import Flask

app = Flask(__name__)


@app.route("/")
def strona_glowna():
    return "Hello World! – Algorithm Visualizer"


if __name__ == "__main__":
    app.run()
