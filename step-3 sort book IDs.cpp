// This program sorts book IDs
#include <iostream>
using namespace std;

int main()
{
    int books[5];
    int temp;

    cout << "Enter IDs of 5 books:" << endl;

    for (int i = 0; i < 5; i++)
    {
        cin >> books[i];
    }

    // Sorting in ascending order
    for (int i = 0; i < 5; i++)
    {
        for (int j = i + 1; j < 5; j++)
        {
            if (books[i] > books[j])
            {
                temp = books[i];
                books[i] = books[j];
                books[j] = temp;
            }
        }
    }

    cout << "\nBook IDs in ascending order:" << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << books[i] << " ";
    }

    return 0;
}