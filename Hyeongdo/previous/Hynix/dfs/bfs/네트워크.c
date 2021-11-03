#include<stdio.h>
int computers[3][3] = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}}	;
int visited[200][200];
void dfs(int start, int end, int n){
    visited[start][end] = 1;
    int start1, end1;
    if (visited[start-1][end] == 0){
        start1 = start-1;
        end1 = end;
        if(computers[start1][end1] == 1){
            dfs(start1, end1, n);
        }
    }
    if (visited[start+1][end] == 0){
        start1 = start+1;
        end1 = end;
        if(computers[start1][end1] == 1){
            dfs(start1, end1, n );
        }
    }
    if (visited[start][end-1] == 0){
        start1 = start;
        end1 = end -1 ;
        if(computers[start1][end1] == 1){
            dfs(start1, end1, n);
        }
    }
    if (visited[start][end+1] == 0){
        start1 = start;
        end1 = end+1;
        if(computers[start1][end1] == 1){
            dfs(start1, end1, n);
        }
    }
}
int main(void){
    int n = 3;
    int count = 0;
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n ;j++){
            if (computers[i][j] == 1 && visited[i][j] == 0){
                count++;
                dfs(i, j, n);
            }
        }
    }
    printf("%d", count);
}