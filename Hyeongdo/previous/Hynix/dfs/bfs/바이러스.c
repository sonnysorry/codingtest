#include<stdio.h>
int com[101][101] = {0, };
int visit[101] = {0, };
int answer = 0;
void dfs(int start, int p){
    visit[start] = 1;
    answer ++;
    for (int j = 1; j <= p; j++){
        if (com[start][j] == 1 && visit[j] == 0){
            dfs(j, p);
        }
    }
    return;
}

int main(void){
    int n, m, x, y;
    scanf("%d", &n);
    scanf("%d", &m);
    for (int i = 0; i < m; i++){
        scanf("%d %d", &x, &y);
        com[x][y] = 1;
        com[y][x] = 1;
    }
    dfs(1, n);
    printf("%d", answer - 1);
}