'''
* Author: Dennis Muturia
* This is just a basic bot for fun and to play with
* Enjoy 
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def receive_Message():
    return("Hello world")

if __name__ == '__main__':
    app.run()