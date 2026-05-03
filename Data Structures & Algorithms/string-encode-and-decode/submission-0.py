class Solution:

    def encode(self, strs: List[str]) -> str:
        #converts to a encoded string
        res=''
        for strin in strs:
            res = res + str(len(strin)) + '#' + strin 
        return res

    def decode(self, s: str) -> List[str]:
        
        strs = []
        #i - start of encoded string
        #j - start of actual string with 45#abcd...
        i,j=0,0
        while ( i < len( s ) ):
            j = i

            while ( s[j] != '#' ):
                j = j +1

            length = int(s[i:j])
            word = s[j+1: j + 1 + length  ] 
            strs.append(word)
            i = j + 1 + length

            #debug
            print(length)
            print(word)

        return strs
