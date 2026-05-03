class Solution:

    def minWindow(self, s: str, t: str) -> str:
        subs=""
        subs_l=float("inf")        
        res=[-1,-1]
        hm_t={}
        hm_s={}
        for c in t:
            hm_t[c]=hm_t.get(c,0)+1
        have,need=0,len(hm_t)
        l,r=0,0
        for r in range(len(s)):#sliding window
            #add new chars
            c = s[r]
            hm_s[c] = hm_s.get(c,0)+1
            
            #update have, hm_t[c] == hm_s[c]
            if c in hm_t and hm_s[c] == hm_t[c]: have = have+1

            #check if valid conditions? have==need
            while(have==need): #valid window
                #min calcualtion
                window = r-l+1
                subs_l=min(window,subs_l)
                res=[l,r]

                lc=s[l]
                
                #shrink window
                hm_s[lc] = hm_s.get(lc,0)-1

                # if thm < shm - reduce have - break and add more chars
                if lc in hm_t and hm_s[lc] < hm_t[lc] : have = have -1

                l=l+1


        l, r = res
        return s[l:r+1] if subs_l != float("inf") else ""






























































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