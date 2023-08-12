class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h={}
        for i,c in enumerate(order):
            h[c]=chr(i+ord('a'))
        def convert(word):
            return ''.join(h[c] for c in word)
        last=''
        for word in words:
            converted_word=convert(word)
            if converted_word<last:
                return False
            last=converted_word
        return True

