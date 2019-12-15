import socket
import os

objective_sring = """
LiPy - Open Source Project.
Executes Unix/Linux Commands in any Operating System.

version: 0.1.1

(Enter "exit" to quit the command line)

Made with <3 by Hustlers!
"""

# Get the directory path where the file is stored
dir_path = os.path.dirname(os.path.realpath(__file__).replace("\\","/"))

# Get System Hostname
system_hostname = socket.gethostname()

command_line_shell = dir_path + "/"+ system_hostname + "$ "
print(objective_sring)

# Start receiving commands.
while True:
	command = raw_input(command_line_shell)
	
	# If user presses "Enter" key, then do not take any action, 
	# just print the command line once again.
	if command == "":
		continue

	# If the entered command is exit, then call the exit() method
	# and quit the program.
	if command == "exit":
		exit()

	try:
		# Each command is stored in a file whose name is that of the command itself.
		# e.g. if "ls" is the command we implement, then the code of that command will 
		# be "ls.py". When the user enters the command we try to import the respective
		# file, and if the import failed, that means the file/command does not exist
		# or has not yet been implemented.
		__import__(command)
	except NameError:
		print("Command not found!")
