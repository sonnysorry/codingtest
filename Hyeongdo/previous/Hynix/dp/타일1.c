#include<stdio.h>

int d[1001];

int dp(int x){
    if (x==1) return 1;
    if (x==2) return 2;
    // 특정 값 구했다면 그대로 반환하기.
    if (d[x] != 0) return d[x];
    // 오버플로우 발생 방지
    return d[x] = (dp(x-1) + dp(x - 2)) % 10007;
}

int main(void){
    int x;
    scanf("%d", &x);
    printf("%d", dp(x));
}