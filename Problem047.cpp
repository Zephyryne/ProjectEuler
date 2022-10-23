#include <iostream>
#include <vector>
using namespace std;

int countPrimes(int num) {
    int primes = 0;
    int div = 2;
    do {
        bool inc = false;
        while (num % div == 0) {
            inc = true;
            num /= div;
        }
        if (inc) primes++;
        div++;
    } while (num > 1);
    
    return primes;
}

int main() {
    int consec = 0;
    int check = 1;
    while (consec < 4) {
        if (countPrimes(check) == 4) {
            consec++;
        }
        else {
            consec = 0;
        }
        check++;
    }
    int ans = check - 4;
    
    cout << ans << "\n";
    return 0;
}
