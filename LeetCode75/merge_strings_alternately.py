class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        l = min(l1,l2)
        result=''
        for i in range(l):
            result=result+word1[i]+word2[i]
        if l1==l2:
            return result
        if l1>l2:
            return result+word1[l:l1]
        else:
            return result+word2[l:l2]
