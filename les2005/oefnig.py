import os 
def fldrSize(dir):
    size = 0
    for item in os.listdir(dir):
        fileFldr = os.path.join(dir, item)
        if os.path.isfile(fileFldr):
            size= size +os.path.getsize(fileFldr)
    return size

print(fldrSize('c:\\'))