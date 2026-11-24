#include <iostream>
#include <queue>
#include <stack>
using namespace std;

queue<string> normalCustomers;
queue<string> priorityCustomers;
stack<string> servedCustomers;

int main()
{
    int choice;
    string name;

    do
    {
        cout << "\n\n===== BANK TOKEN MANAGEMENT SYSTEM =====";
        cout << "\n1. Add Normal Customer";
        cout << "\n2. Add Priority Customer";
        cout << "\n3. Serve Next Customer";
        cout << "\n4. View Recently Served Customers";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;
        cin.ignore();

        switch(choice)
        {
            case 1:
                cout << "Enter Customer Name: ";
                getline(cin, name);

                normalCustomers.push(name);
                cout << "Token Issued Successfully!\n";
                break;

            case 2:
                cout << "Enter Priority Customer Name: ";
                getline(cin, name);

                priorityCustomers.push(name);
                cout << "Priority Token Issued Successfully!\n";
                break;

            case 3:
                if(!priorityCustomers.empty())
                {
                    cout << "Serving Priority Customer: "
                         << priorityCustomers.front() << endl;

                    servedCustomers.push(priorityCustomers.front());
                    priorityCustomers.pop();
                }
                else if(!normalCustomers.empty())
                {
                    cout << "Serving Customer: "
                         << normalCustomers.front() << endl;

                    servedCustomers.push(normalCustomers.front());
                    normalCustomers.pop();
                }
                else
                {
                    cout << "No Customers in Queue!\n";
                }
                break;

            case 4:
            {
                stack<string> temp = servedCustomers;

                cout << "\nRecently Served Customers:\n";

                while(!temp.empty())
                {
                    cout << temp.top() << endl;
                    temp.pop();
                }
                break;
            }

            case 0:
                cout << "Program Ended.\n";
                break;

            default:
                cout << "Invalid Choice!\n";
        }

    } while(choice != 0);

    return 0;
}