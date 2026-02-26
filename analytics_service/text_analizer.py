from collections import Counter 
from typing import List

class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text 
        self.counter = Counter
        self.split_words = self.text.split()

    def count_words(self) -> List[tuple[str, int]]:
        count_words = self.counter(self.split_words)  # type: ignore
        return self.counter.most_common(count_words)


