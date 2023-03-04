import glob
from os import chdir
from tkinter import filedialog as fd


class File_Handler:
    def __init__(self, directory="~/"):
        chdir(directory)

        self.files = glob.glob("*.mp4")
        
        self.filenames = [file.split(".")[0] for file in self.files]
        self.pretty_print = "Files:"
        for f in self.filenames:
            self.pretty_print += f"\n{f}"
        
        self.files = [f.replace(" ", "\\ ") for f in self.files]
        self.filenames = [file.split(".")[0] for file in self.files]



    def get_files(self):
        return self.files


    def get_filenames(self):
        return self.filenames

    def __str__(self):
        return self.pretty_print

    def __len__(self):
        if self.files is None:
            return 0
        return len(self.files)

    def __getitem__(self, item: int):
        files = self.get_files()
        return files[item]

def ask_directory_gui():
    return fd.askdirectory(initialdir="~/")

def ask_directory_cmd():
    return input("Please enter the path to the directory with your files in:\n")

