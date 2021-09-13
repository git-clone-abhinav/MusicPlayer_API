import music

def checkQueue():
    with open ("/home/pi/Desktop/MusicPlayer_API/queue.txt","r") as f:
        songs = f.readlines()
        songList = []
        for song in songs:
            songData = song.rstrip("\n").split(", ")
            print(songData)
            songList.append(songData)
        

def updateQueue(songData):
    with open('/home/pi/Desktop/MusicPlayer_API/playerstatus.txt', 'a') as f:
        f.write(f"{songData}\n".format())
        f.close()

def make_songData(name):
    data = music.get_metadata(name)
    songData = (data['title'], data['thumbnail'], data['URL'], data['link'])
    fString = ", ".join(songData)
    return fString

def addSong(name):
    updateQueue(make_songData(name))
