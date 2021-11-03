#include <stdio.h>
// 퀵 정렬
int n = 10;
int data[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};

void qSort(int *data, int start, int end){
    if (start >= end){ // 원소 1개인 경우
        return;
    }
    int key = start; // 첫번째 값
    int i = start + 1; // 인덱스 
    int j = end; // 마지막 값 (오른 쪽 출발 지점)
    int temp;

    while(i <= j) { // 엇갈릴 때까지 반복
        while(data[i] <= data[key]){
            i++; // 키 값보다 큰 값 만날 때까지 오른쪽으로 이동.
        }
        while(data[j] >= data[key] && j > start){ // 왼쪽으로만 넘어가지 않게 설정
            j--; // 키 값보다 큰 값 만날 때까지 오른쪽으로 이동.
        }
        if (i > j) {
            temp = data[j];
            data[j] = data[key];
            data[key] = temp;
        } else{
            temp = data[j];
            data[j] = data[i];
            data[i] = temp;
        }
    }
    qSort(data, start, j-1);
    qSort(data, j+1, end);
}

int main(void){
    qSort(data, 0, n-1);
    for (int i = 0; i < n; i++){
        printf("%d", data[i]);
    }
}