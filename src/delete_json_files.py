import glob, os, os.path

#delete all created json files in this directory
filelist = glob.glob(os.path.join('../src/', "*.json"))
for f in filelist:
    os.remove(f)