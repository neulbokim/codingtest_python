# 문제 03. 두 개 뽑아서 더하기
# 15:04 ~ 15:13
        
def solution(numbers):
    result = list()
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                result.append(numbers[i] + numbers[j])
                
    result = list(set(result))
    result.sort()
    
    return result

#TEST 코드입니다. 주석을 풀어서 확인해보세요
print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]
