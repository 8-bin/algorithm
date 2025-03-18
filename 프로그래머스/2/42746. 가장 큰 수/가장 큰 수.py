from functools import cmp_to_key

def compare(x, y):
    return (int(y + x) - int(x + y))

def solution(numbers):
    numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
    numbers.sort(key=cmp_to_key(compare))  # 정렬 기준 적용
    result = ''.join(numbers)  # 정렬된 숫자를 이어 붙이기
    return '0' if result[0] == '0' else result  # 0이 여러 개일 경우 처리
