// This program stores and displays book IDs and display it
#include <iostream>
using namespace std;

int main()
{
    int bookID, bookID2, bookID3;
    string bookName, bookName2, bookName3;

    cout << "Enter first book ID: ";
    cin >> bookID;

    cout << "Enter first book name: ";
    cin >> bookName;

    cout << "Enter second book ID: ";
    cin >> bookID2;

    cout << "Enter second book name: ";
    cin >> bookName2;

    cout << "Enter third book ID: ";
    cin >> bookID3;

    cout << "Enter third book name: ";
    cin >> bookName3;

    cout << "\n--- BOOK DETAILS ---\n";

    cout << "1. " << bookID << " - " << bookName << endl;
    cout << "2. " << bookID2 << " - " << bookName2 << endl;
    cout << "3. " << bookID3 << " - " << bookName3 << endl;

    return 0;
}