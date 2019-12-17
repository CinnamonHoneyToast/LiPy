import os
from __main__ import lipy


class cd():

    # change the directory
    def change_dir(self):
        os.chdir(lipy.get_argument())

    # get current working directory
    def get_cwd(self):
        self.dir_pat = os.getcwd().replace("\\", "/")

    # update command line shell
    def shell_update(self):
        lipy.command_line_shell = self.dir_pat + "/" + "$ "


# create object
cd_ob = cd()

try:
    cd_ob.change_dir()
    cd_ob.get_cwd()
    cd_ob.shell_update()
    
except FileNotFoundError:
    print("Path not defined!")

except NotADirectoryError:
    print("The directory name is invalid")
    

    

