# 그래프  => TSP
# TSP => 간선의 합이 최소임을 원함

# 50개(!) #일반화된 상태에서(n)

# 간선과 정점으로 구성된 자료구조
# 간선
# - 방향성이 있는 것 => 네트워크
# - 방향성이 없는 것 => 순수 그래프(조합 그래프)

# 문제 해결 방법
## 간단한 언덕 등반 알고리즘
## > Convex.txt 를 사용해서 계산

## 1. 파일을 읽어서 뭔가 만들어냄!
## 2. 그 뭔가로 초기값을 생성함
## 3. Convex.txt 파일의 수식과 값을 이용해서 계산

# 여러분이 작성가능
# 읽기 좋게 짜기!

# 상태(state)
# -> 상태가  관지자
import random
import math

# TODO : 인접행렬 그래프 만들고 다시.
def create_problem(filename):
    f = open(filename, "r")
    num_cities = int(f.readline())

    locations = []
    for line in f.readlines():
        # 튜블(x,y)
        locations.append(eval(line))

    f.close()
    table = create_distance_table(num_cities, locations)
    return num_cities, locations, table
#그래프는 어떻게 표현할까? 입접행렬을 만들어야 됨

def create_distance_table(num_cities, locations):
    
    # 1)거리 계산
    # 맨하튼?? => 격자(grid world) 이문제는 이거안씀
    #  - 유클리드 거리 
    #  - 점 두 개가 필요?
    table = []
    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            distance = math.sqrt(((locations[i][0] - locations[k][0] )**2 + (locations[i][1] - locations[k][1] )**2))
            line.append(distance)
        table.append(line)
    
    return table

def random_init(p):
    # 결과 shuffle!

    n = p[0]
    init = list(range(n)) # 0.. n-1
    random.shuffle(init)
    return init
 
def evaluate(current, p):
    # cost 출력

    cost = 0
    num_cities, locations, table = p
    for i in range(num_cities):
        cost += table[current[i]][current[i-1]]
    return cost

def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of ci\teis : {n}")
    locations = p[1]
    #table = p[2]
    for i in range(n):
        print(f"locations{i}")
        if i % 5 == 4:
            print()

if __name__ == "__main__":
    p = create_problem("./data/tsp30.txt")
    #describe_problem(p)
    init = random_init(p)
    print(evaluate(init, p))