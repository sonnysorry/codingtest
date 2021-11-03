#include<stdio.h>

int main(void){
    int brown = 24;
    int yellow = 24;

    int answer[2];
    int n = (brown-4)/2;
    for(int i=1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if (i*j == yellow && i+j==n){
                answer[0] = i+2;
                answer[1] = j+2;
            }
        }
    }
    for(int k = 0; k < 2; k++){
        printf("%d", answer[k]);
    }
}