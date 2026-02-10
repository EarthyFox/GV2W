#!/bin/bash 

# bash for loop
for f in $( ls jpgfolder/ ); do
      convert jpgfolder/$f \
      -sampling-factor 4:2:0 \
      -strip \
      -quality 85 \
      -interlace Plane \
        -gaussian-blur 0.05 \
        -colorspace RGB \
        \jpgfolder/$f-small.jpg

import cv2 # not needed but left in for now 
import pytesseract  # not needed since using google now
import pandas as pd  # leaving in since we will be using pandas for wrangling soon
DIRECTORY = './images/jpgfolder_converted'
from pathlib import Path
import numpy as np

p = Path(DIRECTORY)
# creates a list of the files in the directory
files_in_directory = list(p.glob('**/*.JP*'))

# this is the google piece that calls the google cloud API
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

print('__________START OF FILE_____')
for each in files_in_directory:
    print(f'file name is {str(each)}')
    # this calls the function above that reaches out to google
    # this should be behind a try except block
    # we will clean it up for production
    # the text puts it in a variable so that we can print it in a variable easier
    text = detect_text(str(each))
    print('__________NEW__RECORD_____')
    print(text)
    print('__________END__RECORD_____')

print('__________END OF FILE_____')
:wq

