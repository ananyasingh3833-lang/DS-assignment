#include <iostream>
#include <queue>
#include <stack>
using namespace std;

queue<string> normalOrders;
queue<string> vipOrders;
stack<string> cancelledOrders;

// Recursive Menu
void foodMenu(int n)
{
    if(n == 0)
        return;

    int choice;

    cout << "\n----- RESTAURANT MENU -----\n";
    cout << "1. Pizza\n";
    cout << "2. Burger\n";
    cout << "3. Pasta\n";
    cout << "0. Exit Menu\n";

    cout << "Enter Choice: ";
    cin >> choice;

    if(choice == 0)
        return;

    cout << "Item Selected Successfully!\n";

    foodMenu(n - 1);
}

int main()
{
    int choice;
    string order;

    do
    {
        cout << "\n\n===== RESTAURANT ORDER MANAGEMENT =====";
        cout << "\n1. Add Normal Order";
        cout << "\n2. Add VIP Order";
        cout << "\n3. Process Order";
        cout << "\n4. Cancel Order";
        cout << "\n5. View Cancelled Orders";
        cout << "\n6. Open Food Menu";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;
        cin.ignore();

        switch(choice)
        {
            case 1:
                cout << "Enter Order Name: ";
                getline(cin, order);
                normalOrders.push(order);
                cout << "Normal Order Added.\n";
                break;

            case 2:
                cout << "Enter VIP Order Name: ";
                getline(cin, order);
                vipOrders.push(order);
                cout << "VIP Order Added.\n";
                break;

            case 3:
                if(!vipOrders.empty())
                {
                    cout << "Processing VIP Order: "
                         << vipOrders.front() << endl;
                    vipOrders.pop();
                }
                else if(!normalOrders.empty())
                {
                    cout << "Processing Normal Order: "
                         << normalOrders.front() << endl;
                    normalOrders.pop();
                }
                else
                {
                    cout << "No Orders Available!\n";
                }
                break;

            case 4:
                if(!vipOrders.empty())
                {
                    cancelledOrders.push(vipOrders.front());
                    cout << "VIP Order Cancelled: "
                         << vipOrders.front() << endl;
                    vipOrders.pop();
                }
                else if(!normalOrders.empty())
                {
                    cancelledOrders.push(normalOrders.front());
                    cout << "Normal Order Cancelled: "
                         << normalOrders.front() << endl;
                    normalOrders.pop();
                }
                else
                {
                    cout << "No Orders Available!\n";
                }
                break;

            case 5:
            {
                stack<string> temp = cancelledOrders;

                cout << "\nCancelled Orders:\n";

                while(!temp.empty())
                {
                    cout << temp.top() << endl;
                    temp.pop();
                }
                break;
            }

            case 6:
                foodMenu(3);
                break;

            case 0:
                cout << "Program Ended.\n";
                break;

            default:
                cout << "Invalid Choice!\n";
        }

    } while(choice != 0);

    return 0;
}