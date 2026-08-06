# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        def build(left, right):
            if left > right:
                return None

            mid = (left+right)//2
            root = TreeNode(val=nums[mid],left=None,right=None)
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)

            return root
        
        return build(left, right)