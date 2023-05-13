import sys
import subprocess

class Clam():

    def __init__(self):
        self.args = sys.argv[1:]
        if self.args == []:
            self.args = ["/home/zane/audio_vis/audio_vis_clam.py"]
        self.files = []
        self.py_ext = '.py'     # For python files
        self.wav_ext = '.wav'   # Wav audio files (just for testing)
        self.exe_cmd_args(self.args)

    def exe_cmd_args(self, args) -> None:
        self.get_files(args)

    def get_files(self, args) -> None:
        """
        We need to first filter out the paths to the files and add them to the file 
        list self.files.

        We then need to filter out directories and perform the add to file for each
        of the compatiable files in the directory
        """

        for arg in args:

            # This index math will prevent us from looking for substrings of the ext
            py_index = len(arg) - len(self.py_ext)

            # If file with the extension we want, add to file list
            if self.py_ext == arg[py_index:]:
                self.add_file(arg)

            # If the arg is a directory, get file names in dir and call recursively
            elif self.is_dir(arg):

                files = self.ls(arg)
                dir_char = ''

                if arg.rfind('/') > 1:
                    dir_char = '/'

                files = [arg + dir_char + file for file in files]
                self.get_files(files)

    def is_dir(self, path) -> bool:

        index_dir = path.rfind('/')
        index_ext = path.rfind('.')

        if index_dir > index_ext:
            return True

        return False

    def add_file(self, file) -> None:
            self.files.append(file)
                
    def ls(self, directory: str) -> list[str]:

        files = subprocess.run(["ls", directory], capture_output=True, text=True).stdout.split("\n")
        files = files[:-1]  # Last array item is ''

        return files

if __name__ == '__main__':

    # Finding path with the clam
    clam = Clam()
    print(clam.files)
