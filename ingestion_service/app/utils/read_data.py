from os import listdir, fsdecode
from os.path import join
class ReadData:
    def __init__(self, path):
        self.path = path 
        self.path_list = []
        self.filename = []

    def read_images(self) -> list:
        for file in listdir(self.path):
            filename = fsdecode(file)
            self.filename.append(filename)
            self.path_list.append(join(self.path, file))
        return self.path_list

# from ..config import settings
# # path = "ingestion_service/data/tweet_images" 
# read_data = ReadData(settings.FOLDER_PATH)
# data = read_data.read_images()
# print(data)




