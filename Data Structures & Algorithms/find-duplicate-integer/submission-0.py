#brute force

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupes = {}

        for i in nums:
            if i in dupes:
                return i
            else:
                dupes[i] = 1

        return None