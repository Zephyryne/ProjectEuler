#include <iostream>
using namespace std;

int main() {
    int ans = 0;
    for (int i = 100; i < 1000; i++) {
        for (int j = i + 1; j < 1000; j++) {
            int result = i*j;
            int test_pal = 0;
            while (result != 0) {
                test_pal = test_pal * 10 + result % 10;
                result /= 10;
            }
            // all this instead of just str(i*j)[::-1] smh
            if (i*j == test_pal and i*j > ans) {
                ans = i*j;
            }
        }
    }
    
    cout << ans << "\n";
    return 0;
}
