class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = []
        mapping = {'[':']','{':'}','(':')'}
        for bracket in s:
            if bracket in ['[','{','(']:
                brackets_stack.append(bracket)
            else:
                if len(brackets_stack) == 0:
                    return False
                popped_br = brackets_stack.pop()
                if mapping[popped_br] != bracket:
                    return False
        return len(brackets_stack) == 0