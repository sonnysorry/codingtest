// 일곱 난쟁이

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int temp;
    int temp_num;
    int sum_num = 0;
    vector<int> arr(9);
    for (int i = 0; i < 9; i++){
        cin >> temp;
        arr[i] = temp;
        sum_num += temp;
    }
    sort(arr.begin(), arr.end());
    // 배열합 체크해야함.
    // int sum_num = accumulate(arr.begin(), arr.end(), 0);
    int max_i, max_j = 99999;
    for (int i = 0; i < 8; i++){
        for (int j = i+1; j < 9; j++){
            temp_num = sum_num - arr[i] - arr[j];
            if(temp_num == 100){
                max_i = i;
                max_j = j;
            }
        }
    }
    for(int k = 0; k < 9; k++){
        if (k== max_i || k == max_j)
            continue;
        cout << arr[k] << endl;
    }

}