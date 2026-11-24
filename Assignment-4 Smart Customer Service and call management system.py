#include <iostream>
#include <queue>
#include <stack>
#include <string>

using namespace std;

// Customer Request Structure
struct Request {
    int id;
    string customerName;
    string issue;
    int priority;

    // For Priority Queue
    bool operator<(const Request& other) const {
        return priority < other.priority;
    }
};

// Queue for Normal Calls
queue<Request> normalCalls;

// Priority Queue for Urgent Calls
priority_queue<Request> urgentCalls;

// Stack for Resolved Requests
stack<Request> resolvedRequests;

// Add Normal Call
void addNormalCall() {
    Request r;

    cout << "Enter Request ID: ";
    cin >> r.id;
    cin.ignore();

    cout << "Enter Customer Name: ";
    getline(cin, r.customerName);

    cout << "Enter Issue: ";
    getline(cin, r.issue);

    r.priority = 0;

    normalCalls.push(r);

    cout << "Normal Call Added Successfully.\n";
}

// Add Urgent Call
void addUrgentCall() {
    Request r;

    cout << "Enter Request ID: ";
    cin >> r.id;
    cin.ignore();

    cout << "Enter Customer Name: ";
    getline(cin, r.customerName);

    cout << "Enter Issue: ";
    getline(cin, r.issue);

    cout << "Enter Priority (1-10): ";
    cin >> r.priority;

    urgentCalls.push(r);

    cout << "Urgent Request Added Successfully.\n";
}

// Process Next Request
void processRequest() {

    Request current;

    if (!urgentCalls.empty()) {
        current = urgentCalls.top();
        urgentCalls.pop();

        cout << "\nProcessing URGENT Request:\n";
    }
    else if (!normalCalls.empty()) {
        current = normalCalls.front();
        normalCalls.pop();

        cout << "\nProcessing NORMAL Request:\n";
    }
    else {
        cout << "No Pending Requests.\n";
        return;
    }

    cout << "ID: " << current.id << endl;
    cout << "Customer: " << current.customerName << endl;
    cout << "Issue: " << current.issue << endl;

    resolvedRequests.push(current);

    cout << "Request Resolved Successfully.\n";
}

// View Recent Resolved Requests
void viewResolvedRequests() {

    if (resolvedRequests.empty()) {
        cout << "No Resolved Requests Available.\n";
        return;
    }

    stack<Request> temp = resolvedRequests;

    cout << "\n===== RECENTLY RESOLVED REQUESTS =====\n";

    while (!temp.empty()) {
        Request r = temp.top();

        cout << "\nRequest ID: " << r.id;
        cout << "\nCustomer: " << r.customerName;
        cout << "\nIssue: " << r.issue;
        cout << "\nPriority: " << r.priority;
        cout << "\n--------------------------";

        temp.pop();
    }
}

// Recursive IVR System
void IVRMenu(int level) {

    if (level == 0) {
        cout << "\nThank you for using our support system.\n";
        return;
    }

    int choice;

    cout << "\n===== IVR MENU =====\n";
    cout << "1. Billing Support\n";
    cout << "2. Technical Support\n";
    cout << "3. Product Information\n";
    cout << "4. Speak to Representative\n";
    cout << "0. Exit IVR\n";

    cout << "Enter Choice: ";
    cin >> choice;

    if (choice == 0) {
        cout << "Exiting IVR...\n";
        return;
    }

    switch (choice) {
        case 1:
            cout << "You selected Billing Support.\n";
            break;
        case 2:
            cout << "You selected Technical Support.\n";
            break;
        case 3:
            cout << "You selected Product Information.\n";
            break;
        case 4:
            cout << "Connecting to Representative...\n";
            break;
        default:
            cout << "Invalid Choice.\n";
    }

    // Recursive Call
    IVRMenu(level - 1);
}

int main() {

    int choice;

    do {
        cout << "\n\n===== SMART CUSTOMER SERVICE & CALL MANAGEMENT SYSTEM =====";
        cout << "\n1. Add Normal Call";
        cout << "\n2. Add Urgent Request";
        cout << "\n3. Process Next Request";
        cout << "\n4. View Resolved Requests";
        cout << "\n5. Start IVR System";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch (choice) {

            case 1:
                addNormalCall();
                break;

            case 2:
                addUrgentCall();
                break;

            case 3:
                processRequest();
                break;

            case 4:
                viewResolvedRequests();
                break;

            case 5:
                IVRMenu(5);
                break;

            case 0:
                cout << "Exiting System...\n";
                break;

            default:
                cout << "Invalid Choice!\n";
        }

    } while (choice != 0);

    return 0;
}