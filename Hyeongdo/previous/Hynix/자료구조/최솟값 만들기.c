#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int static upCompare(const void* first, const void* second){
    if (*(int*)first > *(int*)second){
        return 1;
    }
    else if (*(int*)first < *(int*)second){
        return -1;
    }
    else{
        return 0;
    }
}

int static downCompare(const void* first, const void* second){
    if (*(int*)first < *(int*)second){
        return 1;
    }
    else if(*(int*)first > *(int*)second){
        return -1;
    }
    else{
        return 0;
    }
}
// A_len은 배열 A의 길이입니다.
// B_len은 배열 B의 길이입니다.
int solution(int A[], size_t A_len, int B[], size_t B_len) {
    int answer = 0;
    qsort(A,A_len,sizeof(int), upCompare);
    qsort(B,B_len,sizeof(int), downCompare);
    for(int i = 0; i < A_len; i++){
        answer += A[i]*B[i];
    }
    return answer;
}