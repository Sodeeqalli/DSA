class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                x = stack[-1] + stack[-2]
                stack.append(x)
            elif op == 'D':
                x = stack[-1] * 2
                stack.append(x)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)



        