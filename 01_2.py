class Solution(object):
    def twoSum(self, nums, target):
        prev = {}
        for index, i in enumerate(nums):
            diff = target - i
            if diff in prev:
                return [prev[diff], index]
            prev[i] = index
        
        return "There are no numbers whose sum equals the target"

nums = [2, 3, 5, 7, 1]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print(result) 
