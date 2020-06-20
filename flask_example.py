from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Khajan'

def new_function():
	print("i love this new config")


def hello_world():
	print('hello khjan')
