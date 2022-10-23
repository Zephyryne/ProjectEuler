#include <iostream>
#include <vector>
using namespace std;

bool isPrime(long num) {
    if (num < 2) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (int i = 3; (i*i) <= num; i += 2){
        if (num % i == 0) return false;
    }
    return true;
}

vector<int> convert(long num) {
    vector<int> digits = {};
    do {
        digits.push_back(num % 10);
        num /= 10;
    } while (num > 0);
    sort(digits.begin(), digits.end());
    return digits;
}

int main() {
    long ans = 0;
    
    for (long i = 1000; i < 10000; i++) {
        for (long j = 1; j < 4500; j++) {
            if (isPrime(i) and isPrime(i+j) and isPrime(i+2*j) and convert(i) == convert(i+j) and convert(i) == convert(i+2*j)) {
                ans = i * 100000000 + (i+j) * 10000 + (i+2*j);
            }
        }
    }
    
    cout << ans << "\n";
    return 0;
}
