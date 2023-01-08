from flask import Flask
heloflask = Flask(__name__)

@heloflask.route('/')
def hello_world():
    return 'This is my first API call!'