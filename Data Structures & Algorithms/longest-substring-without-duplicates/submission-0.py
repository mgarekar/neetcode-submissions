class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        #zxyx
        #yx - after
        charset=set()
        res=0
        for r in range(len(s)):
            while( s[r] in charset ):#there are duplicates
                charset.remove(s[l])
                l = l +1
            charset.add(s[r])
            res = max(res, r-l+1 )
        return res
