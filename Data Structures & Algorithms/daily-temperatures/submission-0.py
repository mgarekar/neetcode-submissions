class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack=[] # [temp, index]

        for i,temp in enumerate(temperatures):
            while( stack and temp > stack[-1][0] ):# compared to top of stack? -- pop - High temp incoming - compare in loop
               temp2, index = stack.pop()
               days = i - index
               res[index] = days
            stack.append( [temp,i] ) # Saving all the small temperatures

        return res




