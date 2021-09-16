import string
from collections import Counter


# BFS 

class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        puncs = string.punctuation
        for c in puncs:
            paragraph = paragraph.replace(c, ' ')
        
        words = paragraph.split()
        words_dic = Counter(words)
        words_dic = sorted(words_dic, key=lambda x:-(words_dic[x]))
        for word in words_dic:
            if not word in banned:
                return word
        return None
        