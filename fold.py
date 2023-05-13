"""
The mechanisam will basically be go to the file, open it, find the index of defination
statements like:
    def some_Text() # till the end of the line

then we find the index of the end, this can be done by looiking for another defination
statement and going back line by line till we find a line with text, this line will be the
end index of the prior defination statement. 

We then call vim to make the folds at the indexes an makeview to save the folds.

We do this for all the files given to the clam
"""
import subprocess

class Folder():

    def __init__(self, files: list[str]) -> None:
        self.files = files
        self.fold()

    def fold(self) -> None:
        """
        Find the start and end index of a funciton then call vim or nvim to add a fold to
        the file
        """
        for file in self.files:
            array = self.load_file(file)
            index_list = make_index_list(file)
            for range_ in index_list:
                vim_fold(range_, file_name)

    def load_file(self, file_name: str) -> list[str]:
        """
        Load all the files into an array and operate on that
        """
        pass

    def make_index_list(self, file_name: str):
        pass

    def find_function_index(self, start_index: int, file_name: str) -> list[int, int]:
        """
        We use python's indentation rule to determin when we are reading a function
        """
        pass

    def vim_fold(self, range: list[int, int], file_name: str) -> None:
        """
        command we are using:
            :{range}fo

        where range is rep as 3,10 (from line 3 to 10)
        """
        vim = 'vim '
        fold_range = f'-c {range[0]};{range[1]}fold '
        mkview = '-c "mkview" '
        
        command_str = vim + fold_range + mkview + file_name

        self.run(command_str)

    def run(self, args: str) -> None:
        subprocess.run(args)
        
