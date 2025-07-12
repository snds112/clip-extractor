import os
import argparse
import pandas as pd

def get_video_files(directory_path):
    
    video_extensions = [
        '.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.mpg',
        '.m4v', '.3gp', '.3g2', '.f4v', '.vob', '.ogv', '.ogg', '.m2v', '.mts',
        '.m2ts', '.ts', '.qt', '.divx', '.rm', '.rmvb', '.asf', '.amv', '.nsv'
    ]
    
    file_list = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
       
        if os.path.splitext(entry)[1].lower() in video_extensions and os.path.isfile(full_path):
            file_list.append(entry)
    return file_list


def get_episodes():
    

    try:
        directory = '.' 
        files = get_video_files(directory)
        return sorted(files)
        

    except Exception as e:
            print(f"An error occurred: {e}")
            



