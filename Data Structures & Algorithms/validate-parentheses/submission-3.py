class Solution:
    def isValid(self, s: str) -> bool:
        #[{()}]
        #[)](
        stack = []
        hm_close_to_open = {
                    ")": "(",
                    "}": "{",
                    "]": "["
                }

        for c in s:
            if stack and c in hm_close_to_open:
                if stack[-1] == hm_close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else: #pass throguh signs
                stack.append(c)

        return not stack