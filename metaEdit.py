import os
import sys

def listFiles(dir, files):
    temp = os.listdir(dir)
    for t in temp:
        files.append(dir+"/"+t)
        if os.path.isdir(dir+"/"+t):
            files = listFiles(dir+"/"+t, files)

    return files

if len(sys.argv)<=1:
    print("Usage: python3 metaEdit.py [file] [options]")
    print("""
positional arguments:
  file                  the file to process

optional arguments:
  -h, --help            show this help message and exit
  -s, --show            show metadata withought running editor

    """)
    quit()

show = False;
filename = sys.argv[1]
if len(sys.argv)>2 and (sys.argv[2] == "--show" or sys.argv[2] == "-s"):
    show = True;
else:
    show = False


os.system("cp "+filename+" /tmp/"+filename.split("/")[-1:][0]+".zip")
try:
    os.mkdir("/tmp/metaEdit")
except:
    print("Tmp dir already exists.")
    os.system("rm -rf /tmp/metaEdit/*")

os.system("unzip /tmp/"+filename.split("/")[-1:][0]+".zip -d /tmp/metaEdit/")

f = []
path ="/tmp/metaEdit"
files = listFiles(path, [])
print()
print("Metadata files found:")
print("---------------------------")
for f in files:
    if f.endswith(".xml"):
        print(f)
print("---------------------------")
