class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        bucket=[[] for i in range(len(nums)+1)]

        for i, num in freq.items():
            bucket[num].append(i)
        
        res=[]

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res