"""Uses google image library to extract text from images."""

import io
import os
import sys

import time

from datetime import date
from pathlib import Path

# import pandas as pd

from dotenv import load_dotenv

from google.cloud import vision

from loguru import logger

config = {
    "handlers": [
        {"sink": sys.stdout, "level": "INFO"},
        {"sink": "./tmp/mylogs/{time}.log", "level": "DEBUG"},
    ],
}
logger.configure(**config)
logger.info("Write this message to STDOUT and /tmp/mylogs/timestamp.log")

load_dotenv()

#jpg_image_directory = os.environ["JPG_IMAGE_DIRECTORY"]
jpg_image_directory = "./images/jpg_folder"


p = Path(jpg_image_directory)


files_in_directory = list(p.glob("**/*.jpg*"))


def detect_text(path):
    """Detect text in the file using google vision API."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # img_text = list()
    for text in texts:
        vertices = [
            "({},{})".format(vertex.x, vertex.y)
            for vertex in text.bounding_poly.vertices
        ]

        # print(text.description)

        # img_text.append(text.description)

    # positive_thoughts = pd.DataFrame(img_text, columns=['Text'])
    # file_name = 'Positive_Thoughts_From_Google_Vision.csv'
    # positive_thoughts.to_csv(file_name, index=False)

    # return texts

    # print("bounds: {}".format(",".join(vertices)))

    # "https://cloud.google.com/apis/design/errors"

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "see code ".format(response.error.message)
        )

    # import pandas as pd

    # datapandas = pd.DataFrame(texts, columns=['Text'])
    # print(datapandas)

    return texts


# print("__________START OF FILE_____")
# for each in files_in_directory:
#     print(f"file name is {str(each)}")
#     text = detect_text(str(each))
#     print("__________NEW__RECORD_____")
#     print(text)
#     print("__________END__RECORD_____")

# print("__________END OF FILE_____")

# def oops():
#     'one' + 1


# datapandas = pd.DataFrame(text.description, columns=['Text'])
# print(datapandas)


@logger.catch
def main():
    """Call Main function directly."""
    # print(f"processing files in:{jpg_image_directory}:")
    # print("__________START OF FILE_____")

    # logger.debug('About to do an oops.')
    # oops()
    # sys.exit(main())

    for each in files_in_directory:
        print(f"file name is {str(each)}")
        text: str = "\nEMPTY_RECORD\n"
        # CALL TO GOOGLE STARTS HERE
        try:
            today = date.today()
            d4 = today.strftime("%b-%d-%Y")

            tmp_file_name = f"./from_google_vision/{each.name}_{d4}_out.txt"

            with open(tmp_file_name, "w", encoding="utf-8") as file_handle:
                # text = detect_text(str(each))
                texts = detect_text(str(each))
                for text in texts:
                    # print(dir(text))
                    # print(text.description)

                    file_handle.write(text.description)

            #time.sleep(1)
            # print("This message will be printed after a wait of 5 seconds (Changed to 3 seconds)")

        except Exception as _error:
            raise ValueError("Investigate error.") from _error


if __name__ == "__main__":
    main()  # pragma: no cover
