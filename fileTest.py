from fileModificationHandler import FileModified

def file_modified():
    print("File Modified!")
    return False
    

fileModifiedHandler = FileModified(r"logs7.txt",file_modified)
fileModifiedHandler.start()

