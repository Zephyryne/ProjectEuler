#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    long ans = 0;
    long primes[] = {2,3,5,7,11,13,17};
    long perms[] = {0,1,2,3,4,5,6,7,8,9};
    sort(perms, perms+10);
    
    do {
        bool valid = true;
        for (int i = 0; i < 7; i++) {
            if ((perms[i+1] * 100 + perms[i+2] * 10 + perms[i+3]) % primes[i] != 0) valid = false;
        }
        if (valid) {
            for (int j = 0; j < 10; j++) {
                ans += perms[j] * pow(10,9-j);
            }
        }
    } while (next_permutation(perms, perms+10));
    
    cout << ans << "\n";
    return 0;
}
