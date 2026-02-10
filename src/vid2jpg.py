import cv2
import datetime
from easygui import fileopenbox

count = 0
filename = fileopenbox()
vidcap = cv2.VideoCapture(filename)
success,image = vidcap.read()
success = True
dt = datetime.datetime.now()
time = dt.microsecond
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*200))    # added this line
    success,image = vidcap.read()
    print ('Read a new frame: ', success, filename)
    # cv2.imwrite( '/home/green/Documents/Code/Python/googlevisiontoword/images/' + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
    cv2.imwrite( '/home/green/Python/Code/googlevisiontoword_working/images/jpg_folder/' + "\frame%d {0}.jpg".format(time) % count, image)     # save frame as JPEG file
    print(count)
    count = count + 1
