from flask import Flask, render_template, request
from raffle import Raffle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/and_the_winner_is')
def back_to_index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    username = request.form['username']
    password = request.form['password']

    raffle = Raffle(username, password)

    post_hash = request.form['postHash']
    comments_total = request.form['commentsTotal']

    winner = raffle.raffle(post_hash, comments_total)

    return render_template('result.html', data=winner)

