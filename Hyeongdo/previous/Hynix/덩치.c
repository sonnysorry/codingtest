#include<stdio.h>

int main(void){
    int a;
    scanf("%d", &a);
    int x[50];
    int y[50];
    // 리스트에 넣기.
    for(int i = 0; i < a; i++){
        scanf("%d %d", &x[i], &y[i]);
    }
    for (int j = 0; j < a; j++){
        int tmp = 0; 
        for (int k = 0; k < a; k++){
            if (x[j] < x[k] && y[j] < y[k]){
                tmp++;
            }
        }
        printf("%d ", tmp+1);
    }
    return 0;
}