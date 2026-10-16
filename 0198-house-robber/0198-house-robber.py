class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        prev_rob = nums[0]
        max_rob = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            max_rob,prev_rob= max(prev_rob + nums[i], max_rob),max_rob

        return max_rob