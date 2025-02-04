class Solution(object):
    def twoSum(self,nums:list[int],target:int )-> list[int]:
        prev = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prev:
                return [prev,i]
            prev[n] =i
nums = [2, 3, 5, 7, 1,8]
target = 11
sol = Solution()
result = sol.twoSum(nums, target)
print(result) 