#include <iostream>
#include "dblLinkedList.h"
#include "insertionSort.h"

using namespace std;

void arrayMenu();
void dLnkLstMenu();

int main() {
    int menu = 0;
    do {
        cout << "This is the test menu for assignment one. Please type:\n"
            << "1. for the array menu\n"
            << "2. for the doubly linked list menu\n"
            << "3. to exit\n"
            << "Response: ";
        cin >> menu;
        switch (menu) {
            case 1:
                arrayMenu();
                break;
            case 2:
                dLnkLstMenu();
                break;
            case 3:
                cout << "Shutting down... Thank you. Have a wonderful day!\n";
                break;
            default:
                cout << "Invalid response. Please try again.\n";
                break;
        }
    } while (menu != 3);
    return 0;
}

void arrayMenu() {
    int choice = 0;
    inSortArray myArray;
    do {
        cout << "Arrays, please make your selection and hit enter:\n"
            << "1. Initiate the default array\n"
            << "2. Set up a customized array\n"
            << "3. Sort the initiated array using the insertion sort algorithm\n"
            << "4. Display the array\n"
            << "5. Return to the main menu\n"
            << "Response: ";
        cin >> choice;
        switch (choice) {
            case 1:
                myArray.defaultArray();
                myArray.dsplyArray();
                break;
            case 2: {
                int size;
                cout << "Set the size of the array: ";
                cin >> size;
                myArray.customArray(size);
                myArray.dsplyArray();
                break;
            }
            case 3:
                myArray.insertionSort();
                myArray.dsplyArray();
                break;
            case 4:
                myArray.dsplyArray();
                break;
            case 5:
                cout << "Going back to the main menu...\n";
                break;
            default:
                cout << "Invalid response. Please try again.\n";
                break;
        }
    } while (choice != 5);
}

void dLnkLstMenu() {
    int choice = 0;
    dblLnkLst myDblLL;
    do {
        cout << "Doubly linked lists, please make your selection and hit enter:\n"
            << "1. Insert a value on the left\n"
            << "2. Insert a value on the right\n"
            << "3. Insert a value at a certain position\n"
            << "4. Delete a value at a certain position\n"
            << "5. Organize the linked list with an insertion sort algorithm\n"
            << "6. Display the current linked list\n"
            << "7. Return to the main menu\n"
            << "Response: ";
        cin >> choice;
        switch (choice) {
            case 1: {
                int value;
                cout << "Please type in an integer for the element value: ";
                cin >> value;
                myDblLL.headInsert(value);
                myDblLL.dsplyLnkLst();
                break;
            }
            case 2: {
                int value;
                cout << "Please type in an integer for the element value: ";
                cin >> value;
                myDblLL.tailInsert(value);
                myDblLL.dsplyLnkLst();
                break;
            }
            case 3: {
                int value, position;
                cout << "Please type in an integer for the element value: ";
                cin >> value;
                cout << "Please give a positive integer for the insert position: ";
                cin >> position;
                myDblLL.posInsert(value, position);
                myDblLL.dsplyLnkLst();
                break;
            }
            case 4: {
                int position;
                cout << "Please give a positive integer for the position to delete: ";
                cin >> position;
                myDblLL.deleteNode(position);
                myDblLL.dsplyLnkLst();
                break;
            }
            case 5:
                myDblLL.dblLLInsertSort();
                myDblLL.dsplyLnkLst();
                break;
            case 6:
                myDblLL.dsplyLnkLst();
                break;
            case 7:
                cout << "Going back to the main menu...\n";
                break;
            default:
                cout << "Invalid response. Please try again.\n";
                break;
        }
    } while (choice != 7);
}
