class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        counts_hm= {}
        res=0

        for r in range(len(s)):
            counts_hm[s[r]] = counts_hm.get(s[r],0)+1

            #is window not valid?
            while( ((r-l+1) - max(counts_hm.values())) > k  ):
                counts_hm[s[l]] = counts_hm[s[l]] - 1
                l = l +1

            #valid window
            res = max(res, r-l+1)
        return res





























    # def characterReplacement(self, s: str, k: int) -> int:
    #     res=0
    #     l,r=0,0
    #     hm={}

    #     for r in range(len(s)):
    #         rchar=s[r]
    #         #add to hm
    #         hm[rchar] = hm.get(rchar,0)+1

    #         #valid window is where we can make all characters the same
    #         while( (r-l+1) - max(hm.values()) > k  ):#window is not valid
    #             lchar=s[l]
    #             hm[lchar] = hm.get(lchar,0) - 1  
    #             l=l+1

    #         window = r-l+1
    #         res = max( res, window )
    #     return res










































































    # def characterReplacement(self, s: str, k: int) -> int:
    #     #lenght of valid substrings
    #     #find if substring is valid
    #     #slide on substrings

    #     res=0
    #     string_hm={}
    #     l,r=0,0

    #     for r in range(len(s)):

    #         #add to HM
    #         string_hm[s[r]] = string_hm.get(s[r],0) +1



    #         while( (r-l+1) - max(string_hm.values()) > k ): #window is not valid
    #             string_hm[s[l]] = string_hm[s[l]] -1
    #             l=l+1
    #         window = r-l+1

    #         res = max(window, res)
    #     return res
            













































        # res=0
        # count={}
        # l,r=0,0

        # for r in range(len(s)):
        #     #add to hm
        #     count[s[r]]=count.get(s[r],0) + 1
        #     while( (r-l+1) - max(count.values()) > k ): #window is invalid
        #         count[s[l]] -= 1
        #         l=l+1 #move forward till window is valid

        #     res = max(res, r-l+1)
        # return res