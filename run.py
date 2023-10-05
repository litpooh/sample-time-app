from flask import Flask
from datetime import datetime, timedelta
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    time = datetime.now()
    correct_time = time - timedelta(hours=4, minutes=0, seconds=0)
    return correct_time.strftime("%H:%M:%S")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
