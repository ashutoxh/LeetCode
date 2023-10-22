class Solution:
    def twoSum(self, nums, target):
        diff = {}
        for i in range(len(nums)):
            if diff.get(nums[i]) is None:
                diff[target - nums[i]] = i
            else:
                return diff.get(nums[i]), i
        return -1, -1

        