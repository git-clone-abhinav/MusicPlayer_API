from flask import Flask
from flask import jsonify
from flask import redirect
from flask_restful import Api
from flask_cors import CORS, cross_origin
import logger
import os.path
import os
from os import path
import music
import queueGen

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#api = Api(app)

@app.route('/hello/', methods=['GET'])
@cross_origin()
def welcome():
    return "Hello World!"

@app.route('/status/', methods=['GET'])
@cross_origin()
def status():
    status = logger.PlayerStatus()
    lm = os.path.getmtime("/home/pi/Desktop/MusicPlayer_API/queue.txt")
    data = {'status' : status,'lm' : lm}
    return jsonify(data), 200 # Everything Okay Data is returned

@app.route('/metadata/<name>', methods=['GET'])
@cross_origin()
def metadata(name):
    try:
        return jsonify(music.get_metadata(name)), 200# Everything okay
    except Exception as e:
        return e, 301
        
@app.route('/add/<name>', methods=['GET'])
@cross_origin()
def add(name):
    try:
        queueGen.addSong(name)
        return "song successfully added", 200# Everything okay
    except Exception as e:
        return e, 301

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1200)
