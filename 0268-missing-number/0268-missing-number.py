class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        total = 0
        for i in range(0,count):
            total+=nums[i]
        excepted = (count+1)*count//2
        return excepted-total
