import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

tl = [[0]*m for _ in range(n)]
tr = [[0]*m for _ in range(n)]
bl = [[0]*m for _ in range(n)]
br = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            tl[i][j] = a[i][j]
        elif i == 0:
            tl[i][j] = min(tl[i][j-1], a[i][j])
        elif j == 0:
            tl[i][j] = min(tl[i-1][j], a[i][j])
        else:
            tl[i][j] = min(a[i][j], tl[i-1][j], tl[i][j-1])

for i in range(n):
    for j in range(m-1, -1, -1):
        if i == 0 and j == m-1:
            tr[i][j] = a[i][j]
        elif i == 0:
            tr[i][j] = min(tr[i][j+1], a[i][j])
        elif j == m-1:
            tr[i][j] = min(tr[i-1][j], a[i][j])
        else:
            tr[i][j] = min(a[i][j], tr[i-1][j], tr[i][j+1])

for i in range(n-1, -1, -1):
    for j in range(m):
        if i == n-1 and j == 0:
            bl[i][j] = a[i][j]
        elif i == n-1:
            bl[i][j] = min(bl[i][j-1], a[i][j])
        elif j == 0:
            bl[i][j] = min(bl[i+1][j], a[i][j])
        else:
            bl[i][j] = min(a[i][j], bl[i+1][j], bl[i][j-1])

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i == n-1 and j == m-1:
            br[i][j] = a[i][j]
        elif i == n-1:
            br[i][j] = min(br[i][j+1], a[i][j])
        elif j == m-1:
            br[i][j] = min(br[i+1][j], a[i][j])
        else:
            br[i][j] = min(a[i][j], br[i+1][j], br[i][j+1])

q = int(input())

for _ in range(q):
    R, C = map(int, input().split())
    R -= 1
    C -= 1

    ans = 0

    if R > 0 and C > 0:
        ans += tl[R-1][C-1]
    if R > 0 and C < m-1:
        ans += tr[R-1][C+1]
    if R < n-1 and C > 0:
        ans += bl[R+1][C-1]
    if R < n-1 and C < m-1:
        ans += br[R+1][C+1]

    print(ans)
    