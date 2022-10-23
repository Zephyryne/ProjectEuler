#include <iostream>
#include <vector>
using namespace std;

int main() {
    long ans = 0;
    for (long a = 1; a < 10; a++) {
        for (long b = 0; b < 10; b++) {
            vector<long> check = {a};
            if (count(check.begin(), check.end(), b)) continue;
            else {
                for (long c = 0; c < 10; c++) {
                    vector<long> check = {a, b};
                    if (count(check.begin(), check.end(), c)) continue;
                    else {
                        for (long d = 0; d < 10; d++) {
                            vector<long> check = {a, b , c};
                            if (count(check.begin(), check.end(), d)) continue;
                            else {
                                for (long e = 0; e < 10; e++) {
                                    vector<long> check = {a, b, c, d};
                                    if (count(check.begin(), check.end(), e)) continue;
                                    else {
                                        for (long f = 0; f < 2; f++) { // must be 5 or 0, see below
                                            vector<long> check = {a, b, c, d, e};
                                            if (count(check.begin(), check.end(), f*5)) continue;
                                            else {
                                                f *= 5;
                                                for (long g = 0; g < 10; g++) {
                                                    vector<long> check = {a, b, c, d, e, f};
                                                    if (count(check.begin(), check.end(), g)) continue;
                                                    else {
                                                        for (long h = 0; h < 10; h++) {
                                                            vector<long> check = {a, b, c, d, e, f, g};
                                                            if (count(check.begin(), check.end(), h)) continue;
                                                            else {
                                                                for (long i = 0; i < 10; i++) {
                                                                    vector<long> check = {a, b, c, d, e, f, g, h};
                                                                    if (count(check.begin(), check.end(), i)) continue;
                                                                    for (long j = 0; j < 10; j++) {
                                                                        vector<long> check = {a, b, c, d, e, f, g, h, i};
                                                                        if (count(check.begin(), check.end(), j)) continue;
                                                                        else {
                                                                            long num = j + i * 10 + h * 100 + g * 1000 + f * 10000 + e * 100000 + d * 1000000 + c * 10000000 + b * 100000000 + a * 1000000000;
                                                                            int byTwo = (b * 100 + c * 10 + d) % 2;
                                                                            int byThr = (c * 100 + d * 10 + e) % 3;
                                                                            //int byFiv = (d * 100 + e * 10 + f) % 5; not needed, f = 0 or 5
                                                                            int bySev = (e * 100 + f * 10 + g) % 7;
                                                                            int byEle = (f * 100 + g * 10 + h) % 11;
                                                                            int byThi = (g * 100 + h * 10 + i) % 13;
                                                                            int bySet = (h * 100 + i * 10 + j) % 17;
                                                                            if (byTwo == 0 and byThr == 0 and bySev == 0 and byEle == 0 and byThi == 0 and bySet == 0) {
                                                                                ans += num;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    cout << ans << "\n";
    return 0;
}
