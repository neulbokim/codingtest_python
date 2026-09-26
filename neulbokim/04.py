# 문제 04. 모의고사
# 23:33 ~ 

def solution(answers):
    supo2_pattern = [2,1,2,3,2,4,2,5]
    supo3_pattern = [3,3,1,1,2,2,4,4,5,5]
    
    supo1 = [(i%5 + 1) for i in range(len(answers))]
    supo2 = [supo2_pattern[i%len(supo2_pattern)] for i in range(len(answers))]
    supo3 = [supo3_pattern[i%len(supo2_pattern)] for i in range(len(answers))]
    
    count1, count2, count3 = 0,0,0
    for i in range(len(answers)):
        if answers[i] == supo1[i]:
            count1 += 1
        if answers[i] == supo2[i]:
            count2 += 1
        if answers[i] == supo3[i]:
            count3 += 1
    
    correct_count = [count1, count2, count3]
    
    max_count = max(correct_count)
    
    return [i+1 for i in range(3) if correct_count[i] == max_count]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))