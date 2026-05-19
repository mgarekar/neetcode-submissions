class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "Was it a car or a cat I saw?"
        p_s=''

        for char in s:
            #skip non-alpha
            if not char.isalnum(): continue
            pchar=char.lower()
            p_s=p_s+pchar

        # p_s='wasitacaroracatisaw'

        #debug
        print(f'processed string is {p_s}')
        print(f'reversed processed string is {p_s[::-1]}')        

        #is reverse the same?
        if p_s == p_s[::-1]: return True
        else: return False