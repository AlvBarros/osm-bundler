import os
import sys

args=sys.argv
directory=args[1]
protocpath=args[2]

for file in os.listdir(directory):
    if file.endswith(".proto"):
        print(protocpath+" "+directory+"/"+file+" --python_out=.")
        os.system(protocpath+" "+directory+"/"+file+" --python_out=. --proto_path="+directory)