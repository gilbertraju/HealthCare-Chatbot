from flask import Flask, render_template, request
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


os.remove("db.sqlite3")
english_bot = ChatBot('Bot')
english_bot.set_trainer(ListTrainer)

for file in os.listdir('data'):
        convData = open('data/' + file).readlines()
        english_bot.train(convData)

app = Flask(__name__)

english_bot = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
   },

],

trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)


@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = str(english_bot.get_response(userText))
    return response
if __name__ == "__main__":
    app.run()
