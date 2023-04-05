#include <cstdlib>
#include <iostream>
#include <time.h>
using namespace std;

int main() {
    cout << "\n\033[1mNumber Guessing Game\033[0m\n";
    // range
    int lb = 1, ub = 10;
    
    // define rand seed
    srand(time(0));

    // guesses num
    int guesses = 10;

    // preset rand num
    int num = rand() % (ub - lb);

    // run this code 5 times
    for (int i = 0; i < 5; i++) {
        cout << "Guess a number between " << lb << " and " << ub << endl;
        cout << "Guess: ";
        string guessstr;
        cin >> guessstr;
        cout << endl;
        int guess = stoi(guessstr);
        if (num == guess) {
            cout << endl << "You are correct! The number was " << num << endl;
            int num = rand() % (ub - lb);
            ub += 5;
        } else if (num != guess) {
            cout << endl << "You are incorrect. Try again.\n";
            guesses--;
            if (guesses == 0) {
                cout << "You have run out of guesses." << endl;
                return 0;
            }
            cout << "You have " << guesses << " guesses left.\n";
            i--;
        }
    }
    cout << endl;
    return 0;
}