# script written by Shadowdara

# SCRIPTS ARE ONLY FOR IMPORTING!!!

import os
import configparser

def delete_files(path, ini_info2):
    try:
        file_info = configparser.ConfigParser(allow_no_value=True)
        file_info.read(os.path.join(path, ini_info2), encoding = 'UTF-8')
        
        if "auto_generated_files" in file_info:
            for item in file_info.options("auto_generated_files"):
                os.remove(os.path.join(path, item))
                print(f'Deleted: {item}')

    except:
        print('Error: No write Access')
