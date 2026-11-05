class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0

        # 第一階段：尋找相遇點
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # 第二階段：尋找環入口
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow