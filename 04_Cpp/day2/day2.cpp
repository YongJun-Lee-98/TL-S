#include <iostream>
#include <iomanip>
using namespace std;

int sum_func(void){
    int A, B;
    cin >> A >> B;
    cout << A + B << endl;
    return 0;
}

int miner_func(void){
    int A, B;
    cin >> A >> B;
    cout << A - B << endl;
    return 0;
}

int x_func(void){
    int A, B;
    cin >> A >> B;
    cout << A * B << endl;
    return 0;
}

int dis_func(void){
    int A, B;
    double result;
    cin >> A >> B;
    result = (double)A/B;
    cout << fixed << setprecision(9) << result << endl;
    return 0;
}
int main(void){
    dis_func();
}