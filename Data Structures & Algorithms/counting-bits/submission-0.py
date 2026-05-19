class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            num=i
            count=0

            while num!=0:
                count+=num&1
                num>>=1
            res.append(count)
            
        return res