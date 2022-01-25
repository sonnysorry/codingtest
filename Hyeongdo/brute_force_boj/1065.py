# 한수
# [boj-백준] Brute force 1065 한수 - python

n = int(input())

count = 0
# 리스트로 자리수 빼주기
for i in range(1, n+1):
    new_num = list(map(int, str(i)))
    # 99까지는 모든 수가 한수이므로 3자리부터 체크
    if len(new_num) <3:
        count += 1
    # 세자리부터    
    else:
        # 처음 값 - 두번째 값으로 등차인지 확인
        chk = new_num[0] - new_num[1]
        temp = 1
        # 두번째 값부터 하나씩 뒤에 것 빼주면서 등차 확인
        for i in range(1, len(new_num)-1):
            # 뒤에 것 체크해서 템프 값 올려주기
            if chk == new_num[i] - new_num[i+1]:
                temp += 1
        # 템프 값이 길이 - 1 이면 하나 카운트 해주기
        if temp == len(new_num)-1:
            count += 1
print(count)