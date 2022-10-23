#include <iostream>
#include <vector>
using namespace std;

int main() {
    int ans = 1;
    int adding = 0;
    int twos = 2;
    vector<int> spiral = {1,1,1,1};
    while (adding < (1001*1001 + 1)) {
        ans += adding;
        adding = spiral[spiral.size() - 4] + twos;
        spiral.push_back(adding);
        twos += 2;
    }
    cout << ans << "\n";
    return 0;
}
