#include <iostream>
#include <vector>
using namespace std;

int main() {
    int ans = 0;
    int diff = 99999;
    vector<int> pents;
    for (int i = 1; i < 2500; i++) {
        int adding = i*(3*i-1)/2;
        pents.push_back(adding);
    }
    
    // omegaslow bashing method -- still under a minute tho
    for (int a = 0; a < pents.size() - 1; a++) {
        for (int b = a+1; b < pents.size(); b++) {
            int add = pents[b] + pents[a];
            int sub = pents[b] - pents[a];
            if (count(pents.begin(), pents.end(), add) and count(pents.begin(), pents.end(), sub)) {
                if ((b - a) < diff) {
                    diff = (b - a);
                    ans = pents[b] - pents[a];
                }
            }
        }
    }
    

    cout << ans << "\n";
    return 0;
}

/*
 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
    4,  7, 10, 13, 16, 19, 22,  25,  28, ...
 n(3n+1)/2 = n(3n) + n / 2
 (n+1)(3(n+1)-1)/2 = (n+1)(3n+2)/2 = n(3n+2)+3n+2 / 2 = n(3n) + 5n+2 / 2
 (n+2)(3(n+2)-1)/2 = (n+2)(3n+5)/2 = n(3n+5)+6n+10 / 2 = n(3n) + 11n+10 / 2
 
 Note that the difference is 3n + 4.
 */
