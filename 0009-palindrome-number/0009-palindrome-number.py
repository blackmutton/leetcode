class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stack = []
        while x:
            stack.append(x%10)
            x //=10
        count = len(stack)
        right = count - 1
        left = 0
        while left<right:
            if stack[left] != stack[right]:
                return False
            left+=1
            right-=1
        
        return True