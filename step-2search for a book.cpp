// This program stores and searches for book IDs
#include <iostream>
using namespace std;

int main()
{
    int books[5];
    int searchID;
    bool found = false;

    cout << "Enter IDs of 5 books:" << endl;

    for (int i = 0; i < 5; i++)
    {
        cin >> books[i];
    }

    cout << "Enter Book ID to search: ";
    cin >> searchID;

    for (int i = 0; i < 5; i++)
    {
        if (books[i] == searchID)
        {
            found = true;
        }
    }

    if (found)
        cout << "Book Found";
    else
        cout << "Book Not Found";

    return 0;
}