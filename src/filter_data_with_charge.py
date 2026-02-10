"""Filter data function."""

import logging
import re
from datetime import date
from pathlib import Path
import pandas as pd
from docx import Document
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from rich import print

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

def separate_names_into_first_last(fullname: str, pat: str) -> dict[str, str]:
    """Separate names into first and last names."""
    match = re.search(pat, fullname, re.DOTALL)

    full_name = fullname.strip() if fullname else "missing"
    first_name = "missing"
    last_name = "missing"

    if match:
        last_name = match.group(1).strip()
        first_name = match.group(2).strip()

    return {
        "full_name": full_name,
        "first_name": first_name,
        "last_name": last_name,
    }

def filter_text_data_updated(directory: str, pat_match: str) -> pd.DataFrame:
    """Open directory and look for data using a robust regular expression."""
    pathdirectory = Path(directory)
    if not pathdirectory.exists():
        print(f"Directory {directory} does not exist.")
        return pd.DataFrame()

    res = [entry for entry in pathdirectory.iterdir() if entry.is_file()]
    list_of_records = []

    for each in res:
        txt = Path(each).read_text()
        # Using DOTALL to allow '.' to match newlines and IGNORECASE for OCR variations
        match = re.search(pat_match, txt, re.DOTALL | re.IGNORECASE)

        if match:
            filename = each.name.replace("_output.txt", "")
            
            # Extracting the 4 captured groups 
            fullname = match.group(1).strip()
            address = match.group(2).strip()
            citystatezip = match.group(3).strip()
            charge = match.group(4).strip()

            # Process names using existing helper
            name_dict = separate_names_into_first_last(fullname, pat="(.*),(.*)")
            
            list_of_records.append(
                [filename, fullname, address, citystatezip, name_dict["last_name"], name_dict["first_name"], charge]
            )
        else:
            logging.debug(f"Pattern did not match for file: {each.name}")

    # Create DataFrame with the new CHARGE column
    data_frames = pd.DataFrame(
        list_of_records,
        columns=[
            "FILENAME",
            "FULLNAME",
            "ADDRESS",
            "CITYSTATEZIP",
            "LASTNAME",
            "FIRST_NAME",
            "CHARGE",
        ],
    )

    if not data_frames.empty:
        # Saving files
        data_frames.to_csv("nate_output.csv", index=False)
        # Using .xlsx extension to match the xlsxwriter engine correctly
        data_frames.to_excel("nate.xlsx", index=False, engine="xlsxwriter")
        print(f"Successfully processed {len(list_of_records)} files.")
    
    return data_frames

def main():
    """Main execution block with robust regex pattern."""
    DIR_UPDATED = "./from_google_vision"

    # NEW ROBUST PATTERN:
    # 1. NAME:\s*\n(.*?)\s*\n -> Captures name, handles optional trailing spaces
    # 2. STREET:\s*\n(.*?)\s*\n -> Captures street
    # 3. CITY/STATE/ZIP:\s*\n(.*?)\s*\n -> Captures city/state/zip
    # 4. .*?CHARGE:\s*\n(?:CODE\s*\n)?(.*?)\n -> Skips intermediate info, 
    #    optionally skips 'CODE' line, then captures the Charge description 
    PAT = (
        r"NAME:\s*\n(.*?)\s*\n"
        r"STREET:\s*\n(.*?)\s*\n"
        r"CITY/STATE/ZIP:\s*\n(.*?)\s*\n"
        r".*?CHARGE:\s*\n(?:CODE\s*\n)?(.*?)\n"
    )

    list_of_files = filter_text_data_updated(directory=DIR_UPDATED, pat_match=PAT)
    print(list_of_files)

if __name__ == "__main__":
    main()