class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base condition
        if len(s)!=len(t):
            return False
        alphabet= [0]*26
        for i in range(len(s)):
           idx_s = ord(s[i].lower()) - 97
           idx_t = ord(t[i].lower()) - 97
           alphabet[idx_s]+=1
           alphabet[idx_t]-=1
        for i in alphabet:
            if i !=0 :
                return False
            
        return True