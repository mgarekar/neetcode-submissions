class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Brute force with an optimization
        # s = "zxyzxyz"
        res = 0
        l=0
        r=0
        tset=set()

        for r in range(len(s)):

            while( s[r] in tset ):
                print(f'removing in while loop')

                tset.remove(s[l])
                l = l + 1
                print(f'tset = {tset} and s[l] = {s[l]}')                    
                print('\n')

            #valid substring
            tset.add(s[r])
            res = max(res, len(tset))
            print(f'l = {l}, r ={r} & s[r] = {s[r]}')
            print(tset)
        return res











































    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     #Brute force with an optimization
    #     # s = "zxyzxyz"
    #     res = 0
    #     for i in range(len(s)):
    #         tset=set()
    #         for j in range(i,len(s)):
    #             subs=s[i:j+1]
    #             if s[j] in tset: break
    #             else: tset.add(s[j])
    #         res = max(res, len(tset))
    #     return res
             

























































        # maxL=0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         subs=s[i:j+1]
        #         if len(set(subs)) == len(subs):  # Check if all unique
        #             maxL = max(maxL, len(subs))                
        # return maxL








































































        # l,r=0,0
        # hs=set()
        # longest = 0
        # for r in range(len(s)):
        #     char=s[r]

        #     while char in hs:
        #         hs.remove(s[l])
        #         l = l +1

        #     hs.add(char)
        #     longest = max(longest, r-l+1)

        # return longest
                
            









































        # l,r=0,0
        # #zxyx
        # #yx - after
        # charset=set()
        # res=0
        # for r in range(len(s)):
        #     while( s[r] in charset ):#there are duplicates
        #         charset.remove(s[l])
        #         l = l +1
        #     charset.add(s[r])
        #     res = max(res, r-l+1 )
        # return res
