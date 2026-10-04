# 문제 08. 괄호 짝 맞추기
# 261004 일 17:10 - 17:23


def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if len(stack) == 0:
                result = False
            else:
                stack.pop()
    if len(stack)==0:
        result = True
    else:
        result = False
    return result

s = "(())()"
# s = "((())()"

print(solution(s))