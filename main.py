from converter.converter import Converter
from file_handler.file_handler import File_Handler, ask_directory_gui


class Cutter():
    def __init__(self, gui:bool = True):
        file_path = None
        if gui:
            file_path = ask_directory_gui()
        if file_path is None or len(file_path) == 0 :
            raise NotADirectoryError(f"{file_path} is not a valid directory")
        file_path = file_path.replace(" ", "\\ ")
        self.file_handler = File_Handler(file_path)
        print(self.file_handler)
        self.converter = Converter(file_handler=self.file_handler)

    def run(self):
        self.converter.run()

def run_cutter():
    cutter = Cutter()
    if input("Do you want to run on these files [Y/n]") != "Y":
        return
    cutter.run()

if __name__=="__main__":
    run_cutter()
