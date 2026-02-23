from easyocr import Reader

class ImageOcr:
    def __init__(self, path):
        self.reader = Reader(['en'], gpu=False)
        self.path = path
        self.result = []
        self.coord = None 
        self.text = None 
        self.conf = None 

    def read_text_from_image(self) -> list: 
        _text = self.reader.readtext(self.path)
        self.result.append(_text)
        for res in _text:
            self.coord = res[0]     # type: ignore
            self.text = res[1]      # type: ignore
            self.conf = res[2]       # type: ignore
            print(self.text)
            # print(self.coord)
            # print(self.conf) 
        return self.result 
    
    def get_text(self):
        if self.text is None:
            raise ValueError('the text attribute is none, make sure the file is image with text inside')
        return self.text

    def get_coord(self):
        if self.coord is None:
            raise ValueError('the coord attribute is none, make sure the file is image with text inside')
        return self.coord
        
    def get_conf(self):
        if self.conf is None:
            raise ValueError('the conf attribute is none, make sure the file is image with text inside')
        return self.conf
        
    

# image = ImageOcr('ingestion_service/data/tweet_images\\tweet_6681.png')
# image.read_text_from_image()
# print(image.text)