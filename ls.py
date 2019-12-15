import os
import time

def ls():
    # Get current directory
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Iterate through all the files in the directory and print the file names.
    for filename in os.listdir(dir_path):
        print(filename)

# Call the function here, so that the code within the method is executed upon import.
ls()
