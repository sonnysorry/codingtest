#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    char a[100];
    scanf("%s", a);
    int b = (int)strlen(a);
    char z_1[1] = {0}; 
    char z_2[2] = {0, 0};
    if(b%3 == 1){
        b += 1;
        strcat(z_1, a);
    }
    else if(b%3 == 2){
        b += 2;
        strcat(z_2, a);
    }
    for (int i = 0; i < )
}