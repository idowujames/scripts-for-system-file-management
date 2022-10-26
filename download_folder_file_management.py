import os
import shutil
import logging

logging.basicConfig(level=logging.INFO ,filename='file_management_script\logfile.log', format='%(asctime)s :: %(levelname)s :: %(message)s')

os.chdir('C:/Users/DELL/Downloads')

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

folders = ['software','audio','video','images','documents','zips']

path = os.getcwd()

def create_folders():
    for folder in folders:
        if not os.path.exists(f'{path}/{folder}'):
            os.makedirs(f'{path}/{folder}')
    return folder

def file_type(file):
    ext = os.path.splitext(file)[1]
    if ext in software:
        shutil.move(file, f'{path}/software')
    elif ext in video:
        shutil.move(file, f'{path}/video')
    elif ext in audio:
        shutil.move(file, f'{path}/audio')
    elif ext in img:
        shutil.move(file, f'{path}/images')
    elif ext in documents:
        shutil.move(file, f'{path}/documents')
    elif ext in zips:
        shutil.move(file, f'{path}/zips')

try:
    create_folders()
    for file in os.listdir():
        file_type(file)

    logging.info('Script ran successfully') 


except Exception as e:
    logging.exception("Script encountered an error")
    raise e
