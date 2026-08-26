#U:returning the top k most frequent elements from a list
#P: O(n) time means we can parse for a map to access, then map the counts of value to the index of a new array
# make a dict
#loop over the list, for each element, add to the map, if the element is there add to its count, if not +1
#then for i in range k get the top two

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        freq = [[]for i in range(len(nums) + 1)]

        #count frequencies 
        for i in nums:
            if i not in frequencyMap:
                frequencyMap[i] = 1
            else:
                frequencyMap[i] += 1

        #map freqs to index and number to the list 
        for i, c in frequencyMap.items():
            freq[c].append(i)

        #pull the top k
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
