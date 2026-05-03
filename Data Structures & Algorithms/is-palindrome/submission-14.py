class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "Was it a car or a cat I saw?"
        sp=''
        for char in s:
            if char.isalnum(): sp = sp + char.lower()
            else: continue
        print(sp)            
        for i in range( 0,len(sp)//2 ):
            j = len(sp)-i-1
            print(i)
            print(sp[i])
            print(j)  
            print(sp[j])                      
            if sp[i] == sp[j]: continue
            else: return False

        return True




















































































    #     # Input: s = "Was it a car or a cat I saw?"
    #     l,r = 0, len(s) - 1
    #     while( l < r ):
    #         #skip chars
    #         while l < r and not self.isalnumc(s[l]):
    #             l = l+1
    #         while l < r and not self.isalnumc(s[r]):
    #             r = r-1
    #         #main logic
    #         if (s[l].lower() != s[r].lower()):
    #             return False
    #         l=l+1
    #         r=r-1      
    #     return True  

    # def isalnumc(self,s):
    #     ''' return true if alnum , false if not'''
    #     return s.isalnum()































    # def isPalindrome(self, s: str) -> bool:
    #     fil_s=''
    #     for c in s:
    #     #pre=processing step
    #         if c.isalnum(): 
    #             #lower case
    #             fil_s=c.lower() + fil_s
    #         else:
    #             continue
    #     rev_s = fil_s[::-1]
    #     return rev_s == fil_s
        