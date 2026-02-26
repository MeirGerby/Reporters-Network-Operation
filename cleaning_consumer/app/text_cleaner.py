from cleantext import clean 


class TextCleaner: 
    """cleaning text """
    def __init__(self, text): 
        self.text = text 
        self.clean_d = None

    def clean_text_pucnt(self):
        """clean text punctuation"""
        self.clean_d = clean(text=self.text, no_punct=True)
        return self.clean_d 

