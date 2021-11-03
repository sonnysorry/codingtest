prec_n = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def post_fix(s):
    stack = []
    re = ''
    for c in s:
        if c not in '()+-*/':
            re += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                re += stack.pop()
            stack.pop()
        elif stack and prec_n[c] <= prec_n[stack[-1]]:
            re += stack.pop()
            stack.append(c)
        else:
            stack.append(c)

    while stack:
        re += stack.pop()
    return re

s = str(input())
print(post_fix(s))