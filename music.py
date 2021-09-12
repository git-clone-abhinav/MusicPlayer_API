import os
import traceback, os, json
from youtube_search import YoutubeSearch
import subprocess
def get_song_link(songname):
    yt = YoutubeSearch(songname, max_results=1).to_json()
    try:
        yt_id = str(json.loads(yt)['videos'][0]['id'])
        link = 'https://www.youtube.com/watch?v='+yt_id
        return get_dl_link(link)
    except:
        raise Exception("Song not found.")

def get_dl_link(link):
    """
    Returns the highest quality .m4a file link of the song provided

    Example
    > get_dl_link(https://www.youtube.com/watch?v=wqZnO71PBis)
     https://r2---sn-g5pauxapo-qxal.googlevideo.com/videoplayback?expire=1631406085&ei=pfM8Ybz3J_itz7sPgZa1wAc&ip=103.66.74.145&id=o-APvYtDbaHf0xuS99XEif3N-oKINlXOxCLvW4yxowCMl7&itag=140&source=youtube&requiressl=yes&mh=pk&mm=31%2C29&mn=sn-g5pauxapo-qxal%2Csn-qxa7snee&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=807500&vprv=1&mime=audio%2Fmp4&ns=bXapoJoUEn9TTkQ9Dd76likG&gir=yes&clen=1556930&dur=96.130&lmt=1630657844858371&mt=1631383995&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=3hcsuX3okp0OLCR5&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALoY9UW0VS-ZtzrLNBpO9_rS2ZEDnVXV-KIUq8onUDs4AiAyY3em9KbicUfTn1IbQV8q5WHzca7LxT2Xv4pfQw1_lg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAIwdJREOWDaP3kKvr7AJ4spHvpjMqDegdUj5VrJKblD4AiBzFvWrdGEj4tvWdJAhdY0yd81vr9Uu3gxtbZxQkVofrQ%3D%3D
    """
    
    fString = "youtube-dl --get-url -f 140  {}".format(link)
    output = subprocess.check_output(fString, shell=True)
    #output = str(os.system(fString)) # Can't use this since: https://unix.stackexchange.com/questions/418616/python-how-to-print-value-that-comes-from-os-system
    # print("## Output ##")
    # print(output)
    # print(type(output))
    return output

    