sum1 = int(input())
n = int(input())
sum2 = 0
sum3 = 0

for i in range(n) :
    a, b = map(int, input().split())
    sum2 = a * b
    sum3 += sum2

if (sum1 == sum3) :
    print('Yes')
else :
    print('No')