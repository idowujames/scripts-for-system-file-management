import os
import shutil
import logging

logging.basicConfig(
    level=logging.INFO ,
    filename='file_management_script\logfile.log',
    format='%(asctime)s :: %(levelname)s :: %(message)s'
    )

## Changing directory to point to the downloads folder
os.chdir('C:/Users/DELL/Downloads')

## List of extensions for each file type
software = ['.exe','.iso','msi']

audio = [".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv"]

video = [".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf"]

img = [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif"]

documents = [".csv", ".doc", ".docx", ".pdf", ".ppt", ".pptx",
       ".xls", ".xlsx", ".txt"]

zips = ['.zip']

jupyter_notes = ['.ipynb']
## End List of extensions


## Folders for each file extension
folders = ['Software','Audio','Video','Images','Documents','Zips','Jupyter_Notebooks']


## Saving current working directory to variable
path = os.getcwd()


## Function to create the extension directories if they don't already exist on system 
def create_folders():
    for folder in folders:
        if not os.path.exists(f'{path}/{folder}'):
            os.makedirs(f'{path}/{folder}')
    return folder

## Function to move file based on extension to their respective directories
def file_type(file):
    ext = os.path.splitext(file)[1]
    if ext in software:
        shutil.move(file, f'{path}/Software')
    elif ext in video:
        shutil.move(file, f'{path}/Video')
    elif ext in audio:
        shutil.move(file, f'{path}/Audio')
    elif ext in img:
        shutil.move(file, f'{path}/Images')
    elif ext in documents:
        shutil.move(file, f'{path}/Documents')
    elif ext in zips:
        shutil.move(file, f'{path}/Zips')
    elif ext in jupyter_notes:
        shutil.move(file, f'{path}/Jupyter_Notebooks')
        



## Calling the functions in a try & catch block and logging
## into file, if the script runs successfully or encounters an error
try:
    create_folders()
    for file in os.listdir():
        file_type(file)

    logging.info('Script ran successfully') 


except Exception as e:
    logging.exception("Script encountered an error")
    raise e
