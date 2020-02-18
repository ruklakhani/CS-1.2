from flask import Flask, render_template
from dictogram import *


word_list = open_file("text.txt")
frank_hist = Dictogram(word_list)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/randomwords')
def random_words():
    rand_words = []
    for _ in range(5):
        rand_words.append(frank_hist.sample())
    return render_template('random_words.html', word_list=rand_words)