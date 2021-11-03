#include<stdio.h>

int main(void){
    int n, m, c;
    int max, sum = 0;
    scanf("%d %d", &n, &m);
    int tmp[100] = {0, };
    for(int i = 0; i < n; i++){
        scanf("%d", &c);
        tmp[i] = c;
    }
    for (int j = 0; j < n; j++){
        for (int k = j+1; k < n; k++){
            for (int p = k+1; p < n; p++){
                sum = tmp[j] + tmp[k] + tmp[p];
                if(sum <= m && sum > max){
                    max = sum;
                }
            }
        }
    }
    printf("%d", max);
    return 0;
}