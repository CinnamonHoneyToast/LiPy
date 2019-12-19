import os


class Lists():

    #get current working directory path
    def dir_path(self):
        self.dir_path = os.getcwd().replace("\\","/")

    def print_files(self):
        # Iterate through all the files in the directory and print the file names.
        for filename in os.listdir(self.dir_path):
            print(filename)

# create object
ls_ob = Lists()

# Call the function here, so that the code within the method is executed upon import.
ls_ob.dir_path()
ls_ob.print_files()
