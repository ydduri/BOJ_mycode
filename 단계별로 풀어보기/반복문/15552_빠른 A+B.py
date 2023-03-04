# .ipynb 파일에서는 sys.stdin.readline()을 제대로 사용할 수 없다고 하여 이번만 .py 파일로 작성

import sys
n_test = int(sys.stdin.readline().rstrip())

for i in range(n_test):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    print(a+b)