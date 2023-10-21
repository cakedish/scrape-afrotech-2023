from flask import Flask, render_template
import bios

app = Flask(__name__)
events = bios.read('events_list.json')

@app.route('/')
def home():
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
