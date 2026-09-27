# 문제 05. 행렬의 곱셈
# 260927 09:26 ~ 10:15

def solution(arr1, arr2):
    ret = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    print(ret)
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr2)):
                ret[i][k] += arr1[i][j]*arr2[j][k]
        print(ret)
    return ret

# arr1 = [[1,4],[3,2],[4,1]]
# arr2 = [[3,3],[3,3]]

arr1 = [[2,3,2],[4,2,4],[3,1,4]]
arr2 = [[5,4,3],[2,4,1],[3,1,1]]
print(solution(arr1, arr2))