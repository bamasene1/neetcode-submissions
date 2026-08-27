#going to have a loop, fix a point and two pointer from the start and end to get the three sum
#logic: if the sum is smaller than 0, move the left pointer, if its bigger, move the right pointer 
#to skip over the anchor check if they are the same??

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []

        nums = sorted(nums)
        
        res = []


        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = nums[i] + nums[left]+ nums[right]
                if threeSum == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left +=1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return res




                    
