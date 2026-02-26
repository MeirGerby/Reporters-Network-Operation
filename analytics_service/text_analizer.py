from collections import Counter 
from typing import List

class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text 
        self.counter = Counter
        self.split_words = self.text.split() 

    def count_words(self) -> List[tuple[str, int]]:
        """find the most common words in the text"""
        count_words = self.counter(self.split_words)  # type: ignore
        return self.counter.most_common(count_words)

    def find_weapens(self, weapon_file):
        """find weapon if they are in the text """
        weapon_list = []
        with open(weapon_file, 'r') as f:
            data = f.read() 
            for i in data.split():
                if i in self.text:
                    weapon_list.append(i)
        return weapon_list 

