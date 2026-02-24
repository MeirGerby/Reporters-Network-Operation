import requests 
from pathlib import Path

class SendImage:
    def __init__(self, image, url, image_name):
        self.image: Path  = Path(image) 
        self.url: str = url
        self.image_name: str = image_name
        self.valid_extention = ('.jpg', '.png', '.jpeg')
    
    def validation_if_image(self) -> bool:
        return self.image.is_file() and self.image.suffix.lower() in self.valid_extention

    def send_image(self):
        if not self.validation_if_image():
            return f"the file is not validate {self.image}"
        
        with open(str(self.image), 'rb') as f:
            files=({"file": (self.image_name, f, 'image/png')})
            response = requests.post(self.url, files=files)
        return response.text 
    
    
# send = SendImage(r'ingestion_service\data\tweet_images\tweet_0.png', 'http://localhost:5000','tweet_0.png')
# image = r'ingestion_service\data\tweet_images\tweet_0.png'
# url = 'http://localhost:5000'
# content_type = 'image/png'
# packet = {'file': open(image, 'rb')}
# with open(image, 'rb') as f:
    # r = requests.post(url, files=({"file": (content_type, f, 'image/png')} ))
    # print(r.text)
# send.send_image()
