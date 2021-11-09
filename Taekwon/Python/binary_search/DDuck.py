'''
풀이방법
 1. 입력 받은 떡의 개별 높이 중, 가장 큰 값을 h의 초기값으로 설정
 2. h를 1씩 줄여나간다는 알고리즘 생각
 3. h를 기준으로 잘리고 남은 떡 길이의 총합이 입력받은 m과 같거나 크다면 반복문 종료

단, 이러한 알고리즘으로 문제를 풀었을 때의 문제점. 0~10억까지의 숫자이기 때문에 숫자를 1씩 줄여간다면
시간복잡도를 장담할 수 없음..
'''

n, m = map(int, input().split())
d = list(map(int, input().split()))

h = max(d)
sd = 0

while sd <= m:
    for i in d:
        i_minus_h = i - h
        if i_minus_h < 0:
            i_minus_h = 0
        sd += i_minus_h
    h = h - 1

print(h)
