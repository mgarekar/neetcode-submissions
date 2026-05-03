class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1="adc"
        # s2="dcda"

        if len(s1)>len(s2): return False

        #init
        hm_s1={}
        hm_s2={}
        matches=0
        l = 0
        for i in range(len(s1)):
            hm_s1[s1[i]] = hm_s1.get(s1[i],0)+1
            hm_s2[s2[i]] = hm_s2.get(s2[i],0)+1
        for i in range(26):
            char = chr(i+ord('a'))
            hm_s1[char]=hm_s1.get(char,0)
            hm_s2[char]=hm_s2.get(char,0)
            if hm_s1[char] == hm_s2[char]: matches = matches + 1

        print(hm_s1)
        print(hm_s2)
        print(matches)

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            incoming_c=s2[r]
            outgoing_c=s2[l]

            hm_s2[incoming_c] = hm_s2.get(incoming_c,0)+1
            if hm_s1[incoming_c] == hm_s2[incoming_c]: matches = matches + 1
            elif hm_s2[incoming_c]  - 1 == hm_s1[incoming_c] : matches = matches - 1

            hm_s2[outgoing_c] = hm_s2.get(outgoing_c,0) - 1
            if hm_s1[outgoing_c] == hm_s2[outgoing_c]: matches = matches + 1
            elif hm_s2[outgoing_c] + 1 == hm_s1[outgoing_c] : matches = matches - 1

            l = l + 1

        return matches == 26















































































# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         # s1="ky"
#         # s2="ainwkckifykxlribaypk"

#         hm_s1={}
#         hm_s2={}
#         l,r=0,0

#         if len(s1)>len(s2): return False
#         for i in range(len(s1)):
#             hm_s1[s1[i]] = hm_s1.get(s1[i],0) + 1   
#             hm_s2[s2[i]] = hm_s2.get(s2[i],0) + 1 

#         if hm_s1 == hm_s2: return True

#         print(hm_s1)
#         print(hm_s2)        
#         for r in range( len(s1), len(s2) ):

#             #update hash map
#             rchar = s2[r]
#             hm_s2[rchar] = hm_s2.get(rchar,0) + 1


#             #passed left char so remove and delete
#             lchar=s2[l]
#             hm_s2[lchar] = hm_s2.get(lchar,0) - 1
#             if hm_s2[lchar] <= 0: del hm_s2[lchar]
#             l=l+1

#             #compare updated hm
            
#             if hm_s1 == hm_s2: return True  
#             print(hm_s2)                    
#         return False














































































# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         l,r=0,0
#         hm_s1={}
#         hm_s2={}
#         window=len(s1)

#         if len(s1)>len(s2): return False


#         #init
#         for i in range(window):
#             hm_s1[s1[i]] = hm_s1.get(s1[i],0)+1
#             hm_s2[s2[i]] = hm_s2.get(s2[i],0)+1
#         if hm_s1 == hm_s2: return True

#         #slide
#         for r in range(window, len(s2)):
#             #compare hm_s1 and hm_s2

#             #move window forward
#             rchar = s2[r]
#             lchar = s2[l]
#             hm_s2[rchar] = hm_s2.get(rchar,0)+1
#             hm_s2[lchar] = hm_s2[lchar] -1
#             if hm_s2[lchar] == 0: del hm_s2[lchar]
#             l=l+1

#             if hm_s1 == hm_s2: return True

#         return False








































        # l,r=0,0
        # hm_s1={}
        # hm_s2={}

        # def compare_hm(hm_s1,hm_s2):
        #     matches = 0
        #     for key in hm_s1:
        #         if key not in hm_s2: return False
        #         if hm_s2[key] != hm_s1[key]: return False
        #         if hm_s2[key] == hm_s1[key]: matches = matches + 1
        #     if matches == len(hm_s1): return True

        # if len(s1)>len(s2): return False

        # for i in range(len(s1)):
        #     hm_s1[s1[i]]=hm_s1.get(s1[i],0)+1
        #     hm_s2[s2[i]]=hm_s2.get(s2[i],0)+1
        # #length of window = len of s1

        # for r in range(len(s1), len(s2)):
        #     #r should start at end of current window
        #     #compare hm
        #     # if hm_s1 == hm_s2: return True
        #     if compare_hm(hm_s1,hm_s2): return True

        #     #update hm
        #     new_char=s2[r]
        #     old_char=s2[l]
        #     hm_s2[new_char] = hm_s2.get(new_char, 0) + 1
            
        #     hm_s2[old_char] = hm_s2.get(old_char) - 1 
        #     if hm_s2[old_char] == 0: del  hm_s2[old_char]

        #     l=l+1
        # return False
