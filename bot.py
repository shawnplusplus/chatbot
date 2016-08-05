from flask import Flask, Response, request
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
global AI
AI = ChatBot("papajohns")
AI.set_trainer(ChatterBotCorpusTrainer)
AI.train("chatterbot.corpus.english")

@app.route("/")
def hello():
        return "Hello World!"

@app.route("/chatbot/", methods=['POST'])
def bot():
    context = request.get_json()
    global AI
    r = AI.get_response(context['text'])
    resp = Response(response=str(r), status=200, mimetype="application/json")
    return resp

if __name__ == "__main__":
    app.run()
