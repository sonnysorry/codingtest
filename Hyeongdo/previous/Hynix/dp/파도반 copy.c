#include<stdio.h>
long long dp[100];
long long pado(int x){
    if(x==1 || x==2 || x==3) return 1;
    if(x==4 || x==5) return 2;
    if (dp[x] != 0) return dp[x];
    return dp[x] = pado(x-1) + pado(x-5); 

}
int main(void){
    int t, ans;
    int arr[101];
    scanf("%d", &t);
    for(int j = 0; j < t; j++){
        scanf("%d", &ans);
        printf("%lld \n", pado(ans));
    }
    return 0;
}
