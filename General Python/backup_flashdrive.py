#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     25/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import shutil,os,time

current_date = time.strftime("%m_%d_%Y")
flashdrive_drive = input('What is the current drive that the flash drive is plugged into? (ex. E, G)')
files_to_copy = [r":\Research\Research.py",":\Research\Track Time.xlsx",r":\MUST\mizzou unmanned systems team notes.txt",
                 r":\Resume\Brandon Resume.doc",r":\Capstone\notes.txt"]

dst = r"C:\Users\James\Python\General Python\flashbackup_" + current_date

# Make the directory that will have the files copied into it.
if not os.path.exists(dst):
    os.mkdir(dst)

# Add the drive that the flash drive is plugged into and copy the given files
for i in files_to_copy:
    shutil.copy(flashdrive_drive + i,dst)