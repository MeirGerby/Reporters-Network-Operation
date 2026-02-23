from utils.send_image import SendImage
from config import settings
from pathlib import Path

class MongoLoaderClient:
    def __init__(self, image: str, url=settings.MONGO_LOADER_URL):
        self.image: Path = Path(image)
        self.image_name = self.image.stem
        self.send = SendImage(self.image, url, self.image_name)

    def send_to_mongo_loader(self):
        return self.send.send_image()
