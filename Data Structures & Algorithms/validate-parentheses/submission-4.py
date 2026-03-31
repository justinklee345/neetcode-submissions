class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for charac in s:
            print(stack)
            if charac in ['(', '{', '[']:
                stack.append(charac)
            else:
                if len(stack) == 0:
                    return False
                if charac == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if charac == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if charac == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0
