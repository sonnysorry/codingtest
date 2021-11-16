#주유소

n = int(input())

road = list(map(int, input().split()))
gas = list(map(int, input().split()))

# 처음 전체 비용으로 초기화
total_cost = gas[0]*road[0]
# 처음 주유 비용으로 초기화
gas_cost = gas[0] 
# 주유비용 리스트 돌면서
for i in range(1, len(gas)-1):
    # 주유 비용이 현재 가격보다 낮으면 가스비 바꿈 
    if gas[i] < gas_cost:
        gas_cost = gas[i]
    # 전체 비용에 현재 가스비 * 각 노드의 운행비용을 더해줌
    total_cost += gas_cost * road[i]

print(total_cost)