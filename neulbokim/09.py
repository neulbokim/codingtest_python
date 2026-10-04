# 문제 09. 10진수를 2진수로 변환하기
# 261004 일 17:37-18:00

def solution(decimal):
    stack = []
    while True:
        stack.append(str(decimal % 2))
        decimal = decimal // 2
        # print("2로 나눈 몫:", decimal, ", 현재 stack: ",stack)
        if decimal == 0:
            break
        
    result = []
    for i in range(len(stack)):
        result.append(stack[-i-1])
        # print("현재 result: ", result)
    
    result = "".join(result)
    # print("문자열로 바꾼 result: ", result)
    return result

print(solution(10))
print(solution(27))
print(solution(12345))