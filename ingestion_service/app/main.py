from config import settings 
from service.mongo_loader import MongoLoaderClient 
from utils.read_data import ReadData


class Main:
    def __init__(self):
        self.data = ReadData(settings.FOLDER_PATH)
        self.path_list = self.data.read_images()

    def main(self):
        for img in self.path_list:
            try:
                mongo_loader = MongoLoaderClient(img)
                respone = mongo_loader.send_to_mongo_loader() 
                print(respone)
            except ValueError as e:
                print(e, img)
    
if __name__ == '__main__':
    main = Main.main()