class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        total = 0
        for i in range(0,count):
            total+=nums[i]
        excepted = int((0+count)/2*(count+1))
        return excepted-total
