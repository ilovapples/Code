#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

char playing = 'y';

void clear() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
};

string slots[9] = {
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
};

void printBoard() {
    cout << "\n\033[1mTic Tac Toe\033[0m\n\n";
    cout << "_____________\n";
    cout << "|_" << slots[0] << "_|_" << slots[1] << "_|_" << slots[2] << "_|\n";
    cout << "|_" << slots[3] << "_|_" << slots[4] << "_|_" << slots[5] << "_|\n";
    cout << "|_" << slots[6] << "_|_" << slots[7] << "_|_" << slots[8] << "_|\n";
}


int main() {
    clear();
    printBoard();
    playing = 'y';
    int turn = 1;
    string X_or_O;

    if (turn % 2 == 0) {
        X_or_O = "O";
    } else {
        X_or_O = "X";
    }
    string inputstr;
    int input;
    while (playing == 'y') {
        cout << "Slot: ";
        cin >> inputstr;
        // check if the input is 'r', for 'reset'  
        if (inputstr == "r") {
            for (int i; i < 9; i++) {
                slots[i] = "_";
            };
            turn = 0;
            X_or_O = "X";
            clear();
            printBoard();
            continue;
        }
        
        input = stoi(inputstr);
        
        if (slots[input-1] != "_") {
            clear();
            printBoard();
            cout << "Invalid.\n";
            continue;
        } else {
            slots[input-1] = X_or_O;
            turn++;
            clear();
            printBoard();
        }
        // check if its a win

        // check for top row. (1-3)
        if (slots[0] == slots[1] && slots[1] == slots[2] && slots[2] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        //check for middle row
        } else if (slots[3] == slots[4] && slots[4] == slots[5] && slots[5] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        //check for bottom row
        } else if (slots[6] == slots[7] && slots[7] == slots[8] && slots[8] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        // check for column one (1, 4, 7)
        } else if (slots[0] == slots[3] && slots[3] == slots[6] && slots[6] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        // check for middle column (2, 5, 8) 
        } else if (slots[1] == slots[4] && slots[4] == slots[7] && slots[7] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        // far right column
        } else if (slots[2] == slots[5] && slots[5] == slots[8] && slots[8] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        // top left to bottom right: diagonal
        } else if (slots[0] == slots[4] && slots[4] == slots[8] && slots[8] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        // top right to bottom left: diagonal
        } else if (slots[2] == slots[4] && slots[4] == slots[6] && slots[6] != "_") {
            cout << "\n" << X_or_O << " won!\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                turn = 0;
                main();
                return 0;
            } else {
                return 0;
            };
        }
        // check if its a tie
        if (
            slots[0] != "_" &&
            slots[1] != "_" &&
            slots[2] != "_" &&
            slots[3] != "_" &&
            slots[4] != "_" &&
            slots[5] != "_" &&
            slots[6] != "_" &&
            slots[7] != "_" &&
            slots[8] != "_") {
            cout << "\nIt's a tie! The game is over.\n";
            cout << "Play again? (Y/n): ";
            cin >> playing;
            if (playing == 'y' || playing == 'Y') {
                for (int i; i < 9; i++) {
                    slots[i] = "_";
                };
                main();
            } else {
                return 0;
            };
        };
        if (turn % 2 == 0) {
            X_or_O = "O";
        }
        else {
            X_or_O = "X";
        };
    };
    return 0;
}