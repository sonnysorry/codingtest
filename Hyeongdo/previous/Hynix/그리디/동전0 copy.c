#include<stdio.h>

int main(void){
    int n;
    long long k;
    scanf("%d %lld",&n, &k);
    // arr 에 값을 담는다.
    int arr[10];
    for (int i =0; i <n ; i++){
        scanf("%d", &arr[i]);
    }
    int count = 0;
    // 동전 맨 위에서 부터 내리기 체크.
    int i = n-1;
    // k가 0이 될 때까지.
    while(k > 0){
        if(arr[i] > k){
            i--;
        }
        else{
            k-=arr[i];
            count++;
        }
    }
    printf("%d", count);
    return 0;
}