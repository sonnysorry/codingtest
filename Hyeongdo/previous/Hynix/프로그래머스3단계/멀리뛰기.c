#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
dp[2000];
long long fib(int n){
    if (n==1) return 1;
    if (n==2) return 2;
    if (dp[n] != 0) return dp[n];
    return dp[n] = (fib(n-1) + fib(n-2)) % 1234567;
}
long long solution(int n) {
    long long answer = fib(n);
    return answer;
}