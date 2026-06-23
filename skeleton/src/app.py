from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, dummy human! :) ',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/status')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

@app.route('/api/v1/dashboard')

def dashboard():
    return "Hello World"


@app.route("/")
def home():
    return "OK", 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")

