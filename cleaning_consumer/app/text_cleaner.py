from cleantext import clean 


class TextCleaner: 
    """cleaning text """
    def __init__(self, text): 
        self.text = text 

    def clean_text_pucnt(self):
        """clean text punctuation"""
        return clean(text=self.text, no_punct=True)
        

