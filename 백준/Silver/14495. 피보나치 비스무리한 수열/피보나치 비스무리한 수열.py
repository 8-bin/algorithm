n = int(input())  
arr = [0] * (n + 1)

def seq(n):
    if arr[n] != 0:
        return arr[n]
    if n == 1 or n == 2 or n == 3:
        arr[n] = 1
    else:
        arr[n] = seq(n - 1) + seq(n - 3)
    return arr[n]

seq(n)  
print(arr[n])