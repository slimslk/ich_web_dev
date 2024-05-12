from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/user/<string:name>")
def user(name: str):
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run()
