from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Home"

@app.route("/mock")
def mock():
    return "mock"

@app.route("/api/api_send_box")
def api():
    return "api_send_box"

@app.route("/api/grpcurl")
def grpcurl():
    return "grpcurl"

@app.route("/api/short_link")
def short_link():
    return "short_link"

