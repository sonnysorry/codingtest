#include <stdio.h>

int w[101] = {0, };
int p[101] = {0, };
int dp[101] = {0, };

int max(int a, int b){
    if (a >= b) return a;
    else return b;
}

int main(void){
    int n, k;
    scanf("%d %d", &n, &k);
    for(int i = 1; i < n; i++){
        scanf( "%d %d", &w[i], &p[i]);
    }
    for (int i = 0; i < n; i++){
        for (int j = k; j >=0; j--){
            if (w[i] <= j){
                dp[j] = max(dp[j], dp[j - w[i]] + p[i]);
            }
        }
    }
    printf("%d", dp[k]);
    return 0;
}