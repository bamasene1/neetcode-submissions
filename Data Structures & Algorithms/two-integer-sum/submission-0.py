class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevVal = {}

        for i,k in enumerate(nums):
            diff = target - k
            if diff in prevVal:
                return [prevVal[diff], i]
            else:
                prevVal[k] = i
        return None
        