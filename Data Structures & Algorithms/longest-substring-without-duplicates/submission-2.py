class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL=0
        for i in range(len(s)):
            for j in range(i, len(s)):
                subs=s[i:j+1]
                valid_subs = set(subs)
                if len(set(subs)) == len(subs):  # Check if all unique
                    maxL = max(maxL, len(subs))                
        return maxL








































































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
