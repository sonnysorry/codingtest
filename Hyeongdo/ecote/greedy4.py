#모험가길드

data = list(map(int, input().split()))

sorted(data, reverse=False)

result = 0 #그룹수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data: # 공포도 낮은 것부터 확인
    count += 1 # 현재 그룹에 모험가 포함
    if count >= i : # 모험가 수가 현재 공포도 이상일 시, 그룹 결성
        result += 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹에 포함된 모험가 수 초기화

print(result)