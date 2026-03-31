class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        logic_stack = []
        ops = ["+", "-", "*", "/"]

        for token in tokens:
            if token in ops:
                rhs = logic_stack.pop()
                lhs = logic_stack.pop()
                if token == "+":
                    logic_stack.append(str(int(int(lhs) + int(rhs))))
                elif token == "-":
                    logic_stack.append(str(int(int(lhs) - int(rhs))))
                elif token == "*":
                    logic_stack.append(str(int(int(lhs) * int(rhs))))
                else:
                    logic_stack.append(str(int(int(lhs) / int(rhs))))
            else:
                logic_stack.append(token)
        
        return int(logic_stack.pop())
                