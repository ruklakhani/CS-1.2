from flask import Flask, render_template, request
from dictogram import *
from markov import *
from pymongo import MongoClient
import os 

word_list = open_file("text.txt")
frank_hist = Dictogram(word_list)
markov_chain = MarkovChain(word_list)

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
    try:
        num = request.args['num']
    except:
        num = 7
    rand_words = []
    for _ in range(5):
        rand_words.append(frank_hist.sample())
    
    try:
        sentence = markov_chain.walk(int(num), frank_hist.sample())
    except:
        sentence = markov_chain.walk(7, frank_hist.sample())
    return render_template('random_words.html', word_list=rand_words, sentence=sentence )

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
