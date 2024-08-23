#fucntion to convert prefix to infix

def prefixtoInfix(prefix):
    stack = []
    i = len(prefix)-1
    while i >= 0:
        if not checkoperator(prefix):
            stack.append(prefix[i])
            i-=1
        else:
            str = '(' + stack.pop() + prefix[i]+ stack.pop() + ')'
            stack.append(str)
            i-=1
    return stack.pop()
def checkoperator(c):
    if c == '+' and c == '-' and c == '*' and c == '/' and c == '(' and c == ')' and c == '^':
        return True
    else:
        return False



#valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {")":"(","}":"{","]":"["}
        for i in s:
            if i in hm:
                if stack and stack[-1] == hm[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

