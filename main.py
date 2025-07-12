import argparse
import pandas as pd
import os
from folder_handler import get_episodes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze data from a specified file.")
    parser.add_argument("clips_csv_filepath", type=str, help="Path to the csv file.")
    
    args = parser.parse_args()
    
    try:
        clips_df= pd.read_csv(args.clips_csv_filepath)
        print(clips_df)
        files=get_episodes()
        print(files)
    except Exception as e:
        print(f"An error occurred: {e}")
        
    clips_dict= clips_df.to_dict("records")
    os.system("mkdir clips")
    os.chdir("clips")
    for clip in clips_dict:
        print(clip)
        extension = files[int(clip["episode"])-1].split('.')[-1]
        os.system("ffmpeg -n -ss "+ clip["start time"] +  " -to "+ clip["end time"] + " -i ../"+files[int(clip["episode"])-1] + " -reset_timestamps 1 -map 0 -c copy -avoid_negative_ts 1 "+ clip["name"]+"."+extension)
        
        