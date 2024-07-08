a, b = map(int, input().split())
c = int(input())

m = b+c

while (True):
    if m >= 60 :
        m = m - 60
        a = a + 1
    elif m < 60 :
        break
           
if a >= 24 : 
    a = a - 24
 
print(a, m)