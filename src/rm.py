from __main__ import lipy

location = os.getcwd().replace("\\", "/") + "/" + lipy.get_argument()

class ReMove():

    def __init__(self,l):
        self.location=l

    def delete_file(self):
        import shutil
        # to delete a file
        if  os.path.isfile(self.location):
            os.remove(self.location)
            print("deletion successful")
            return
        # to delete a directory
        elif os.path.isdir(self.location):
            shutil.rmtree(self.location,ignore_errors=True)
            print("deletion successful")
            return
        else:
            raise FileNotFoundError


rm_ob=ReMove(location)

try:
    rm_ob.delete_file()
except FileNotFoundError:
    print("The given file/folder is not found")
except PermissionError:
    print("Delete Permission Denied")
except OSError:
    print("File cannot be deleted")

