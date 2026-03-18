class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for bracket in s:
            if bracket not in bracketMap:
                stack.append(bracket)
            else:
                if not stack or bracketMap[bracket] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack




        