#include <iostream>
using namespace std;

int main() {
    int numer = 1;
    int denom = 1;
    for (int i = 11; i < 99; i++) {
        for (int j = i + 1; j < 100; j++) {
            double storeI = i;
            double storeJ = j;
            double storeIMod = i % 10;
            double storeJMod = j % 10;
            double check = storeI / storeJ;
            double negDiag = (i / 10) / storeJMod;
            double posDiag = storeIMod / (j / 10);
            
            if (check == negDiag and ((i % 10) == (j / 10))) {
                numer *= i / 10;
                denom *= j % 10;
            }
            if (check == posDiag and ((i / 10) == (j % 10))) {
                numer *= i % 10;
                denom *= j / 10;
            }
        }
    }
    for (int k = 2; k < denom; k++) {
        while (numer % k == 0 and denom % k == 0) {
            numer /= k;
            denom /= k;
        }
    }
    
    cout << denom << "\n";
    return 0;
}
