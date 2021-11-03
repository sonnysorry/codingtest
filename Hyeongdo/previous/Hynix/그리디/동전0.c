#include<stdio.h>

int main(void){
    int n;
    long long k;
    scanf("%d %lld",&n, &k);
    int arr[10];
    for (int i =0; i <n ; i++){
        scanf("%d", &arr[i]);
    }
    int count = 0;
    for (int j = n-1; j >= 0; j--){
        if (arr[j] < k){
            for (int p = 1; p < 10; p++){
                if (k < arr[j]){
                    break;
                }
                else{
                    k -=
                     arr[j];
                    count++;
                }
            }
        }
    }
    printf("%d", count);
    return 0;
}