#needs to be o(n)
#U: given an unsortedd array, give the longest consequetive sequence of elements that can be made
#P: map every integer to a set so that they are sorted, if the previous value of the current isnt in the set then its a new sequence.
# while we still have a value that comes next in the set then we add to the length.
#before clearing the answer sequence, check the len of the subarray and the max len

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        values = set(nums)

        for i in values:
            print(i)
            if i - 1 not in values:
                length = 1
                while i + length in values:
                    length +=1
                res = max(res, length)
        
        return res

        #while solved == false:

        
