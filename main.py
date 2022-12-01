import os

subfolders = [f.path for f in os.scandir(".") if f.is_dir()]

for e in subfolders:
    if str(e).startswith("./Tag"):
        os.system("python \""+e+"/"+e[2:].replace(" ","").lower()+".py\"")