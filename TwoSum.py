class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if target == (nums[i]+j):
                    return[nums.index(nums[i]),i+1+nums[nums.index(nums[i])+1:].index(j)]