from http import server
from flask import Flask
server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, World!'
server.run(port=5001)