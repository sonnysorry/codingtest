/* A * 특징
1.
openList와 closeList라는 보조 데이터를 사용한다.
2.
F = G + H
를
매번
노드를
생성할
때마다
계산한다.
3.
openList에는
현재
노드에서
갈
수
있는
노드를
전부
추가해서
F, G, H를
계산한다.
openList에
중복된
노드가
있다면, F값이
제일
작은
노드로
바꾼다.

4.
closeList에는
openList에서
F값이
가장
작은
노드를
추가시킨다.
* /

openList.add(startNode)  # openList는 시작 노드로 init

while openList is not empty:
    # 현재 노드 = openList에서 F 값 가장 작은 것
    currentNode < - node in openList
    having
    the
    lowest
    F
    value
    openList.remove(currentNode)  # openList에서 현재 노드 제거
    closeList.add(currentNode)  # closeList에 현재 노드 추가

    if goalNode is currentNode:
        currentNode.parent.position
        계속
        추가
        후
        경로
        출력
        후
        종료

    children < - currentNode와
    인접한
    모든
    노드
    추가

    for each child in children:
        if child in closeList:
            continue

        child.g = currentNode.g + child와
        currentNode
        거리(1)
        child.h = child와
        목적지까지의
        거리
        child.f = child.g + child.h

        # child가 openList에 있고, child의 g 값이 openList에 중복된 노드 g값과 같으면
        # 다른 자식 불러오기
        if child in openList and child.g > openNode.g in openList:
            continue

        openList.add(child)

[출처: https: // choiseokwon.tistory.com /]