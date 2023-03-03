from os import system,chdir


class Converter:
    def __init__(self, directory):
        chdir(directory)
        self.files = files
        self.filenames = [f.split(".")[0] for f in files]
        self.commands = [self.get_command(i) for i in range(files)]

    def run(self):
        pass

    def get_command(self, i):
        return f"ffmpeg -i {self.files[i]} -c:v libx264 {self.filenames[i]}_edit.mp4 && auto-editor {self.filenames[i]}_edit.mp4 --no-open"

    def _run_cmd(self, i):
        system(self.commands[i])

    def _converter(self, i):
        try:
            self._run_cmd(i)
        except:
            raise SystemError("An error occured when converting " + self.files[i])
