"""
The mechanisam will basically be go to the file, open it, find the index of defination
statements like:
    \def\ some_Text() # till the end of the line

then we find the index of the end, this can be done by looiking for another defination
statement and going back line by line till we find a line with text, this line will be the
end index of the prior defination statement. 

We then call vim to make the folds at the indexes an makeview to save the folds.

We do this for all the files given to the clam
"""
import subprocess

class Folder():
    # TODO: Need to run the vim folder at 10 commands per subprocess call
    # TODO: Run the folding  in a different subprocess and output to user when process ends

    def __init__(self, files: list[str]) -> None:
        self.files = files
        self.first_fold = True
        self.fold()

    def fold(self) -> None:
        """
        Find the start and end index of a funciton then call vim or nvim to add a fold to
        the file
        """
        for file in self.files:

            self.clear_folds(file)

            array = self.load_file(file)
            index_list = self.make_index_list(array)

            self.first_fold = True

            for range_ in index_list:

                print('\t' , range_)
                self.vim_fold(range_, file)

                if self.first_fold:
                    self.first_fold = False

    def load_file(self, file_name: str) -> list[str]:
        """
        Load all the files into an array and operate on that
        """
        print("Loading file as array of lines for " + file_name)
        line_array = []
        with open(file_name, 'r') as file:
            line_array.append(file.readlines()) # read lines & remove trailing '\n'

        return line_array[0]

    def make_index_list(self, line_array: list[str]):
        print("Making index list")
        start = 0
        end = 0

        index_list = []
        indent_count = 0

        search_for_start = True
        
        for line_count, line in enumerate(line_array):
            """
            Using pythons indentation rule to get the range lines the mehtod covers
            """
            is_lower_indent = self.get_indent_count(line) <= indent_count
            is_not_empty_line = len(line) > 2
            is_not_start = start < line_count

            is_end_function = is_lower_indent 
            is_end_function &= is_not_empty_line 
            is_end_function &= is_not_start

            if is_end_function and start != 0 and start != end:
                end = line_count - 1
                index_list.append([start, end])
                search_for_start = True

            if line.find('def ') != -1 and search_for_start:
                start = line_count + 1
                indent_count = self.get_indent_count(line)
                search_for_start = False

        return index_list

    def get_indent_count(self, line: str) -> int:
        count = 0

        for char in line:
            if char == ' ':
                count += 1
            else:
                return count

    def clear_folds(self, file_name: str) -> None:
         
        vim = 'vim '
        mkview = '-c "mkview" '
        quit_ = '-c "q" '

        cmd_str = vim + mkview + quit_ + file_name

        self.run(cmd_str)

    def vim_fold(self, range: list[int, int], file_name: str) -> None:
        """
        command we are using:
            :{range}fo

        where range is rep as 3,10 (from line 3 to 10)
        """

        vim = 'vim '
        loadview = '-c loadview '
        fold_range = f'-c "{range[0]};{range[1]}fold" '
        mkview = '-c "mkview" '
        quit_ = '-c "q" '
        
        cmd_str = vim + loadview + fold_range + mkview + quit_ + file_name

        self.run(cmd_str)

    def run(self, args: str) -> None:
        subprocess.run(args, shell=True)
        
