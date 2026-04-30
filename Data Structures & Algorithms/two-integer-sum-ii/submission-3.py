#U: two sum but with a sortted array 
#P:Need two pointers on each end. if the sum > target move the right one down, else left up
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left<right:
            if numbers[left] + numbers[right] == target:
                return [left +1, right +1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1 

        return None

        
