#include <iostream>
#include <vector>
using namespace std;

// Recall that the repeating bit of 1/7, 142857, works, so let's see if there's a number less than 142857 that also works.

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
    //int ans;
    for (int i = 1; i <= 142857; i++) {
        for (int j = 1; j <= 6; j++) {
            bool compare = false;
            int iter = i*j;
            if (convert(i) != convert(iter)) break;
            if (convert(i) == convert(iter) and j == 6) compare = true;
            if (compare) cout << i << "\n";
        }
    }
    
    return 0;
}
