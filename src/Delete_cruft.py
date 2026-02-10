import os

def cleanup():
    dir = os.getcwd()
    files = input()
    files = dir+"/"+files
    video_files = dir+"/"+"Videos/"
    try:
        os.remove(files)
        os.remove(video_files)
    except OSError as e:
        print("Error deleting files", e)
