import glob
import os
from tkinter import filedialog as fd
from multiprocessing.pool import ThreadPool
def getFolder() -> str:
    name = fd.askdirectory(initialdir="~/")
    return name

def main():
    directory = getFolder()
    os.chdir(directory)
    files =  glob.glob("*.mp4")
    files = [f.replace(" ", "\\ ") for f in files]
    
    print(files) 
    
    if input("Do you want to convert these files [Y/n]") != "Y":
        return
    
    with ThreadPool(processes=4) as pool:
        # call the function for each item concurrently, get results as tasks complete
        for result in pool.imap(converter, files):
            print(result)

def converter(file):
    cmd = get_command(file)
    try:
        run_command(cmd)
        os.system(f"rm {file}")
    except:
        print("An error occured for file " + file)
    
    return file + " converted succesfully"
    


def get_command(file)->str:
    return f"ffmpeg -i {file} -c:v libx264 {file}_edit.mp4 && auto-editor {file}_edit.mp4 --no-open"

def run_command(cmd)-> bool:
    os.system(cmd)
    

if __name__ == "__main__":
    main()