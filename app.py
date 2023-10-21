"""Display metadata from experience.afrotech.com"""
from flask import Flask, render_template
import bios

app = Flask(__name__)

@app.route('/')
def home():
    '''Return the home page'''
    events = bios.read('events_list.json')
    return render_template('index.html', events=events)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
