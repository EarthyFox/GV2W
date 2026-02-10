"""Filter data function."""

from cgitb import reset
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import logging

# import os
import re

from datetime import date

from pathlib import Path

#from PyPDF2 import PdfReader

from docx import Document

from dotenv import load_dotenv

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape

from rich import print

import pandas as pd

# from rich import print

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

# excel_output = os.environ["EXCEL_OUTPUT"]


# def easy_gui_here():
#     '''
#     # easy gui instructions here
#     # msg = "Pick your image directory"
#     # image_directory = easygui.fileopenbox(msg="Choose a file")
#     # print(image_directory)
#     '''


# def separate_address_into_city_state(city: str, pat: str) -> dict[str, str]:
#     """Separate names into first and last names."""
#     my_dict = dict(
#         city=full_name,
#         address_name=first_name,
#         last_name=last_name,
#     )

#     return my_dictt
def get_list_of_completed_images(directory: str):
    """Move image files out of jpg folder."""
    pathdirectory = Path(directory)
    res = []
    for entry in pathdirectory.iterdir():
        if entry.is_file():
            string = entry.name
            new_string = string.replace("_output.txt", "")
            res.append(new_string)
    return res


def move_completed_from_images(list_of_files: list[str, str]):
    """Get list of completed and move from images."""
    # DIR = './tmp/txtfiles/'
    # list_to_move = get_list_of_completed_images(DIR)

    # print(list_to_move)
    # list_to_move = ['IMG_7997.JPG','IMG_8072.JPG']
    src_dir = "images/jpg_folder/"
    dst_dir = "images/jpg_folder_completed/"

    for file_name in list_of_files:
        try:
            path = Path(f"{src_dir}{file_name}")

            if path.is_file():
                Path(f"{src_dir}{file_name}").rename(f"{dst_dir}{file_name}")

        except Exception as _error:
            raise ValueError("Investigate error.") from _error

    return True


# def read_tmp_files_in_and_get_description(
#     directory: str, pat: str = None
# ) -> list[str, str]:
#     """Open file get line for processing.

#     description: "LI\nSES\nAGES\nDEFENDANT\nNAME:\nCHEN,
#     JINGRU\nSTREET:\n42847 PILGRIM SQ\nCITY/STATE/ZIP:\nCHANTILLY,
#     VA 20152\nCASE INFO\nOFFENSE DATE:\n9/3/2022\nHEARING TIME:
#     \n09:00 AM\nCHARGE AND DISPOSITION\nCHARGE:\nFAIL TO STOP-RIGHT ON RED\nAMENDED
#     CHARGE:\nUNIT #:\nH5186\nDISPOSITION:\nDOCUMENT IMAGES: 1\nHEARING DATE:\n12/7/2022\n
#     JUDGE:\nDATE OF BIRTH:\nATTORNEY:\nAPP\nCOMPLAINANT:\nWILL, A\nCOUR\nCODE SECTION:\n46.2-835\n
#     AMENDED CODE:"
#     """
#     pathdirectory = Path(directory)
#     all_data = []
#     for entry in pathdirectory.iterdir():
#         # print(entry)
#         with open(entry, "r") as file_input:
#         #     head = [next(file_input) for x in range(2)]
#         #     list1 = head[1].split("\n")
#         #     for each in list1:
#         #         list2 = each.split("\\n")
#         #         all_data.append(list2)

#     return all_data





def read_list_get_name(my_list, pat):
    """Read list and get name and address."""
    # match = re.search(pat, fullname, re.DOTALL)
    # pat = r"(DEFENDANT\nNAME:(.*))STREET:(.*)CITY/STATE/ZIP:\n(.*)CASE I"

    # string = " ".join([str(item for item in my_list)])

    # print(string)
    # print(each.split(','))
    # print(len(each))
    # match3 = re.search(pat, each, re.DOTALL)

    # if match3:
    #     fname = match3.group(2)
    #     address = match3.group(3)
    #     citystatezip = match3.group(4)

    #     address = address.strip()
    #     fname = fname.strip()
    #     citystatezip = citystatezip.strip()

    # match = re.search(pat, fullname, re.DOTALL)

    full_name = "missing"
    first_name = "missing"
    last_name = "missing"

    # if match:
    #     print(f"Full match:match_0:{match.group(0)}:")
    #     print(f"found match_1 in {match.group(1)}")
    #     print(f"found match_2 in {match.group(2)}")
    #     first_name = match.group(2)
    #     last_name = match.group(1)
    #     full_name = match.group(0)

    my_dict = dict(
        full_name=full_name,
        first_name=first_name,
        last_name=last_name,
    )

    return my_dict

    #     # check if it a file
    #     if entry.is_file():
    #         res.append(entry)

    # list_of_records = []

    # for each in res:
    #     txt = Path(each).read_text()
    # for each in directory:


def separate_names_into_first_last(fullname: str, pat: str) -> dict[str, str]:
    """Separate names into first and last names.

    fullname: str full name to separate
    pat: str pattern match to use to separate
    example = BRANDI TERRESITA

    output:
    
    first_name: str  = BRANDI TERRESITA
    last_name: str = DECOTEAU
    Note this client prefers upper case
    """
    match = re.search(pat, fullname, re.DOTALL)

    full_name = "missing"
    first_name = "missing"
    last_name = "missing"

    if match:
        print(f"Full match:match_0:{match.group(0)}:")
        print(f"found match_1 in {match.group(1)}")
        print(f"found match_2 in {match.group(2)}")
        first_name = match.group(2)
        last_name = match.group(1)
        full_name = match.group(0)

    my_dict = dict(
        full_name=full_name,
        first_name=first_name,
        last_name=last_name,
    )

    return my_dict


def filter_text_data(directory: str, pat_match: str) -> pd.DataFrame:
    """Open directory and look for data using a regular expression."""
    pathdirectory = Path(directory)
    res = []
    for entry in pathdirectory.iterdir():
        # check if it a file
        if entry.is_file():
            res.append(entry)

    list_of_records = []

    for each in res:
        txt = Path(each).read_text()

        match3 = re.search(pat_match, txt, re.DOTALL)

        if match3:
            fname = match3.group(2)
            address = match3.group(3)
            citystatezip = match3.group(4)

            address = address.strip()
            fname = fname.strip()
            citystatezip = citystatezip.strip()

            list_of_records.append([fname, address, citystatezip])

        data_frames = pd.DataFrame(
            list_of_records, columns=["FULLNAME", "ADDRESS", "CITYSTATEZIP"]
        )

    return data_frames


def df_to_word(data: dict, report_name: str) -> Document:
    """Convert data frame to word document.

    # assert type(data) == dict, 'data has to be dict'
    # assert '.docx' in report_name, 'report_name has to be a .docx file'
    """
    try:
        df = pd.DataFrame(data)
        doc = Document()
        table = doc.add_table(df.shape[0] + 1, df.shape[1])

        for j in range(df.shape[-1]):
            table.cell(0, j).text = df.columns[j]

        for i in range(df.shape[0]):
            for j in range(df.shape[-1]):
                table.cell(i + 1, j).text = str(df.values[i, j])

        doc.save(f"./{report_name}")
        return data, report_name

    except Exception as _error:
        raise ValueError("Investigate error.") from _error


def template_w_pathlib(input_dict_name: str, template_name: str) -> str:
    """Prepare output using template and dictionary.

    Take dictionary and template file.  Combine to create
    template output.
    Returns:
    output_text (str): output text
    """
    trim_blocks = True
    lstrip_blocks = True
    keep_trailing_newline = False

    templateloader = FileSystemLoader(searchpath="./templates")
    templatenv = Environment(
        autoescape=select_autoescape(["html", "htm", "xml"]),
        loader=templateloader,
        trim_blocks=trim_blocks,
        lstrip_blocks=lstrip_blocks,
        keep_trailing_newline=keep_trailing_newline,
    )
    template = templatenv.get_template(template_name)
    return template.render(jinja_var=input_dict_name)


def filter_text_data_updated(directory: str, pat_match: str) -> pd.DataFrame:
    """Open directory and look for data using a regular expression."""
    pathdirectory = Path(directory)
    res = []
    for entry in pathdirectory.iterdir():
        # check if it a file
        if entry.is_file():
            res.append(entry)

    list_of_records = []

    for each in res:
        txt = Path(each).read_text()

        match = re.search(pat_match, txt, re.DOTALL)

        if match:
            # print(f'group0::{match.group(0)}')
            # print(f'group1 name ::{match.group(1)}')
            # print(f'group2 address::{match.group(2)}')
            # print(f'group3::{match.group(3)}')
            # print(f'group4::{match.group(4)}')
            # print(f'group5::{match.group(5)}')
            # print(f'group6::{match.group(6)}')
            filename = each.name
            filename = filename.replace("_output.txt", "")

            fullname = match.group(1)
            address = match.group(2)
            citystatezip = match.group(3)
            last_name = separate_names_into_first_last(fullname, pat="(.*),(.*)")[
                "last_name"
            ]
            first_name = separate_names_into_first_last(fullname, pat="(.*),(.*)")[
                "first_name"
            ]

            address = address.strip()
            fullname = fullname.strip()
            citystatezip = citystatezip.strip()
            list_of_records.append(
                [filename, fullname, address, citystatezip, last_name, first_name]
            )

        data_frames = pd.DataFrame(
            list_of_records,
            columns=[
                "FILENAME",
                "FULLNAME",
                "ADDRESS",
                "CITYSTATEZIP",
                "LASTNAME",
                "FIRST_NAME",
            ],
        )

    today = date.today()

    d4 = today.strftime("%b-%d-%Y")
    print(data_frames)
    data_frames.to_csv("nate_output.csv")
    read_csv_file = pd.read_csv("nate_output.csv")
    convert_file_to_xls = read_csv_file.to_excel("nate.xls", index='False', engine="xlsxwriter")

    return data_frames


def read_pdf_data(input_pdf_file_name):
    '''Get data from pdf into system.
    
    returns as text'''

    list_in_text_fmt = []

    reader = PdfReader(input_pdf_file_name)
    pages = reader.pages
    for each in pages:
        each.extract_text()
        list_in_text_fmt.append(each.extract_text())

    return list_in_text_fmt
    
def convert_text_to_info(input_data):
    '''Get data from pdf into system.'''
    # print(input_data)
    
    PAT = re.compile(r'.*')
# >>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
# ['12', '11', '10']

    pat_match = r'(.*)'

    for txt in input_data:
        # txt = txt.split(",")
        match = re.search(PAT, txt)
    
        if match:
            print(f'group0::{match.group(0)}')
            # print(f'group1 name ::{match.group(1)}')
            # print(f'group2 address::{match.group(2)}')
            # print(f'group3::{match.group(3)}')
            # print(f'group4::{match.group(4)}')
            # print(f'group5::{match.group(5)}')
            # print(f'group6::{match.group(6)}')
            # filename = each.name
            # filename = filename.replace("_output.txt", "")

        # print(each2)

    # convert file 
    # df = pd.read_csv(input_data[0], sep=" ", header=None)
    
    # df = pd.read_csv(StringIO(input_data[0].read()))

    # # data.columns = ["a", "b", "c", "etc."]
    # return df







def main():
    """Call Main function directly."""
    # alldata = read_tmp_files_in_and_get_description(directory="./tmp/txtfiles/")
    # print(type(alldata[0]))
    # alldata = pd.DataFrame(alldata[0])
    # print(alldata.head())
    pat = (r"(DEFENDANT\nNAME:(.*))STREET:(.*)CITY/STATE/ZIP:\n(.*)CASE I",)

    # read_list_get_name(alldata, pat=pat)

    # DIR = "./tmp/txtfiles"
    DIR_UPDATED = "./from_google_vision"

    PAT = "NAME:\n(.*)\nSTREET:\n(.*)CITY/STATE/ZIP:\n(.*)\nCASE.*\n"

    # # TER\nCITY/STATE/ZIP:\nALDIE

    list_of_files = filter_text_data_updated(directory=DIR_UPDATED, pat_match=PAT)
    # # list_of_files = filter_text_data_updated(directory=DIR, pat_match=PAT)

    # # list_of_files = get_list_of_completed_images(directory=DIR)

    print(list_of_files)
    # input_file = './__input_files/FOIA-W018835_Arrests_Redacted_.pdf'

    # result = read_pdf_data(input_pdf_file_name=input_file)
    # # print(result)
    # convert_text_to_info(result)

        

    # print(result[0].extract_text())


    # move_completed_from_images(list_of_files=list_of_files)

    # archive = PffArchive("./archive/danbak.pst.pst")
    # eml_out = Path(Path.cwd() / "emls")


if __name__ == "__main__":
    main()  # pragma: no cover
