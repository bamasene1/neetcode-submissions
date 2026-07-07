class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramsMap = {}

        sortedS = sorted(s)
        sortedT = sorted(t)

        if sortedS != sortedT:
            return False
        
        return True