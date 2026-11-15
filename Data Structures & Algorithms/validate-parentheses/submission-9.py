class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for charac in s:
            if charac in ['(', '{', '[']:
                stack.append(charac)
            else:
                if len(stack) == 0:
                    return False
                if charac == ')' and stack[-1] == '(':
                    stack.pop()
                elif charac == '}' and stack[-1] == '{':
                    stack.pop()
                elif charac == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(charac)
                
        if len(stack) == 0:
            return True
        return False
                
        