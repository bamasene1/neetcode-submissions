class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupes = {}

        for i,k in enumerate(nums):
            if k in dupes:
                return True
            else:
                dupes[k] = i

        return False