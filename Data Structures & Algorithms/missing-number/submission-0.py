class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualSum=0
        l=len(nums)
        expectedSum=l*(l+1)//2
        for i in nums:
            actualSum+=i
        return expectedSum-actualSum