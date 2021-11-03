#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
dp[100000];
int fib(int n){
    if (n==0) return 0;
    if (n==1 || n==2) return 1;
    if (dp[n] != 0) return dp[n];
    return dp[n] = (fib(n-1) + fib(n-2))%1234567;
}
int solution(int n) {
    fib(n);
    int answer = dp[n];
    return answer;
}