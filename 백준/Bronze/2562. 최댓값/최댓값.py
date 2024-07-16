ls = []

for i in range(9):
    num = int(input())
    ls.append(num)

mx = max(ls)

for i in range(len(ls)):
    if ls[i] == mx:
        print(mx)
        print(i+1)