class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s={}
        hm_t={}
        for num in s:
            hm_s[num] = hm_s.get(num,0)+1
        for num in t:
            hm_t[num] = hm_t.get(num,0)+1            



        def compare_hm(hm_s,hm_t):
            if len(hm_s) != len(hm_t): return False
            for key in hm_s:
                if key not in hm_t: return False
                else:
                    if (hm_s[key]) != (hm_t[key]): return False
            return True

        return compare_hm(hm_s,hm_t)


        