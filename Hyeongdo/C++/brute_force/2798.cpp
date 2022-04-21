// 블랙잭

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
bool compare(int j, int k){
    return k < j;
}

int main(){
    int a, b;
    int temp = 0;
    vector<int> arr(100);
    cin >> a >> b;
    for (int i = 0; i < a; i++){
        cin >> arr[i];
    }
    int answer = 0;
    for (int j = 0; j < a-2; j++){
        for (int p = j+1; p < a-1; p++ ){
            for (int k = p+1; k < a; k++){
                if (arr[j] + arr[p] + arr[k] <= b )
                    temp = max(arr[j] + arr[p] + arr[k], answer);
                    answer = temp;
            }
        }
    }
    cout << answer;
}

