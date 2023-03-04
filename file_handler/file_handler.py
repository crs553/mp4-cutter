import glob
from os import chdir


class File_Handler:
    def __init__(self, directory="~/"):
        self.change_directory(directory)
        self.files = None
        self.filenames = None

    def refresh_files(self):
        self.files = glob.glob("*.mp4")

    def get_files(self):
        return [f.replace(" ", "\\") for f in self.files]

    def refresh_filenames(self):
        self.filenames = [file.split(".")[0] for file in self.files]

    def get_filenames(self):
        return self.filenames

    @staticmethod
    def change_directory(directory):
        chdir(directory)

    def __str__(self):
        self.refresh_filenames()
        val = "Files:"
        for f in self.filenames:
            f"\n{f}"
        return val

    def __len__(self):
        self.refresh_files()
        if self.files is None:
            return 0
        return len(self.files)
