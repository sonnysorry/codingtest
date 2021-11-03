#include<stdio.h>
int dp[10000001];
int tile(int x){
    if(x==0) return 0;
    if(x==1) return 1;
    if(x==2) return 2;
    if(dp[x] != 0) return dp[x];
    return dp[x] = (tile(x-1) + tile(x-2))% 15746;
}
int main(void){
    int n;
    scanf("%d", &n);
    int answer = tile(n);
    printf("%d", answer);
    return 0;
}