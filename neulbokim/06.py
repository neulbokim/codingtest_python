# 문제 06. 실패율
# 260928 16:05 ~ 16:13 잠깐 포기..
# 260928 18:34 ~ 18:57 개어렵다 ㅜ
# 260929 21:21 ~ 

def solution(stages, N):
    실패율 = []
    for stage in range(1, N+1):
        실패 = 0
        도전 = 0
        for player in stages:
            if stage <= player:
                도전 += 1
            if stage == player:
                실패 += 1
        rate = 실패 / 도전 if 도전 > 0 else 0
        실패율.append((stage, rate))   # (스테이지 번호, 실패율) 튜플로 저장

    실패율.sort(key=lambda x: x[1], reverse=True)  # x[1] = 실패율 값 기준 내림차순

    return [stage for stage, rate in 실패율]


stages = [2,1,2,6,2,4,3,3]
N = 5

# stages = [4,4,4,4,4]
# N = 4

print(solution(stages, N))