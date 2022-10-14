#include <iostream>
using namespace std;

int main() {
    long ans = 1;
    for (long i = 2; i < 21; i++) {
        // euclid's algorithm
        long a = i;
        long b = ans;
        while (a != 0) {
            long save_val = a;
            a = b % a;
            b = save_val;
        }
        ans = i * ans / b;
    }
    
    cout << ans << "\n";
    return 0;
}

// Note: Using int instead of long results in an incorrect answer.
