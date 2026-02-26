from collections import Counter 
from typing import List
from textblob import TextBlob 
class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text 
        self.counter = Counter
        self.text_blob = TextBlob
        self.split_words = self.text.split() 

    def most_common_words(self) -> List[tuple[str, int]]:
        """find the most common words in the text"""
        count_words = self.counter(self.split_words)  # type: ignore
        return self.counter.most_common(count_words, 10)

    def find_weapens(self, weapon_file):
        """find weapon if they are in the text """
        weapon_list = []
        with open(weapon_file, 'r') as f:
            data = f.read() 
            for i in data.split():
                if i in self.text:
                    weapon_list.append(i)
        return weapon_list 
    
    def analyse_emotion_level(self):
        """find what emotion is in the text"""
        blob = self.text_blob(self.text)
        sentiments = blob.sentiment 
        return sentiments

    def analyse_text(self, weapon_file) -> dict:
        most_common = self.most_common_words()
        weapon_list = self.find_weapens(weapon_file)
        emotion_words = self.analyse_emotion_level()
        return self.to_dict(most_common, weapon_list, emotion_words)
    
    def to_dict(self, common, weapons, emotion):
        return {
            "most_common": common,
            "weapons": weapons,
            "emotion": emotion
        }

