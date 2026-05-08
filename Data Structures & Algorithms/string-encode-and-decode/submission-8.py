class Solution:

    # dummy_input = ["Hello","World"]  

    def encode(self, strs: List[str]) -> str:
        DELIMITER='#'
        ans=''
        for s in strs:
            l_word=str(len(s))
            ans = ans + l_word + DELIMITER + s
        return ans

    def decode(self, s: str) -> List[str]:
        # s = '5#Hello15#World'
        ans=[]

        i=0
        while( i<len(s) ):
            j=i

            while( s[j] != '#' ):
                j=j+1
            #j is at #    
            word_l=int(s[i:j])

            word = s[ j+1: j+1+word_l   ]
            ans.append(word)

            i = j+1+word_l

        return ans