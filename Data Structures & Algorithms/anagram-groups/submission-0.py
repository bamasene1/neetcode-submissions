#U: need to group anagrams that are in a list
#P: make a dict for the strings, for each string:
    #sort the word and add the word into the map 
    #Make the key the full word(unsorted)
#I:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringsMap = {}
        
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in stringsMap:
                stringsMap[sortedWord].append(word)
            else:
                stringsMap[sortedWord] = [word]

        return list(stringsMap.values())

        