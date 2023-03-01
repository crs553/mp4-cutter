import glob, os
from tkinter import filedialog as fd
from multiprocessing.pool import ThreadPool

def getFolder() -> str:
    """
    Opens file dialogue
    :return : file directory path as string
    """
    directory = fd.askdirectory(initialdir="~/")
    directory.replace(" ","\\ ")
    print(directory)
    return directory

def converter(file:str) -> str:
    """
    Conversion subroutine
    :param file: string
    :return: str containing name of successfully congerted file
    """
    cmd = get_command(file)
    try:
        run_command(cmd)
        os.system(f"rm {file}")
    except:
        raise SystemError("An error occured when converting file" + file)
    
    return file + " converted succesfully"
    
def get_command(file:str)->str:
    """
    Gets str for appropriate command for ffmpeg and auto editor given the file
    """
    return f"ffmpeg -i {file} -c:v libx264 {file}_edit.mp4 && auto-editor {file}_edit.mp4 --no-open"

def run_command(cmd:str):
    """
    Runs the string command
    """
    os.system(cmd)

def get_files(directory:str) -> list:
    """Returns a list of filenames given the directory path as a strings"""
    os.chdir(directory)
    files = glob.glob("*,mp4")

    if files is None or len(files) == 0:
        raise FileNotFoundError(f"No mp4 files in the directory {directory}")  
     
    print(f"Files:")
    for f in files:
        print(f)

    files = [f.replace(" ", "\\ ") for f in files]

    return files

def main():
    directory = getFolder()
    files = get_files(directory)
      
    if input("Do you want to convert these files [Y/n]") != "Y":
        return
   
    # threading over 4 processes
    with ThreadPool(processes=4) as pool:
        # call the function for each item concurrently, get results as tasks complete
        for result in pool.imap(converter, files):
            print(result)

if __name__ == "__main__":
    main()