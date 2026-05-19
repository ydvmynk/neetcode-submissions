class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        i=1
        while i<3:
            for num in nums:
                ans.append(num)
            i+=1
        return ans