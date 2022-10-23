#include <iostream>
using namespace std;

bool isPrime(int num) {
    if (num < 2) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (int i = 3; (i*i) <= num; i += 2){
        if (num % i == 0) return false;
    }
    return true;
}

int remove_first_digit(int num) {
    if (num < 10) return 0;
    else return (num % 10) + remove_first_digit(num/10) * 10 ;
}

int main() {
    int ans = 0;
    int count = 0;
    int i = 11;
    while (count < 11) {
        if (isPrime(i)) {
            int rightward = i;
            int leftward = i;
            while (isPrime(rightward) and isPrime(leftward) and (rightward > 9 or leftward > 9)) {
                if (rightward > 9) rightward /= 10;
                if (leftward > 9) leftward = remove_first_digit(leftward);
            }
            if (isPrime(rightward) and isPrime(leftward)) {
                ans += i;
                count++;
            }
        }
        i++;
    }
    
    cout << ans << "\n";
    return 0;
}
