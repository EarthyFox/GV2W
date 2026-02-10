"""Automate completion of VA Documents.

Vehicle #', 'Year', 'Make', 'Monthly Lease Pymt', 'Model',
       'Plowing \nvehicle', 'Unit #', 'FFX County\nProperty #', 'Title Number',
       'VIN#', 'Tag#', 'State', 'Odometer', 'EW', 'GW', 'GVWR', 'GVCR',
       'Inspection Date', 'Driver', 'Status', 'Owned/Leased',
       'Annual Registration Fee', 'Renewal Date', 'Assessed Value',
       'Tax Amount', 'Cost-REPAIR', 'Buy/Sell', 'Sell Price',
       'Assigned Status', 'Service Notes', 'Estimate Service Costs',    

"""
from pathlib import Path
from rich import print

# import os
import PyPDF2
import sys

import pandas as pd

from dotenv import load_dotenv

import pdfplumber

from PyPDF2 import PdfReader

from loguru import logger

load_dotenv()

config = {
    "handlers": [
        {"sink": sys.stdout, "level": "INFO"},
        {"sink": "./tmp/mylogs/{time}.log", "level": "DEBUG"},
    ],
}

logger.configure(**config)
logger.info("Write this message to STDOUT and ./tmp/mylogs/timestamp.log")


import pdfplumber


from PyPDF2 import PdfReader, PdfWriter


def write_to_form(input_data, input_pdf_file_name, output_pdf_file_name):
    """Write to pdf form."""

    # print(input_data['Year'])
    # print(input_data['Make'])

    year = input_data["Year"]
    make = input_data["Make"]
    model = input_data["Model"]
    title_number = input_data["Title Number"]
    driver = input_data["Driver"]
    odometer = input_data["Odometer"]
    vin = input_data["VIN#"]
    # bodytype = input_data["Body Type"]
    previous_title_number = ""
    gross_weight = ""

    print(year, make, title_number, driver, odometer, vin)

    reader = PdfReader(input_pdf_file_name)

    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)

    writer.update_page_form_field_values(
        writer.pages[0],
        {
            "WhereGaraged[0]": "Fairfax",
            "MailingAddr[0]": "8003 Forbes Pl. Suite 300",
            "MailCity[0]": "Springfield",
            "MailZip[0]": "22151",
            "MailState[0]": "VA",
            "ResAddr[0]": "11010 Poplar Ford Trl.",
            "City[0]": "Manassas",
            "Zip[0]": "20109",
            "State[0]": "VA",
            "ResAddr[1]": "",
            "City[1]": "",
            "Zip[1]": "",
            "State[1]": "",
            "SSN2[0]": "",
            "SSN2[1]": "",
            "CoOwnerName[0]": "",
            "TeleNum2[0]": "",
            "BusinessStreetAdd[0]": "MountChor Technologies Inc.",
            "SSN1[0]": "20-2482529",
            "TeleNum1[0]": "703-660-4986",
            "LienDate[0]": "",
            "LienName[0]": "",
            "LienholderCode[0]": "",
            "LienHolderAdd[0]": "",
            "LienHolderCity[0]": "",
            "LienHolderZip[0]": "",
            "LienHolderState[0]": "",
            "ResAddr[2]": "",
            "City[2]": "",
            "Zip[2]": "",
            "State[2]": "",
            "ResAddr[3]": "",  # co owners
            "City[3]": "",
            "Zip[3]": "",
            "State[3]": "",
            "TextField1[0]": vin,
            "Year[0]": year,
            "Make[0]": make,
            "TextField1[1]": model,
            # "TextField1[2]": bodytype,
            "TextField1[3]": "",  # empty weight
            "TextField1[4]": "",  # gvwr
            "TextField1[5]": "",  # gcwr
            "TextField1[6]": "White",  # primary color
            "TextField1[7]": title_number,
            "TextField1[8]": "VA",  # state
            "TextField1[9]": "2",  # number of axles
            "TextField1[10]": gross_weight,
            "TextField3[0]": "",  # other fuel type
            "TextField2[0]": "",  # division cBody Typeode
            "CoOwnerAddr[0]": "",
            "CoOwnerCity[0]": "",
            "CoOwnerZip[0]": "",
            "CoOwnerState[0]": "",
            "LesseeName[0]": "",
            "SSN1[1]": "",
            "TeleNum1[1]": "",
            "PurchasedFrom[0]": "Orion Management LLC",
            "PurchaseDate[0]": "",
            "SalesPrice[0]": "",
            "ProcessingFee[0]": "",
            "SalesTax[0]": "",
            "StreetAdd[0]": "8003 Forbes Pl.",
            "City[4]": "Springfield",
            "Zip[4]": "22151",
            "State[4]": "VA",
            "SalesPrice[1]": "",
            "LicNum[0]": "",
            "RentorNum[0]": "",
            "TextField2[1]": odometer,
            "TextField4[0]": "",  # agency code
            "Cell3[0]": "",
            "SignedDate1[0]": "",
            "SignedDate1[1]": "",
            "LesseeName[1]": "",
            "LesseeName[2]": "",
            "LesseeName[3]": "",
        },
    )

    output_file_name = f"./__output_files/{vin}.pdf"
    # print(output_file_name)

    with open(output_file_name, "wb") as output_stream:
        writer.write(output_stream)

def pandas_from_excel():
    file_name = '__input_files/VEHICLE MASTER LIST 08302022.xlsx'
    df = pd.read_excel(open(file_name, 'rb'))
    df2 = df[['Year', 'VIN#', 'Make', 'Model', 'Title Number', 'Tag#', 'Driver', 'Odometer']]
    
    list_of_dicts = df2.to_dict(orient = 'records')
    
    valid_vins = []
    missing_vins = []
    further_info_needed = []
    
    for each in list_of_dicts:
        n = each['VIN#']
        match n:
            case n if len(str(n)) == 17:
                valid_vins.append(each)
    
            case n if str(n) == 'nan':
                missing_vins.append(each)
            case _:
                further_info_needed.append(each)
    
    return dict(
        valid=valid_vins,
        missing=missing_vins, 
        needinfo=further_info_needed,
    )

@logger.catch
def main():
    """Call Main function directly."""
    
    # print(pandas_from_excel())
    # df.dropna(subset=['VIN#'],inplace=True)
    # df2 = df[['Year', 'VIN#', 'Make', 'Title Number', 'Tag#', 'Driver', 'Odometer']]
    # print(df.columns)
    
    
    # print(df2)

    input_data = pandas_from_excel()
    # print(input_data['valid'])

    # onerecord = input_data['valid'][0]
    
    # write_to_form(
    #     input_data=onerecord, 
    #     input_pdf_file_name='__input_files/vsa17a.pdf',
    #     output_pdf_file_name='output_pdf_file_name.pdf',
    # )

    for each_vin in input_data['valid']:
        write_to_form(
            input_data=each_vin,
            input_pdf_file_name='__input_files/vsa17a.pdf',
            output_pdf_file_name='output_pdf_file_name.pdf',
        )

if __name__ == "__main__":
    main()  # pragma: no cover


    # run this to test connectivity only

# def import_excel_data_to_pandas(file_name:str):
#     '''Excel data to pandas.'''

    
#     df = pd.read_excel(open(file_name, 'rb'))
#     # age_no_na = titanic[titanic["Age"].notna()]

#     # df = pd.DataFrame(data, columns = ['Product', 'Price'])
#     df2 = df[['Make', 'VIN#']]

# # df = pd.DataFrame(data, columns = ['Product', 'Price'])

# # print(type(my_dictionary))


