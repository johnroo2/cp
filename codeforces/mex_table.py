#rating: 800
def mex_table(x, y):
    return max(x, y) + 1

n = int(input())

for _ in range(n):
    x, y = map(int, input().split()) 
    print(mex_table(x, y))
    