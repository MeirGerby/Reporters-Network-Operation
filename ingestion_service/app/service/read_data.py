from io import TextIOWrapper 

class ReadData:
    def __init__(self, path: TextIOWrapper):
        self.path = path 

    def read_images(self) -> 