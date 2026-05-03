class Solution:


    # dummy_input = ["Hello","World"]

    def encode(self, strs: List[str]) -> str:
        # strs = ["Hello","World"]    
        encoded_s=''

        for word in strs:
            encoded_s = encoded_s + str(len(word)) + '#' + word
        return encoded_s

    def decode(self, s: str) -> List[str]:
        # dummy_input = ["Hello","World"]        
        # s='51#hello5#world'
        ans=[]
        i=0
        while( i<len(s) ):
            word=''

            j=i
            while( s[j] != '#' ): 
                j=j+1
                #j is at '#'
            len_word=int(s[i:j])
            word = s[  (j+1) : (j+1+len_word)    ]

            ans.append(word)
            i = (j+1+len_word)


        return ans