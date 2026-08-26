#two passes on the input: first find all prefixes and store them in the output,
#Second, from the end computee the postfixes, but as you do it, use the postfix to 
#multiply by the prefix to get the product for each element andd store it in place

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *(len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # reverse order 
            res[i] *= postfix
            postfix *= nums[i]

        return res 