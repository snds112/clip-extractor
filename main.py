import argparse
import pandas as pd
import os
from folder_handler import get_episodes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze data from a specified file.")
    parser.add_argument("filepath", type=str, help="Path to the clips sheet.")
    
    args = parser.parse_args()
    
    if args.filepath.endswith('.csv'):
        clips_df = pd.read_csv(args.filepath)
    elif args.filepath.endswith(('.xlsx', '.xls')):
        clips_df = pd.read_excel(args.filepath)
    else:
        raise ValueError("Unsupported file format. Use .csv, .xlsx, or .xls")

    files=get_episodes()
    print(files)
   
    clips_dict= clips_df.to_dict("records")
    os.system("mkdir clips")
    os.chdir("clips")
    for clip in clips_dict:
        print(clip)
        extension = files[int(clip["episode"])-1].split('.')[-1]
        os.system("ffmpeg -n -ss "+ clip["start time"] +  " -to "+ clip["end time"] + " -i '../"+files[int(clip["episode"])-1] + "' -reset_timestamps 1 -map 0 -c copy -avoid_negative_ts 1 '"+ clip["name"]+"."+extension+"'")
        
        