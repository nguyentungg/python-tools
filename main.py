import fnmatch
import time
from tkinter import Tk, filedialog
import os
from moviepy.editor import VideoFileClip
import tkfilebrowser
import filetype


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
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# Read the file duration


def get_video_length(file):
    clip = VideoFileClip(file)
    duration = 0
    if file is not None:
        duration = round(clip.duration / 60, 2)
        clip.close()
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
            print(
                f'{bcolors.P}[WARNING] This file is a file: {section}{bcolors.W}')
            continue
        for filename in fnmatch.filter(os.listdir(section), "*.mp4"):
            video = os.path.join(section, filename)
            time = get_video_length(video)
            print(f'{video} => {bcolors.O}{time} minutes{bcolors.W}')
            all_time += time

    total_minutes = round(all_time, 1)
    total_hours = round(all_time/60, 1)
    total_days = round(total_hours/24, 1)
    total_working_days = round(total_hours/12, 1)
    print(f'{bcolors.P}Total minutes: {total_minutes} minutes{bcolors.W}')
    print(f'{bcolors.B}Total hours: {total_hours} hours{bcolors.W}')
    print(f'{bcolors.G}Total days (12): {total_working_days} days{bcolors.W}')
    print(f'{bcolors.R}Total days (24): {total_days} days{bcolors.W}')


# Select multiple folders at once
def multiple_selection_folders():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directories = tkfilebrowser.askopendirnames()
    all_time = 0
    video_count = 0
    # Initial call to print 0% progress
    directories_length = len(directories)
    printProgressBar(0, directories_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, select_dirs in enumerate(directories):
        if os.path.isfile(select_dirs):
            print(f'{bcolors.P}[WARNING] This file is a file: {select_dirs}{bcolors.W}')
            continue

        dir_lists = os.listdir(select_dirs)
        for dir_name in dir_lists:
            file_path = os.path.join(select_dirs, dir_name)
            if not os.path.isfile(file_path):
                # print(f'{bcolors.P}[WARNING] This not file is a file: {section}{bcolors.W}')
                continue

            if filetype.is_video(file_path):
                time = get_video_length(file_path)
                # print(f'{file_path} => {bcolors.O}{time} minutes{bcolors.W}')
                all_time += time
                video_count += 1
        # Update Progress Bar
        printProgressBar(i + 1, directories_length, prefix = 'Progress:', suffix = 'Complete', length = 50)

    total_minutes = round(all_time, 1)
    total_hours = round(all_time/60, 1)
    total_days = round(total_hours/24, 1)
    total_working_days = round(total_hours/12, 1)
    print('-----------RESULT------------')
    print(f'{bcolors.P}Total minutes: {total_minutes} minutes{bcolors.W}')
    print(f'{bcolors.B}Total hours: {total_hours} hours{bcolors.W}')
    print(f'{bcolors.G}Total days (12): {total_working_days} days{bcolors.W}')
    print(f'{bcolors.R}Total days (24): {total_days} days{bcolors.W}')
    print(f'{bcolors.O}Total videos: {video_count} videos{bcolors.W}')


multiple_selection_folders()
# select_sub_folder()
# select_folder()
