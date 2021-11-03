#include<stdio.h>
#include<algorithm>

bool compare(int a, int b){
    return a < b;
}
int main(void){
    int n;
    scanf("%d", &n);
    int arr[100000][2];
    for(int i = 0; i < n; i++){
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }
    

}