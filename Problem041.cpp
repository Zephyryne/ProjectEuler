#include <iostream>
#include <vector>
using namespace std;

bool isPrime(int num) {
    if (num < 2) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (int i = 3; (i*i) <= num; i += 2){
        if (num % i == 0) return false;
    }
    return true;
}

vector<int> convert(int num) {
    vector<int> digits = {};
    do {
        digits.push_back(num % 10);
        num /= 10;
    } while (num > 0);
    sort(digits.begin(), digits.end());
    return digits;
}

int main() {
    int ans = 0;
    vector<int> check = {1,2,3,4,5,6,7};
    for (int i = 1234567; i < 7654322; i++) if (convert(i) == check and isPrime(i)) ans = i;
    cout << ans << "\n";
    return 0;
}


/*
 What is prime?
 1 digit : sum of digits = 1
 2 digit : sum of digits = 3
 3 digit : sum of digits = 6
 4 digit : sum of digits = 10
 5 digit : sum of digits = 15
 6 digit : sum of digits = 21
 7 digit : sum of digits = 28
 8 digit : sum of digits = 36
 9 digit : sum of digits = 45
 
 1 is not prime, so only 4-digit and 7-digit pandigital numbers can be prime.
 Therefore, set limits between 1234567 and 7654321.
 */
