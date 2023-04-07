#include <iostream>
#include <cmath>
#include <time.h>
#include <cstdlib>
#include <algorithm>
using namespace std;

// int randdataset(int length, int min_, int max_) {
//     srand(time(0));
//     int x[] = {};
//     for (int i; i < length; i++) {
//         x[i] = rand() % (max_ - min_);
//     }
// }

int dataset[4] = {15, 16, 17, 18};

double length() {
    return sizeof(dataset) / sizeof(int);
}

double sum(int data[]) {
    double total = 0;
    for (int i = 0; i < length(); i++) {
        total += dataset[i];
    }
    return total;
}

double mean(int data[]) {
    return sum(data) / length();
}

int median(int data[]) {
    // copy the array
    int copy[] = {};
    for (int i; i < length(); i++) {
        copy[i] = data[i];
    };
    size_t len = sizeof(copy) / sizeof(copy[0]);
    sort(copy, copy + len);

    for (int i; i < length(); i++) {
        cout << endl << copy[i];
    };
    return 0;
}


int main() {
    // int dataset[4] = {15, 16, 17, 18};
    double themean = mean(dataset);
    cout << "Mean: " << themean << endl;
    cout << "Sum: " << sum(dataset) << endl;
    cout << "Length: " << length() << endl;
    median(dataset);
    return 0;
}