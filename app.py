import os
import sys
import json
import mandrain
import requests
from flask import Flask, request
import chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer

from chatterbot import ChatBot
chatbot = ChatBot("Training Example",read_only=True,
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    database="./database.json")

chatbot.set_trainer(ChatterBotCorpusTrainer)
'''
print "training..."

chatbot.train(
"chatterbot.corpus.english.conversations"
)
print "training finished"'''
print chatbot.get_response("yes")
import grammar_check
tool = grammar_check.LanguageTool('en-GB')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's face-book ID
                    message_text = messaging_event["message"]["text"]  # the message's text
		    '''		    
			if len(message_text.split())>2:
			text = message_text
			matches = tool.check(text)
			gram=grammar_check.correct(text, matches)
                    	mess=chatbot.get_response(message_text)
                    	send_message(sender_id, str(mess))
			send_message(sender_id, "just checking for grammar...")

			send_message(sender_id, str(gram))
		    else:
			mess=chatbot.get_response(message_text)
            		send_message(sender_id, str(mess))'''
                k = mandrain.Mandrains()
		pin=k.eng2pyin(message_text)
	        if pin!=None:
			send_message(sender_id,"the PinYin is"+"\n"+pin)
		else:
			send_message(sender_id,"PinYin not found")

                if messaging_event.get("delivery"):  # delivery confirmation
                	pass

                if messaging_event.get("optin"):  # optin confirmation
                	pass

               	if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                   	pass

    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
