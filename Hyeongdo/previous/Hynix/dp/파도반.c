#include<stdio.h>

int main(void){
    int t, ans;
    int arr[101];
    scanf("%d", &t);
    for(int i=0; i < t; i++){
    }
    long long dp[101] = {0, 1, 1, 1, 2, 2, };
    
    for (int x = 6; x < 101; x++){
        dp[x] = dp[x-1] + dp[x-5];
    }
    for(int j = 0; j < t; j++){
        scanf("%d", &ans);
        printf("%lld \n", dp[ans]);
    }
    return 0;
}
