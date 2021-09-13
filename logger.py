import time
import os


def log_it(id,message):
    with open('/home/pi/Desktop/MusicPlayer_API/logs.txt', 'w') as f:
        f.write(f"message\n".format())
        f.close()

def playerStatus():
    with open('/home/pi/Desktop/MusicPlayer_API/playerStatus.txt', 'r') as f:
        status = f.read()
        f.close()
        return status

def seekStatus():
    with open('/home/pi/Desktop/MusicPlayer_API/seekStatus.txt', 'r') as f:
        status = f.read()
        f.close()
        return status

def lastQueue():
    os.path.getmtime("/home/pi/Desktop/MusicPlayer_API/queue.txt")