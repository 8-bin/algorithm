count = 0
max_count = 0

for _ in range(10):
    minus, plus = map(int, input().split())
    count += plus
    count -= minus
    max_count = max(max_count, count)

print(max_count)