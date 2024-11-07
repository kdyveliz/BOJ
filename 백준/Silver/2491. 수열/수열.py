import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
increase = 1
decrease = 1
ans = 1

for i in range(1, N):
    # 증가 수열이라면
    if nums[i - 1] <= nums[i]:
        increase += 1
    else:
        increase = 1

    # 감소수열이라면
    if nums[i - 1] < nums[i]:
        decrease = 1
    else:
        decrease += 1

    ans = max(ans, increase, decrease)

print(ans)