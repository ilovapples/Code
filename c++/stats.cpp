#include <iostream>
#include <cmath>
#include <time.h>
#include <cstdlib>
using namespace std;

// int randdataset(int length, int min_, int max_) {
//     srand(time(0));
//     int x[] = {};
//     for (int i; i < length; i++) {
//         x[i] = rand() % (max_ - min_);
//     }
// }

int dataset[4] = {15, 16, 17, 18};

int length() {
    // the four is the size of an integer in bytes, not the length of the array
    return sizeof(dataset) / sizeof(int);
}

int sum(int data[]) {
    int total = 0;
    for (int i = 0; i < length(); i++) {
        total += dataset[i];
    }
    return total;
}

double mean(int data[]) {
    return sum(data)/length();
}


int main() {
    // int dataset[4] = {15, 16, 17, 18};
    cout << "Mean: " << mean(dataset) << endl;
    cout << "Sum: " << sum(dataset) << endl;
    cout << "Length: " << length() << endl;
    return 0;
}