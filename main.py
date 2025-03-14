"""
A simple Flask app that returns a funny message.
"""

from flask import Flask

app = Flask(__name__)


def get_funny_message():
    """Returns a funny message."""
    return "Azure DevOps Dev -> Warning: Low battery! Please charge your developer..."


@app.route("/")
def home():
    """Home route that returns the funny message."""
    return f"<pre>{get_funny_message()}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
