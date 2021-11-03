#include<stdio.h>
int arr[25][25] = {0, };
int visited[25][25] = {0, };
int comp[25];
int check[25*25/2];
int index;
void dfs(int x, int y, int n){
    int x1, y1;
    check[index-1]++;
    if(arr[x-1][y] == 1){
        x1 = x-1;
        y1 = y;
        if(visited[x1][y1] == 0){
            dfs(x1, y, n);
        }
    }
    if(arr[x+1][y] == 1){
        x1 = x+1;
        y1 = y;
        if(visited[x1][y1] == 0){
            dfs(x1, y1, n);
        }
    }
    if(arr[x][y-1] == 1){
        x1 = x;
        y1 = y-1;
        if(visited[x1][y1] == 0){
            dfs(x1, y, n);
        }
    }
    if(arr[x][y+1] == 1){
        x1 = x;
        y1 = y+1;
        if(visited[x1][y1] == 0){
            dfs(x1, y, n);
        }
    }
}

int main(void){
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            scanf("%d", &arr[i][j]);
            if(arr[i][j] == 0){
                visited[i][j] = 1;
            }
        }
    }
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(visited[i][j] == 0){
                index++;
                dfs(i,j, n);
            }
        }
    }
    printf("%d", index);
}