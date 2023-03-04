from os import system,chdir
from file_handler.file_handler import File_Handler
from multiprocessing.pool import ThreadPool

class Converter:
    def __init__(self, file_handler: File_Handler):
        self.file_handler = file_handler
        self.files = self.file_handler.files
        self.filenames = self.file_handler.filenames
        
        
    def run(self):
       with ThreadPool(processes=4) as pool:
        # call the function for each item concurrently, get results as tasks complete
        for result in pool.imap(self._converter, range(len(self.files))):
            print(result)

    def get_command(self,i):
        return f"ffmpeg -hide_banner -loglevel error -i {self.files[i]} -c:v libx264 {self.filenames[i]}_edit.mp4 && auto-editor {self.filenames[i]}_edit.mp4 --no-open --quiet"

    @staticmethod
    def _run_cmd(command:str):
        system(command)

    def _converter(self,i):
        try:
            print(f"Running conversion of file {self.filenames[i]}")
            self._run_cmd(self.get_command(i))
            system(f"rm {self.filenames[i]}_edit.mp4")
        except:
            raise SystemError("An error occured when converting file " + self.files[i])
    
        return self.files[i] + " converted succesfully"

        
