a = int(input())
b = int(input())

b1 = b % 10
b10 = (b // 10) % 10
b100 = (b // 100) 

r1 = a * b1
r10 = a * b10
r100 = a * b100
result = r1 + (r10 * 10) + (r100 * 100)

print(r1)
print(r10)
print(r100)
print(result)