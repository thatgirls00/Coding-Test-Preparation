import sys

m, n = map(int, sys.stdin.readline().split())
arr = []

for i in range(m):
    arr.append(int(input()))

start = 1
end = max(arr)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(m):
        cnt += arr[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)