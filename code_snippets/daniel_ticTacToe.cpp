// Below is the oringal code from the ticTacToe.cpp file.
// ***************************************************************************************************************
// ***************************************************************************************************************
// ***************************************************************************************************************
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdlib> 
#include <limits> 
using namespace std; 

const int NINE = 9; // Number of cells in the board

struct players {
	string symbol; // Either X or O depending on player
	int score; // How many wins a player has
	players () {
		symbol = "";
		score = 0;
	}
};

bool checkCellChoice(int choice) {
	bool temp = true;
	if (cin.fail()) { // Checks for non number inputs
		cout << "You can enter numbers only!" << endl;
		cin.clear(); // Clears and ignores input
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		temp = false;
	}
	else if (choice < 1 || choice > NINE) { // Checks for wrong #
		cout << "Your selection must be between 1 and 9" << endl;  
		cin.clear(); // Clears and ignores input
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		temp = false;
	}
		return temp;
}

bool validateCell(players player, string board[], int choice, bool bot,
bool debugMode){
	bool temp = true;
	if (!bot) { // If its not the computer
		if (board[choice - 1] != to_string(choice)) {
			cout << "This slot is already selected" << endl;
			if (debugMode) {
				cout << "\033[31m" << "Checking the board for a "s + 
				"winning sequence\n\033[30m";
			}
			outputBoard(board);
			cout << "Player " + player.symbol + ", Make a selection: \n";
			if (debugMode) {
				cout << "\033[31mPlay function called.\n\033[30m";
			}
			temp = false;
		}
	}
	else { // If its the computer
		if (board[choice] == player.symbol || board[choice] == "X") {
			temp = false;
		}
	}
	return temp;
}

void outputBoard (string board[]) {
	cout << " -----------\n| "; // Top of board
	for (int i = 0; i < NINE; i++) {
		if (i % 3 == 0 && i != 0) {
			 cout << endl << " -----------\n| "; // line endings
		}
		cout << board[i] << " | "; // Outputs cells
	}
	cout << "\n -----------\n"; // Bottom of board
} 

void selectCell(players player, string board[], int choice, bool bot,
bool debugMode) {
	int x = 0, y = 0;
	if (!bot) { // If its a player
		cout << "Player " + player.symbol +  ", Make a selection: \n"; 
		if (debugMode) {
		cout << "\033[31mPlay function called.\n\033[30m";
		}
		cin >> choice;
		while (!checkCellChoice(choice)) { // checks for right pick
			cin >> choice;
		} // Checks to see if cell is already taken
		while (!validateCell(player, board, choice, bot, debugMode)){
			cin >> choice;
		}
		board[choice - 1] = player.symbol; // Sets cell as taken
	}
	else { // If its the computer
			x = (rand() % 3) ;
        	y = (rand() % 3) ;
			if (debugMode) {
				cout << "\033[31mrow: " << x << " , col: " << y << 
				"\033[30m\n";
			}
			for (int i = 0, k = 0; i < 3; i++){
				bool right = false;
				for (int j = 0; j < 3; j++, k++) {
					if (x == i && y == j) {
						right = true;
						choice = k;
						break;
					}
				}
				if (right) { break; }
			}
		while (!validateCell(player, board, choice, bot, debugMode)) {
			if (debugMode) {
				cout << "\033[31mCell is already selected!\nChanging selection.\n\033[30m\n";
			}
			x = (rand() % 3) ;
        	y = (rand() % 3) ;
			for (int i = 0, k = 0; i < 3; i++){
				bool right = false;
				for (int j = 0; j < 3; j++, k++) {
					if (x == i && y == j) {
						right = true;
						choice = k;
						break;
					}
				}
				if (right) { break; }
			}
		}
			if (debugMode) {
				cout << "\033[31mPlaying in row: " << x << ", col: "
				<< y << "\033[30m\n";
			}
			board[choice] = player.symbol;
	}
}

// ***************************************************************************************************************
// ***************************************************************************************************************
// ***************************************************************************************************************
// Below is the refactored code from the original ticTacToe.cpp file.
// ***************************************************************************************************************
// ***************************************************************************************************************
// ***************************************************************************************************************

/* checked in seperate file that these changes do in fact work, 
 	but since the file is too large, I will not include it here. */
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdlib> 
#include <limits> 
using namespace std; 

const int NINE = 9; // Number of cells in the board

struct players {
	string symbol; // Either X or O depending on player
	int score; // How many wins a player has
	players() {
		symbol = "";
		score = 0;
	}
};

bool checkCellChoice(int choice) {
	if (cin.fail() || choice < 1 || choice > NINE) {
		cout << "Invalid input! Please enter a number between 1 and 9." << endl;
		cin.clear();
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		return false;
	}
	return true;
}

bool validateCell(players player, string board[], int choice, bool bot, bool debugMode) {
	if (!bot) { // If it's not the computer
		if (board[choice - 1] != to_string(choice)) {
			cout << "This slot is already selected" << endl;
			if (debugMode) {
				cout << "\033[31mChecking the board for a winning sequence\n\033[30m";
				outputBoard(board);
				cout << "Player " + player.symbol + ", Make a selection: \n";
				cout << "\033[31mPlay function called.\n\033[30m";
			}
			return false;
		}
	}
	else { // If it's the computer
		if (board[choice] == player.symbol || board[choice] == "X") {
			if (debugMode) {
				cout << "\033[31mCell is already selected!\nChanging selection.\n\033[30m\n";
			}
			return false;
		}
	}
	return true;
}

void outputBoard(string board[]) {
	cout << " -----------\n| "; // Top of board
	for (int i = 0; i < NINE; i++) {
		if (i % 3 == 0 && i != 0) {
			cout << endl << " -----------\n| "; // line endings
		}
		cout << board[i] << " | "; // Outputs cells
	}
	cout << "\n -----------\n"; // Bottom of board
}

void selectCell(players player, string board[], int choice, bool bot, bool debugMode) {
	int x = 0, y = 0;
	if (!bot) { // If it's a player
		cout << "Player " + player.symbol + ", Make a selection: \n";
		if (debugMode) {
			cout << "\033[31mPlay function called.\n\033[30m";
		}
		cin >> choice;
		while (!checkCellChoice(choice) || !validateCell(player, board, choice, bot, debugMode)) {
			cin >> choice;
		}
		board[choice - 1] = player.symbol; // Sets cell as taken
	}
	else { // If it's the computer
		x = rand() % 3;
		y = rand() % 3;
		if (debugMode) {
			cout << "\033[31mrow: " << x << " , col: " << y << "\033[30m\n";
		}
		choice = x * 3 + y; // Calculate the cell index
		while (!validateCell(player, board, choice, bot, debugMode)) {
			if (debugMode) {
				cout << "\033[31mCell is already selected!\nChanging selection.\n\033[30m\n";
			}
			x = rand() % 3;
			y = rand() % 3;
			choice = x * 3 + y; // Calculate the cell index
		}
		if (debugMode) {
			cout << "\033[31mPlaying in row: " << x << ", col: " << y << "\033[30m\n";
		}
		board[choice] = player.symbol;
	}
}

// ***************************************************************************************************************
// ***************************************************************************************************************
// ***************************************************************************************************************
