import os
import shutil
import logging

logging.basicConfig(
    level=logging.INFO ,
    filename='logfile.log',
    format='%(asctime)s :: %(levelname)s :: %(message)s'
    )

## Changing directory to point to the downloads folder
os.chdir('C:/Users/DELL/Downloads')

## File Type & extensions for each file type in Dictionary
files_type = { 
    'Software' : ['.exe','.iso','.msi'],

    'Audio' : [".3ga", ".aac", ".ac3", ".aif", ".aiff",
                ".alac", ".amr", ".ape", ".au", ".dss",
                ".flac", ".flv", ".m4a", ".m4b", ".m4p",
                ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
                ".opus", ".qcp", ".tta", ".voc", ".wav",
                ".wma", ".wv"],

    'Video' : [".webm", ".MTS", ".M2TS", ".TS", ".mov",
                ".mp4", ".m4p", ".m4v", ".mxf",".mkv"],

    'Images' : [".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
                ".gif", ".webp", ".svg", ".apng", ".avif"],

    'Documents' :[".csv", ".doc", ".docx", ".pdf", ".ppt", ".pptx",
                ".xls", ".xlsx", ".txt"],

    'Zips' : ['.zip'],

    'Jupyter_notes' : ['.ipynb']

}

## Saving current working directory to variable
path = os.getcwd()

def move_file(file_):
    """
        Function to move file based on extension to their respective directories.
      
        Using absolute path in shutil.move() to avoid error raised if the same file 
        already exist in destination folder

    """
    ext = os.path.splitext(file)[1]

    # Iterating through the keys of the file_type dictionary
    for folder in files_type:

        # If the extension is in the value of the key
        if ext in files_type[folder]:
            #Check if the folder extension key exist, if not create it
            if not os.path.exists(f'{path}/{folder}'):
                os.makedirs(f'{path}/{folder}')

            # Move the file using full path to avoid duplicate file error
            shutil.move(os.path.join(path, file), os.path.join(f'{path}\{folder}', file))


## Calling the functions in a try & catch block and logging
## into file, if the script runs successfully or encounters an error
try:
    for file in os.listdir():
        move_file(file)

    logging.info('Script ran successfully') 


except Exception as e:
    logging.exception("Script encountered an error")
    raise e
