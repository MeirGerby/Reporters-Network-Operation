from easyocr import Reader

class BaseOCR:
    def __init__(self, path):
        self.reader = Reader(['en'], gpu=False)
        self.path = str(path)
        self.coord = None 
        self.text = None 
        self.conf = None 


class OCREngine(BaseOCR):
    def __init__(self, path):
        super().__init__(path)
        self.result = []

    def read_text_from_image(self) -> list: 
        _text = self.reader.readtext(self.path)
        self.result.append(_text)
        
        if _text:
            self.coord = _text[0][0]     # type: ignore
            self.conf = _text[0][2]       # type: ignore
            self.text = " ".join([res[1] for res in _text])     # type: ignore

        return self.result 

class MetadataExtractor(OCREngine):
    def get_text(self):
        if self.text is None:
            # raise ValueError('the text attribute is none, make sure the file is image with text inside')
            return ""
        return self.text

    def get_coord(self):
        if self.coord is None:
            raise ValueError('the coord attribute is none, make sure the file is image with text inside')
        return self.coord

    def get_conf(self):
        if self.conf is None:
            raise ValueError('the conf attribute is none, make sure the file is image with text inside')
        return self.conf
        
    

# image = MetadataExtractor('ingestion_service/data/tweet_images\\tweet_6681.png')
# image.read_text_from_image()
# print(image.text)