class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                string = ""
                while stack[-1]!="[":
                    string = stack.pop() + string
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*string)
            else:
                stack.append(c)
        
        return ('').join(stack)
            



        





        