class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            freq={}
            for i in s:
                if i not in freq:
                    freq[i]=1
                else:
                    freq[i]+=1

            for i in t:
                if i not in freq:
                    return False
                else:
                    if freq[i]>0:
                        freq[i]-=1
                    else:
                        return False
            return True