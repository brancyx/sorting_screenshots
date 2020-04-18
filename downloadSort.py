import os
import shutil

source_path = input("Source path: ")
dest_path = input("Destination path: ")
os.chdir(source_path) # Changes path to current working directory

for f in os.listdir(): # for every file in the current directory
    file_name, file_path = os.path.splitext(f) # Splits the ext name of file, returns a tuple
    first_word = file_name.split(' ')[0]
    if first_word == 'Screenshot' and file_path == '.png':
        shutil.move(source_path+'/'+f, dest_path+'/'+f)
    