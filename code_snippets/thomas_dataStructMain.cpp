/// ##################################################################
/// Name: Thomas Bryant
/// NSHE ID: 2000193948
/// Course: CS302
/// Section: 1003
/// Semester: SPRING2023
/// Assignment: Assignment #1 Revised, Program Test File
/// Description: This program will first show a doubly linked list
/// including functions to insert, delete, and implement a dummy node.
/// This also includes the insertion sort for a doubly linked list.
/// Secondly, it will show the insertion sort on an array.
/// ##################################################################

#include <string>
#include <iostream>
#include "dblLinkedList.h"
#include "insertionSort.h"
using namespace std;

void arrayMenu();
void dLnkLstMenu();

int main(){
    int menu = 0;
    while(menu != 3){
        cout<<"This is the test menu for assignment one. Please type '1'\n"
            <<"for the array menu, Type '2' for the doubly linked list\n"
            <<"menu. To exit, type '3' and the program will shut down."
            <<endl;
        cout<<"Response: ";
        cin>>menu;
        cin.clear();
        cin.ignore();
        while(menu < 1 || menu > 3 || cin.fail()){

                cout<<"Invalid reponse, please try again. Please type"
                    <<" '1'\nfor the array menu, Type '2' for the "
                    <<"doubly linked list\nmenu. To exit, type '3' and"
                    <<"the program will shut down."<<endl;
                cout<<"Response: ";
                cin>>menu;
                cin.clear();
                cin.ignore();
        }
        if(menu == 1){
            arrayMenu();
        }
        if(menu == 2){
            dLnkLstMenu();
        }
        if(menu == 3){
            cout<<"Shutting down... Thank you."
                <<" Have a wonderful day!"<<endl;
        }
    }
    return 0;
} // main

void arrayMenu(){
    int i = 0;
    int j = 0;
    inSortArray myArray;
    cout<<"Arrays, please make your selection and hit enter. pick\n"
        <<"'1' to initiate the default array, '2' to set up a\n"
        <<"customized array, '3' to sort your initiated array using\n"
        <<"the insertion sort algorithm, '4' to display the\n"
        <<"array, and '5' to return to the main menu."<<endl;
    while(i != 5){
    cout<<"Response: ";
    cin>>i;
        while(i < 1 || i > 5){
            cout<<"Invalid reponse, please try again."<<endl;
            cout<<"Selection: ";
            cin>>i;
            cin.clear();
            cin.ignore();
        }
        if(i == 1){
            myArray.defaultArray();
            myArray.dsplyArray();
        }
        if(i == 2){
            cout<<"Set the size of array. Size: ";
            cin>>j;
            cin.clear();
            cin.ignore();
            myArray.customArray(j);
            myArray.dsplyArray();
        }
        if(i == 3){
            myArray.insertionSort();
            myArray.dsplyArray();
        }
        if(i == 4){
            myArray.dsplyArray();
        }
        if(i == 5){
            cout<<"Going back to main menu..."<<endl;
        }
    }
}

void dLnkLstMenu(){
    int i = 0;
    int j = 0;
    int k = 0;
    dblLnkLst myDblLL;
    cout<<"Doubly linked lists, please make your selection and hit\n"
        <<"enter. Pick '1' to insert a value on the left, '2' to\n"
        <<"insert a value on the right, '3' to insert a value at a\n"
        <<"certain position, '4' to delete a value at a certain\n"
        <<"position, '5' to organize the linked list with an\n"
        <<"insertion sort algorithm, '6' to display the current\n"
        <<"linked list, and '7' to return to the main menu."<<endl;
    while(i != 7){
        cout<<"Response: ";
        cin>>i;
        cin.clear();
        cin.ignore();
        while(i < 1 || i > 7){
            cout<<"Invalid reponse, please try again."<<endl;
            cout<<"Selection: ";
            cin>>i;
            cin.clear();
            cin.ignore();
        }
        if(i == 1){
            cout<<"Please type in an integer for the\n"
                <<"element value: ";
            cin>>j;
            cin.clear();
            cin.ignore();
            myDblLL.headInsert(j);
            myDblLL.dsplyLnkLst();
        }
        if(i == 2){
            cout<<"Please type in an integer for the\n"
                <<"element value: ";
            cin>>j;
            cin.clear();
            cin.ignore();
            myDblLL.tailInsert(j);
            myDblLL.dsplyLnkLst();
        }
        if(i == 3){
            cout<<"Please type in an integer for the\n"
                <<"element value: ";
            cin>>j;
            cin.clear();
            cin.ignore();
            cout<<"Please give a positive integer for the\n"
                <<"insert position: ";
            cin>>k;
            cin.clear();
            cin.ignore();
            myDblLL.posInsert(j, k);
            myDblLL.dsplyLnkLst();
        }
        if(i == 4){
            cout<<"Please give a positive integer for the\n"
                <<"position to delete: ";
            cin>>k;
            cin.clear();
            cin.ignore();
            myDblLL.deleteNode(k);
            myDblLL.dsplyLnkLst();
        }
        if(i == 5){
            myDblLL.dblLLInsertSort();
            myDblLL.dsplyLnkLst();
        }
        if(i == 6){
            myDblLL.dsplyLnkLst();
        }
        if(i == 7){
            cout<<"Going back to main menu..."<<endl;
        }
    }
}
