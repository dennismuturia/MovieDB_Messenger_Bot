'''
* Author: Dennis Muturia
* This is just a basic bot for fun and to play with
* Enjoy 
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def receive_Message():
    #To start off with a bot we need to define two Requests: GET and POST
    if request == 'GET':
        '''
         Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook in the lines of code below. 
        '''
        token_sent = requests.args.get('hub.verify_token')
        return verify_fb_token
if __name__ == '__main__':
    app.run()