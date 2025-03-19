import sys

# 단어를 저장할 리스트
words = [sys.stdin.readline().strip() for _ in range(5)]

# 결과 저장 변수
result = ""

for i in range(15):  
    for word in words:
        if i < len(word):  
            result += word[i]

# 결과 출력
print(result)