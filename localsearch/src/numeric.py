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

def create_problem(filename):
    # 1-1. 파일을 읽자!
    ini_file = open(filename, 'r')
    expression = ini_file.readline().strip()
    # 리스트
    var_names = []
    low = []
    up = []

    for line in ini_file.readline():
        #n,l,u = tuple(line.split(",")[0])
        var_names.append(line.split(",")[0])
        low.append(float(line.split(",")[1]))
        up.append(float(line.split(",")[1]))

    ini_file.close()
    domain = [var_names, low, up]
    # 1-2. 수식과 리스트로 분리
    # 1-3. 리터!!
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(0, len(domain[0])):
        #랜덤선택!
        # 최대 최소 사이의 랜덤 값
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init
#p가 튜플이란 가정하에
def evaluate(current, p):
    num_evel = 0
    current = p[0]
    var_name = p[1][0]

    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(current[i])
        exec(assignment) #exec 문자열을 파이썬으로실행시키는거 회사에서는 보안떄문에 x
    return eval(expr)

if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    # 식과 인자를 번가
    describe_problom(p)
    sultion = random_init(p)
    minimum = evaluate(solution, p)
    print(f"{minimum}")

# 1. 함수 작성 가능
# 2. 파일 읽기 가능
# 3. 리스트 사용 가능
# 4. 반복문 사용 가능

# T1. pytest / junit => 켄트 백 "테스트 주도 개발"
# T2. 함수 연결해서 사용하는 방법(f call)