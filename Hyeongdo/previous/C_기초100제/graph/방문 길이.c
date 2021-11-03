#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int row [10][11];
int col [11][10];
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* dirs) {
    int length = strlen(dirs);
    int x = 5;
    int y = 5;
    int count = 0;
    if (dirs[0] == "U"){
        x--;
        row[x][y] = 1;
        count++;
        }
    else if (dirs[0] == "D"){
        row[x][y] = 1;
        count++;
        }
    else if (dirs[0] == "R"){
        col[x][y] = 1;
        count++;
    }
    else if (dirs[0] == "L"){
        y--;
        col[x][y] = 1;
        count++;
    }
    for (int i = 1; i < length;i++){
        if (x < 0 || x > 10 || y <0 || y > 10){
            continue;
        }
        if (dirs[i] == "U" && row[x][y+1] == 0){
            x--;
            row[x][y] = 1;
            count++;
        }
        else if (dirs[i] == "D" && row[x][y-1] == 0){
            x++;
            row[x][y] = 1;
            count++;
        }
        else if (dirs[i] == "R" && col[x+1][y] == 0){
            y++;
            col[x][y] = 1;
            count++;
        }
        else if (dirs[i] == "L" && col[x-1][y] == 0){
            y--;
            col[x][y] = 1;
            count++;
        }
    }
    int answer = count;
    return answer;
}