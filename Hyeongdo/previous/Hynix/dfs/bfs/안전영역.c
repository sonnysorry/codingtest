#include<stdio.h>
int arr[100][100];
int visit[100];
int count;
void dfs(int start, int n){
    visit[start] = 1;
    count++;
    for(int k = 1; k<=n; k++){
        if(arr[start][k] == 1 && visit[k] == 0){
            dfs(k, n);
        }
    }
}
int main(void){
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    int array[100] = {0, };
    for (int p = 0; p < 100; p++){
        array[p] = dfs(p, n);
    }
    int max = 0;
    for (int p = 0; p < 100; p++){
        if (max < array[p]) max = array[p]; 
    }
    printf("%d", max);
}