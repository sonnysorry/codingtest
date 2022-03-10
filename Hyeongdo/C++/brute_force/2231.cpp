// 분해합

#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    int f_answer = 0;
    for (int i = 0; i < n; i++){
        string a = to_string(i);
        int answer = 0;
        for (int j = 0; j < a.length(); j++){
            int b = a[j] - '0';
            answer += b;
        }

        if (i + answer == n){
            f_answer = i;
            break;
        }
           
    }
    cout << f_answer;
}

