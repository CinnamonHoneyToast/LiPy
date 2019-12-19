import socket
import os


objective_string = """
LiPy - Open Source Project.
Executes Unix/Linux Commands in any Operating System.

version: 0.1.1

(Enter "exit" to quit the command line)

Made with <3 by Hustlers!
"""

class LiPy():

        def __init__(self, ob_string):
                self.objective_string = ob_string

        def shell(self):
                # Get the directory path where the file is stored
                self.dir_path = os.path.dirname(os.path.realpath(__file__).replace("\\","/"))

                # Get System Hostname
                self.system_hostname = socket.gethostname()

                self.command_line_shell = self.dir_path + "/" + self.system_hostname + "$ "
                print(self.objective_string)

        def run_commands(self):
                while(1):
                        self.command_arguments = input(self.command_line_shell)

                        # If user presses "Enter" key, then do not take any action, 
                        # just print the command line once again.
                        if self.command_arguments == "":
                                continue

                        # If the entered command is exit, then call the exit() method
                        # and quit the program.
                        if self.command_arguments == "exit":
                                exit()

                        try:
                                # Each command is stored in a file whose name is that of the command itself.
                                # e.g. if "ls" is the command we implement, then the code of that command will 
                                # be "ls.py". When the user enters the command we try to import the respective
                                # file, and if the import failed, that means the file/command does not exist
                                # or has not yet been implemented.
                                file = self.dir_path + '/' + self.get_command()+'.py'
                                exec(open(file).read())

                        except NameError:
                                 print("Command not found!")
                        except ModuleNotFoundError:
                                print("Command not found!")

        #function to get command
        def get_command(self):
                self.command = self.command_arguments.split()[0]
                return self.command

        #function to get argument
        def get_argument(self):
                try:
                        self.argument = self.command_arguments.split()[1]
                        return self.argument
                except:
                        return None


#create lp object
lipy = LiPy(objective_string)

if __name__ == "__main__":
        

        #get directory path and system host name
        lipy.shell()

        # Start receiving commands.
        lipy.run_commands()

        

        
      


        
