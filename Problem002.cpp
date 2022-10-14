#include <iostream>
using namespace std;

int main() {
    int total = 0;
    int a = 1;
    int b = 1;

    while ((a+b) < 4000000) {
        if ((a+b) % 2 == 0) {
            total += (a+b);
        }
        int save = b;
        b += a;
        a = save;
    }

    cout << total << "\n";
    return 0;
}
