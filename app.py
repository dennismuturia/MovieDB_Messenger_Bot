'''
* Author: Dennis Muturia
* This is just a basic bot for fun and to play with
* Enjoy 
'''
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAC5NdZCdjbgBAFnTChwrNmaOfizPEsHonPwZBAiuXo0PcdSxxDTRM9lTyBWfpq26FFu6p96r91eVOR8uq9xoy2Jjp6wjPrZByrbU3MXedAPsV8vRpgONpDGM0kCkkcsZA67PfdQs7zA2fvN1TCgnvPxJfdG8eE7MIkS1UXzZA6LFaTB6MlwN'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

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
    
    #If the request was a post request then procedd with sending a message back to the user
    else:
        #Getting the message the user sent the bot
        output = request.get_json()
        for event in output:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    #Facebook Messenger ID for user so we know where to send response back to
                    recepient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recepient_id, response_sent_text)
                    #If a user send a photo, Video of a media file
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message processed"

   
def verify_fb_token(token_sent):
    '''
    I will take token sent by facebook and verify it matches the verify token you sent
    if they match, allow the request, else return an error 
    '''
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid Verification token"

def send_message(recepient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recepient_id, response)
    return "success"

if __name__ == '__main__':
    app.run()