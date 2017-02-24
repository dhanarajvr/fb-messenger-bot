from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
from chatterbot import ChatBot
chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train(
"chatterbot.corpus.english"
)
print chatterbot.get_response("hi")