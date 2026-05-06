#U:trying to see if series of brackets are closed properly
#P: make a dict that holds the opening:closing brackets for search. iterate thrught the string:
# if the val is an opening bracket push to the stack, if its a closer, check that the val at the top
# is the correspondinng opener
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {"(":")","{":"}","[":"]"}

        if len(s) == 1 or s[0] in pMap.values(): 
            return False

        for i in s:
            if i in pMap.keys(): 
                stack.append(i)
            elif i in pMap.values():
                if not stack:
                    return False
                comp = stack.pop()
                print(comp)
                if pMap[comp] != i:
                    return False
        if not stack:
            return True
        else:
            return False
            
