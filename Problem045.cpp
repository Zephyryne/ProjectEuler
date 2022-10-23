#include <iostream>
#include <vector>
using namespace std;

int main() {
    long ans = 0;
    vector<long> tris;
    for (long a = 1; a < 100000; a++) {
        long adding = a*(a+1)/2;
        tris.push_back(adding);
    }
    vector<long> pents;
    for (long b = 1; b < 50000; b++) {
        long adding = b*(3*b-1)/2;
        pents.push_back(adding);
    }
    vector<long> hexas;
    for (long c = 1; c < 30000; c++) {
        long adding = c*(2*c-1);
        hexas.push_back(adding);
    }
    
    bool notfound = true;
    int counter = 143; // H_143 worked
    while (notfound) {
        if (count(tris.begin(), tris.end(), hexas[counter]) and count(pents.begin(), pents.end(), hexas[counter])) {
            ans = hexas[counter];
            notfound = false;
        }
        counter++;
    }

    cout << ans << "\n";
    return 0;
}
