class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "Was it a car or a cat I saw?"
        p_s=''

        def is_alnum(c):
            '''return true if is_alnum'''
            if (
                ('0' <= c <= '9') or 
                ('a' <= c <= 'z' ) or 
                ('A' <= c <= 'Z' )):
                return True
            else:
                return False


        for char in s:
            #skip non-alpha
            if not is_alnum(char): continue
            pchar=char.lower()
            p_s=p_s+pchar

        # p_s='wasitacaroracatisaw'

        #debug
        print(f'processed string is {p_s}')
        print(f'reversed processed string is {p_s[::-1]}')        

        #is reverse the same?
        if p_s == p_s[::-1]: return True
        else: return False