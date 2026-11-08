class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                temp_res = stack.pop() + stack.pop()
                stack.append(temp_res)
            elif token == '-':
                temp_res = - stack.pop() + stack.pop()
                stack.append(temp_res)
            elif token == '*':
                temp_res = stack.pop() * stack.pop()
                stack.append(temp_res)
            elif token == '/':
                temp_val = stack.pop()
                temp_res = stack.pop() / temp_val
                stack.append(int(temp_res))
            else:
                stack.append(int(token))
        return stack.pop()
