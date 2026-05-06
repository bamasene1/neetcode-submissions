class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = list(s)
        # print(string)
        left = 0
        right = len(s) - 1

        for i in string:
            # print(string[left])
            # print(string[right])
            if string[left].isalnum() and string[right].isalnum():
                if string[left] != string[right]:
                    return False
                else:
                    left += 1
                    right -=1
                    pass
            elif string[left].isalnum() == False:
                left +=1 
            elif string[right].isalnum() == False:
                right -=1 
            
                
        
        return True
            


        