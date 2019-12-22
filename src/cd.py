import os
from __main__ import lipy


class ChangeDirectory():

    # change the directory
    def change_dir(self):
        if(lipy.get_argument()!=None):
            os.chdir(lipy.get_argument())
        else:
            os.chdir(lipy.dir_path)

    # get current working directory
    def get_cwd(self):
        self.dir_pat = os.getcwd().replace("\\", "/")

    # update command line shell
    def shell_update(self):
        lipy.command_line_shell = self.dir_pat + "/" + lipy.system_hostname + "$ "


#Ccreate object
cd_ob = ChangeDirectory()


try:
    cd_ob.change_dir()
    cd_ob.get_cwd()
    cd_ob.shell_update()
        
except FileNotFoundError:
     print("Path not defined!")

except NotADirectoryError:
     print("The directory name is invalid")


    
    

