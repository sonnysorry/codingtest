#include<stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int arr[1000]={0};
    for(int i=0; i<n;i++){
        scanf("%d", &arr[i]);
    }
    for(int j = 0; j < n; j++){
        int k = j;
        while(k >= 0 && arr[k] > arr[k+1]){
            int temp = arr[k];
            arr[k] = arr[k+1];
            arr[k+1] = temp;
            k--;
        }
    }
    for (int g = 0; g < n; g++){
        printf("%d ", arr[g]);
    }
}