/*
#include <iostream>
#include <vector>
using namespace std;

int countFactors(long num) {
    int factors = 1;
    int div = 2;
    do {
        int count = 1; // add one to the power of the prime factor
        while (num % div == 0) {
            count++;
            num /= div;
        }
        if (count > 0) factors *= count;
        div++;
    } while (num > 1);
    
    return factors;
}

int main() {
    vector<long> triNums;
    long num = 1;
    long adding = 2;
    for (int i = 0; i < 1000000; i++) {
        triNums.push_back(num);
        num += adding;
        adding++;
    }
    
    long ans = 0;
    for (long j : triNums) {
        if (countFactors(j) > 500) {
            ans = j;
            break;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
*/
