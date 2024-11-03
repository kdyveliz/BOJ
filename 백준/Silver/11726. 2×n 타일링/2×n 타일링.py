N = int(input())
rect = [0,1,2,3,5] + [0]*996

for i in range(5,1001):
    rect[i] = rect[i-2]+rect[i-1]

print(rect[N]%10007)