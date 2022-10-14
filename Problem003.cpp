#include <iostream>
using namespace std;

int main() {
    int64_t num = 600851475143;
    int ans = 0;
    for (int count = 2; num != 1; count++) {
        while (num % count == 0) {
            num /= count;
            ans = count;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
