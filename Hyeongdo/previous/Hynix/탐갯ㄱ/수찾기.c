#include<stdio.h>

int main(void){
    int n, m;
    int answer = 1;
    scanf("%d", &n);
    int A[100000];
    int B[100000];
    for(int i = 0; i < n; i++){
        scanf("%d", &A[i]);
    }
    scanf("%d", &m);
    for(int k = 0; k < m; k++){
        scanf("%d", &B[k]);
    }
    for (int k = 0; k < m; k++){
        int count = 0;
        for(int i = 0; i < n; i++){
            if (B[k] == A[i]){
                printf("%d \n", answer);
                break;
            }
            else{
                count ++;
            }
        }
        if (count == n){
            printf("%d \n", 0);
        }
    }
    return 0;
}