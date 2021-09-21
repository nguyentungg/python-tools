import fnmatch
import glob
from tkinter import Tk, filedialog
import os
from moviepy.editor import VideoFileClip


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

    print(f'Total time: {round(all_time, 2)}')
    print(f'Total day(24): {round(all_time/24, 2)}')

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
            print(f'[WARNING] This file is a file: {section}')
            continue
        for filename in fnmatch.filter(os.listdir(section), "*.mp4"):
            video = os.path.join(section, filename)
            time = get_video_length(video)
            print(f'{video} => {time} minutes')
            all_time += time

    print(f'Total time: {round(all_time, 2)}')
    print(f'Total day(24): {round(all_time/24, 2)}')


select_sub_folder()
# select_folder()
