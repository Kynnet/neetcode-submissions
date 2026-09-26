class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverses = {}
        for i in range(len(nums)):
            if inverses.get(nums[i]) != None:
                return [inverses.get(nums[i]), i]
            else:
                inverses[target-nums[i]] = i
        