#include <iostream>
using namespace std;

const int SIZE = 10;

// Patient Node
struct Patient
{
    int id;
    string name;
    int age;
    string disease;

    Patient* next;
};

// Hash Table
Patient* hashTable[SIZE];

// Hash Function
int hashFunction(int id)
{
    return id % SIZE;
}

// Register Patient
void addPatient(int id, string name, int age, string disease)
{
    int index = hashFunction(id);

    Patient* newPatient = new Patient;
    newPatient->id = id;
    newPatient->name = name;
    newPatient->age = age;
    newPatient->disease = disease;
    newPatient->next = nullptr;

    newPatient->next = hashTable[index];
    hashTable[index] = newPatient;

    cout << "Patient Registered Successfully!\n";
}

// Search Patient
void searchPatient(int id)
{
    int index = hashFunction(id);

    Patient* temp = hashTable[index];

    while(temp != nullptr)
    {
        if(temp->id == id)
        {
            cout << "\nPatient Found\n";
            cout << "ID: " << temp->id << endl;
            cout << "Name: " << temp->name << endl;
            cout << "Age: " << temp->age << endl;
            cout << "Disease: " << temp->disease << endl;
            return;
        }
        temp = temp->next;
    }

    cout << "Patient Not Found!\n";
}

// Update Patient
void updatePatient(int id)
{
    int index = hashFunction(id);

    Patient* temp = hashTable[index];

    while(temp != nullptr)
    {
        if(temp->id == id)
        {
            cout << "Enter New Name: ";
            cin.ignore();
            getline(cin, temp->name);

            cout << "Enter New Age: ";
            cin >> temp->age;

            cout << "Enter New Disease: ";
            cin.ignore();
            getline(cin, temp->disease);

            cout << "Record Updated Successfully!\n";
            return;
        }

        temp = temp->next;
    }

    cout << "Patient Not Found!\n";
}

// Discharge Patient
void deletePatient(int id)
{
    int index = hashFunction(id);

    Patient* temp = hashTable[index];
    Patient* prev = nullptr;

    while(temp != nullptr)
    {
        if(temp->id == id)
        {
            if(prev == nullptr)
                hashTable[index] = temp->next;
            else
                prev->next = temp->next;

            delete temp;

            cout << "Patient Discharged Successfully!\n";
            return;
        }

        prev = temp;
        temp = temp->next;
    }

    cout << "Patient Not Found!\n";
}

// Display All Patients
void displayPatients()
{
    cout << "\n===== PATIENT RECORDS =====\n";

    for(int i = 0; i < SIZE; i++)
    {
        Patient* temp = hashTable[i];

        while(temp != nullptr)
        {
            cout << "\nID: " << temp->id;
            cout << "\nName: " << temp->name;
            cout << "\nAge: " << temp->age;
            cout << "\nDisease: " << temp->disease;
            cout << "\n-------------------";

            temp = temp->next;
        }
    }
}

int main()
{
    for(int i = 0; i < SIZE; i++)
        hashTable[i] = nullptr;

    int choice, id, age;
    string name, disease;

    do
    {
        cout << "\n\n===== HOSPITAL MANAGEMENT SYSTEM =====";
        cout << "\n1. Register Patient";
        cout << "\n2. Search Patient";
        cout << "\n3. Update Patient";
        cout << "\n4. Discharge Patient";
        cout << "\n5. Display All Patients";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
                cout << "Enter Patient ID: ";
                cin >> id;
                cin.ignore();

                cout << "Enter Name: ";
                getline(cin, name);

                cout << "Enter Age: ";
                cin >> age;
                cin.ignore();

                cout << "Enter Disease: ";
                getline(cin, disease);

                addPatient(id, name, age, disease);
                break;

            case 2:
                cout << "Enter Patient ID: ";
                cin >> id;
                searchPatient(id);
                break;

            case 3:
                cout << "Enter Patient ID: ";
                cin >> id;
                updatePatient(id);
                break;

            case 4:
                cout << "Enter Patient ID: ";
                cin >> id;
                deletePatient(id);
                break;

            case 5:
                displayPatients();
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