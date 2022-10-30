import fnmatch
import glob
from tkinter import Tk, filedialog
import os
from moviepy.editor import VideoFileClip

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    W  = '\033[0m'  # white (normal)
    R  = '\033[31m' # red
    G  = '\033[32m' # green
    O  = '\033[33m' # orange
    B  = '\033[34m' # blue
    P  = '\033[35m' # purple


# Read the file duration
def get_video_length(file):
    clip = VideoFileClip(file)
    duration = 0
    if file is not None:
        duration = round(clip.duration / 60, 2)
    return duration


# Find from a folder by select dialog
def select_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = filedialog.askdirectory()
    all_time = 0
    for filename in fnmatch.filter(os.listdir(directory), "*.mp4"):
        video = os.path.join(directory, filename)
        time = get_video_length(video)
        print(f'{video} => {time} minutes')
        all_time += time

    print(f'Total time: {round(all_time, 1)}')
    print(f'Total day(24): {round(all_time/24, 1)}')

# Find from sub folder by select in dialog
def select_sub_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = filedialog.askdirectory()
    all_time = 0
    course = os.listdir(directory)
    for dir_name in course:
        section = os.path.join(directory, dir_name)
        if os.path.isfile(section):
            print(f'{bcolors.P}[WARNING] This file is a file: {section}{bcolors.W}')
            continue
        for filename in fnmatch.filter(os.listdir(section), "*.mp4"):
            video = os.path.join(section, filename)
            time = get_video_length(video)
            print(f'{video} => {bcolors.O}{time} minutes{bcolors.W}')
            all_time += time

    print(f'Total time: {round(all_time, 1)}')
    print(f'Total day(24): {round(all_time/24, 1)}')


select_sub_folder()
# select_folder()
