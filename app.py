from flask import Flask, render_template
from dictogram import *
from pymongo import MongoClient
import os 

word_list = open_file("text.txt")
frank_hist = Dictogram(word_list)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweetGen')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
tweets = db.tweets

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def random_words():
    rand_words = []
    for _ in range(5):
        rand_words.append(frank_hist.sample())
    return render_template('random_words.html', word_list=rand_words)

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
