#include<stdio.h>
#include<stdlib.h>

int main(void){
    int brown = 10;
    int yellow = 2;

    int answer[2];
    int n = (brown-4)/2;
    for(int i=1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if (i*j == yellow && i+j==n){
                answer[0] = i;
                answer[1] = j;
            }
        }
    }
    for(int k = 0; k < 2; k++){
        printf("%d", &answer[k]);
    }
}