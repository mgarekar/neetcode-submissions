class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, target_hm = {}, {}
        l,r=0,0

        res=float("infinity")
        resL=[-1,-1]

        #init
        for c in t: target_hm[c] = target_hm.get(c,0)+1
        
        def compare_hm(window, target_hm):
            for key in target_hm:
                if window.get(key, 0) < target_hm[key]:
                    return False
            return True


        
        for r in range(len(s)):
            c=s[r]
            window[c] = window.get(c,0)+1

            while( compare_hm(window, target_hm) ):#condition is valid
                #valid substring

                #calculate minimum
                if (r - l + 1) < res:
                    res = r - l + 1
                    resL = [l, r]


                #shrink 
                lchar=s[l]
                window[lchar] = window.get(lchar) -1
                if window[lchar] == 0:
                    del window[lchar]
                l=l+1

            #not a valid substring
        if res == float("infinity"):
            return ''
        else:
            return s[resL[0]:resL[1]+1]


































































        # l,r=0,0
        # minl=float('infinity')
        # hm_s={}
        # hm_t={}

        # def comapre_hm(hm_s, hm_t):
        #     #return true or false
        #     matches =  30
            
        #     for key in hm_t:
        #         if hm_t[key]==hm_s.get(key,0): 
        #             matches = matches + 1
            
        #     if matches == len(hm_t): 
        #         return True 
        #     else:
        #         return False
                
            
        
        # #init
        # for i in range(len(t)):
        #     char_s=s[i]
        #     char_t=t[i]
        #     hm_s[char_s] = hm_s.get(char_s,0)+1
        #     hm_t[char_t] = hm_t.get(char_t,0)+1            


        # for r in range(len(t),len(s)):
        #     rchar=s[r]
            
        #     while comapre_hm(hm_s,hm_t):
        #         #invalid subs
        #         lchar = s[l]
        #         #delete hm
        #         hm_s[lchar] = hm_s[lchar] -1 
        #         if hm_s[lchar] == 0: del hm_s[lchar]
        #         l=l+1

        #     #valid sub-string
        #     length = r-l+1
        #     min_length = min(length,minl)
            
        # value = s[l:l+min_length]
        # return value


            






























        # left, right = 0, 0
        # window_counts = {}  # Counts of characters in the current window
        # target_counts = {}  # Counts of characters needed from t
        
        # # Initialize the target character counts
        # for char in t:
        #     target_counts[char] = target_counts.get(char, 0) + 1
        
        # formed, required = 0, len(target_counts)
        # result = [-1, -1]
        # min_length = float('infinity')

        # for right in range(len(s)):
        #     char = s[right]
        #     window_counts[char] = window_counts.get(char, 0) + 1  # Add characters to the window

        #     if char in target_counts and window_counts[char] == target_counts[char]:
        #         formed += 1

        #     while formed == required:  # Valid substring found
        #         # Update result if this window is smaller
        #         window_length = right - left + 1
        #         if window_length < min_length:
        #             result = [left, right]
        #             min_length = window_length

        #         # Shrink window from the left
        #         window_counts[s[left]] -= 1

        #         if s[left] in target_counts and window_counts.get(s[left]) < target_counts[s[left]]:
        #             formed -= 1
        #         left += 1

        # left, right = result
        # return s[left:right+1] if min_length != float('infinity') else ''