# 문제 07. 방문 길이
# 261003 00:45~01:30 (클로드의 도움을 받음 하아아아...)

def solution(dirs):
    position = [0,0] #현재 위치

    visited_edges = set()

    for char in dirs:
        # print(char, end='')
        next_position = position.copy()
        if char == "U":
            next_position[1] = position[1] + 1
        elif char == "D":
            next_position[1] = position[1] - 1
        elif char == "R":
            next_position[0] = position[0] + 1
        elif char == "L":
            next_position[0] = position[0] - 1
            
        if -5 <= next_position[0] <=5 and -5 <= next_position[1] <= 5:
            edge = frozenset([tuple(position), tuple(next_position)]) #frozenset이라는 게 있구나
            visited_edges.add(edge)
            position = next_position
    return len(visited_edges)


# 입출력의 예
# dirs = "ULURRDLLU"

dirs = "LULLLLLLLU"

print(solution(dirs))