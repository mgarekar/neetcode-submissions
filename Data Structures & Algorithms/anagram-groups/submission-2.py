class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        hm={} # anagram -> []
        #anagram = sorted string

        for str in strs:
            l=sorted(str)
            ss="".join(l)

            if ss not in hm:
                hm[ss] = []
                hm[ss].append(str)
            else:
                #sorted string in HM. 
                hm[ss].append(str)
        return list(hm.values())