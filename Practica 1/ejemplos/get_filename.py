# Python Program to Get the File Name From the File Path
import os

# file name with extension
file_name = os.path.basename('./data_file.txt') #con el .txt

# file name without extension
print(os.path.splitext(file_name)[0]) #sin el .txt