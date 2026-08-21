from flask import Flask
from database import initialize_database


app = Flask(__name__)


initialize_database()


@app.route("/")
def home():
    return """
    <h1>CyberLab CTF</h1>
    <p>Welcome to the CyberLab Capture The Flag platform!</p>
    <p>Project Status: Online</p>
    """


if __name__ == "__main__":
    app.run(debug=True)