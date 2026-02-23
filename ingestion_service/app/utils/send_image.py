import requests 

class SendImage:
    def __init__(self, image, url, image_name):
        self.image = image 
        self.url: str = url
        self.image_name: str = image_name
    
    def send_image(self):
        with open(self.image, 'rb') as f:
            response = requests.post(self.url, files=({"file": (self.image_name, f, 'image/png')}))
        return response 
    
# send = SendImage(r'ingestion_service\data\tweet_images\tweet_0.png', 'http://localhost:5000','tweet_0.png')
# image = r'ingestion_service\data\tweet_images\tweet_0.png'
# url = 'http://localhost:5000'
# content_type = 'image/png'
# packet = {'file': open(image, 'rb')}
# with open(image, 'rb') as f:
    # r = requests.post(url, files=({"file": (content_type, f, 'image/png')} ))
    # print(r.text)
# send.send_image()
