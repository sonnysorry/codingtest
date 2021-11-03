#include <stdio.h>
int dp[100];
int fib(int x){
    if (x==0) return 0;
    if (x==1) return 1;
    if(dp[x] != 0) return dp[x];
    return dp[x] = fib(x-1) + fib(x-2);
}

int main(void){
    int t;
    scanf("%d", &t);
    int arr[100];
    for(int i = 0; i < t; i++){
        scanf("%d", &arr[i]);
    }
    int max = arr[0];
    for (int i = 0; i < t; i++) {
        if (arr[i] > max) max = arr[i];
    }
    fib(max);
    for(int i = 0; i < t; i++){
        int count_0, count_1 = 0;
        for(int k = 0; k < arr[i]; k++){
            if (dp[k] == 0){
                count_0++;
            } 
            if (dp[k] == 1){
                count_1++;
            }
        }
        printf("%d %d \n", count_0, count_1);
    }
    return 0;
}
