class Solution:
    def isPalindrome(self, s: str) -> bool:
        fil_s=''
        for c in s:
        #pre=processing step
            if c.isalnum(): 
                #lower case
                fil_s=c.lower() + fil_s
            else:
                continue
        rev_s = fil_s[::-1]
        return rev_s == fil_s
        