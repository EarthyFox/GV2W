from rich import print
import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('image.jpg')

for (bbox, text, prob) in result:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    print(f'Text: {text}')