
from flask import Flask, render_template, request
from appbackend import search_word
import re
import time

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')

def index():
    print("Rendering time at:",time.time())
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    clue = request.form['clue']
    letters = request.form['letters']

    clue = f'^{clue}$'
    regex = re.compile(clue, re.IGNORECASE)

    letters = list(letters) if letters else None

    if letters:
        results = search_word(regex, letters)
    else:
        results = search_word(regex)

    if results:
        return render_template('wordleresults.html', results=results)
    else:
        return render_template('wordlenoresults.html')

if __name__ == '__main__':
    app.run(debug=True)