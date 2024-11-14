from collections import deque

T = 10
for _ in range(T):
    tc = input()
    numbers = list(map(int, input().split()))
    queue = deque(numbers)
    
    while True:
        for i in range(1, 6): 
            current = queue.popleft()  
            new_number = current - i  
            if new_number > 0:
                queue.append(new_number)  
            else:
                queue.append(0)  
                break
        if new_number <= 0:
            break 
    
    print("#" + tc, end=' ')
    for num in queue:
        print(num, end=' ')
    print()  
