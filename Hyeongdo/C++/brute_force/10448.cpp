// 유레카 이론

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n, temp;
    cin >> n;
    vector <int> arr(1000);
    for (int i = 0; i < n; i++){
        cin >> temp;
        arr.push_back(temp);
    }
    vector <int> arr2(1000);
    arr2[1] = 1;
    for (int j = 2; j < 1001; j++){
        arr2[j] = arr2[j-1] + j;
    }
    for (int i = 0; i < n; i++){
        int count = 1;
        for (int k = 1; k < 1001; k++ ){
            if (arr[i] == arr2[k]){
                count -= 1;
                break;
            }
        }
        if (count == 1){
            cout << 0 << endl;
        }
        else{
            cout << 1 << endl;
        }
    }
}