class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        
        while word1 and word2:
            new_string+=word1[0]+word2[0]
            word1=word1[1:]
            word2=word2[1:]

        rest_str = word1 if len(word1)>len(word2) else word2
        return new_string+rest_str