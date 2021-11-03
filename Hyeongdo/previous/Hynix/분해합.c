#include<stdio.h>

int main(void){
    int a, n;
    scanf("%d", &a);
    n = a;
    int count = 0;
    while(n!=0){
        n /= 10;
        count++;
    }
    int tmp;
    tmp = count * 9;    
    for(int i = a - tmp; i < a; i++){
        int list[10]={0};
        for(int k = 0; k < count; k++){
            list[k] = i % (10^k);
        }
        int sum, temp = 0;
        for(int j = 0; j < count; j++){
            sum += list[j];
            temp += (10^j) * list[j];
            printf("%d %d", sum, temp);
        }
        sum += temp;
        if(sum == a){
            printf("%d", i);
        }
    }
}