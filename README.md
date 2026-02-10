# googlevisiontoword
Pictures to google vision to MS Word Output
pip install --upgrade google-api-python-client
## to process google jpg files put them in the directory referenced in your .env file
The .env file is not uploaded to github so you have to create it locally
here is an example .env file
OOGLE_APPLICATION_CREDENTIALS='R
## need to login to google to run the image recognition here is an example
paula's changes part 2
GOOGLE_APPLICATION_CREDENTIALS='keys/REDACTEDFILENAME.json'

rm vscode ➜ /workspaces/googvisioncontainer/googlevisiontoword (main ✗) $ 

# TODO PUTTHISINCODEBLOCK
vscode ➜ /workspaces/googvisioncontainer/googlevisiontoword (main ✗) $ cat .env
EXCEL_OUTPUT = "__output_files/output.xlsx"
JPG_IMAGE_DIRECTORY = './images/jpgfolder'


## Instructions
We do not save the actual files in github, but there are test files in the test directory

### This is work in progress please create branch and do merge request and do not push directly to main

#### TODO

TAKE these todos and put them into github as issues and put them on kanban project board

Do the deduplication of data in the output excel file using unique in python

Get the word output working


Remove lines with Unknown and put in file called to investigate


setup testing using the test files in tests/...

setup testing using the faker library called in conftest

setup automatic documentation using sphynx or equivalent library

vscode ➜ /workspaces/googvisioncontainer/googlevisiontoword (main ✗) $ cat .env
EXCEL_OUTPUT = "__output_files/output.xlsx"
JPG_IMAGE_DIRECTORY = './images/jpgfolder'
