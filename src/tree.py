  
import os
import sys
class Tree:
    def __init__(self):
        self.dir_count = 0
        self.file_count = 0

    def register(self, absolute):
        if os.path.isdir(absolute):
            self.dir_count += 1
        else:
            self.file_count += 1
    def summary(self):
        return str(self.dir_count) + " directories, " + str(self.file_count) + " files"

    def walk(self, directory, prefix = ""):
        filepaths = sorted([filepath for filepath in os.listdir(directory)])

        for index in range(len(filepaths)):
            if filepaths[index][0] == ".":
                continue
            absolute = os.path.join(directory, filepaths[index])
            self.register(absolute)

            if index == len(filepaths) - 1:
                print(prefix + "└── " + filepaths[index])
                if os.path.isdir(absolute):
                    self.walk(absolute, prefix + "    ")
            else:
                print(prefix + "├── " + filepaths[index])
                if os.path.isdir(absolute):
                    self.walk(absolute, prefix + "│   "
directory = "."
if len(sys.argv) > 1:
    directory = sys.argv[1]
print(directory)

tree = Tree()
tree.walk(directory)
print("\n" + tree.summary())
