import tsp
import random

LIMITS = 100

def first_choice(p):
    current = tsp.random_init(p)
    value_distance = tsp.evaluate(current, p)
    ## 알고리즘 활용해서 최적값을 변경하는 코드 작성
    ## value_distance 이걸 어떻게 줄이나요?
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        _value_distance = tsp.evaluate(successor, p)
        if value_distance < _value_distance:
            current = successor
            value_distance = _value_distance
            i = 0
        else:
            i += 1

    return current, value_distance

def random_mutant(current, p):
    while True:
        # 좌는 받아왓음 방법이없다.
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            cur_copy = inversion(current, i, j)
            break
    return cur_copy    

def inversion(current, i, j):
    cur_copy = current[:]
    while i < j:
        cur_copy[i], cur_copy[j] = cur_copy[j], cur_copy[i]
        i += 1
        j -= 1
    return cur_copy

if __name__ == "__main__":
    p = tsp.create_problem("./data/tsp30.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)