#9012, 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
# 오..()를 -1 +1이 아니라 +1 -1 방향으로 생각하면 훨씬 더 간결하게 짤 수 있다.. 막힌 사고의 나쁜 예..

import sys

N = int(sys.stdin.readline())

for i in range (N) :
    flag = True
    num = 0
    input_list = list(sys.stdin.readline().rstrip())
    for s in input_list :
        if s == "("   : num -= 1
        elif s == ")" : num += 1
        else :
            flag = False
        if num>0 : 
            flag = False
    if (flag and num==0) : print("YES")
    else : print("NO")