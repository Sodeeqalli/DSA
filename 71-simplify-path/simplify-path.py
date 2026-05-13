class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [p for p in path.split('/') if p]
        stack = []

        for d in directories:
            if d == '.':
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return "/" + ("/").join(stack)
                
            

        