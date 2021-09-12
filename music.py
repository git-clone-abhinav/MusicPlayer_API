import os
import traceback, os, json
from youtube_search import YoutubeSearch
import subprocess

def get_metadata(songname):
    data = {}

    yt = YoutubeSearch(songname, max_results=1).to_json()
    try:
        yt_id = str(json.loads(yt)['videos'][0]['id'])
        link = 'https://www.youtube.com/watch?v='+yt_id
        data['link']=link
    except:
        raise Exception("Song not found.")

    fString = "youtube-dl --get-url -f 140  {}".format(link)
    output = subprocess.check_output(fString, shell=True)
    URL = str(output).lstrip("b'").rstrip("\\n'")
    data['URL'] = URL

    fString = "youtube-dl --get-thumbnail {}".format(link)
    output = subprocess.check_output(fString, shell=True)
    thumbnail =  str(output).lstrip("b'").rstrip("\\n'")
    data['thumbnail'] = thumbnail

    fString = "youtube-dl --get-title  {}".format(link)
    output = subprocess.check_output(fString, shell=True)
    title = str(output).lstrip("b'").rstrip("\\n'")
    data['title'] = title

    return data
