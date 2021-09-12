import time

def log_it(id,message):
    with open('/home/pi/Desktop/MusicPlayer_API/logs.txt', 'w') as f:
        f.write(f"message\n".format())
        f.close()

def read():
    with open('/home/pi/Desktop/MusicPlayer_API/logs.txt', 'r') as f:
        status = f.read()
        f.close()
        return status