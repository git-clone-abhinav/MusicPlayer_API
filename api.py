from flask import Flask
from flask import jsonify
from flask import redirect
from flask_restful import Api
from flask_cors import CORS, cross_origin
import logger
import os.path
from os import path
import music 

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
    if path.exists("/home/pi/Desktop/MusicPlayer_API/logs.txt"):
        status = logger.read()
        return status, 200 # Everything Okay Data is returned

@app.route('/songlink/<songname>', methods=['GET'])
@cross_origin()
def the_link(songname):
    try:
        song = music.get_song_link(songname)
        return song, 200 # Everything okay
    except:
        return "Song Not Found", 301 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1200)
