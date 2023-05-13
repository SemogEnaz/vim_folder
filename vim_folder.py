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

class Folder():

    def __init(self, files: list[str]):
        
