#include <iostream>
using namespace std;

const int SIZE = 10;

struct Student
{
    int rollNo;
    string name;
    string course;

    Student* next;
};

Student* hashTable[SIZE];

// Hash Function
int hashFunction(int rollNo)
{
    return rollNo % SIZE;
}

// Register Student
void addStudent(int rollNo, string name, string course)
{
    int index = hashFunction(rollNo);

    Student* newStudent = new Student;
    newStudent->rollNo = rollNo;
    newStudent->name = name;
    newStudent->course = course;

    newStudent->next = hashTable[index];
    hashTable[index] = newStudent;

    cout << "Student Registered Successfully!\n";
}

// Search Student
void searchStudent(int rollNo)
{
    int index = hashFunction(rollNo);

    Student* temp = hashTable[index];

    while(temp != NULL)
    {
        if(temp->rollNo == rollNo)
        {
            cout << "\nStudent Found\n";
            cout << "Roll No: " << temp->rollNo << endl;
            cout << "Name: " << temp->name << endl;
            cout << "Course: " << temp->course << endl;
            return;
        }

        temp = temp->next;
    }

    cout << "Student Not Found!\n";
}

// Update Student
void updateStudent(int rollNo)
{
    int index = hashFunction(rollNo);

    Student* temp = hashTable[index];

    while(temp != NULL)
    {
        if(temp->rollNo == rollNo)
        {
            cout << "Enter New Name: ";
            cin.ignore();
            getline(cin, temp->name);

            cout << "Student Updated Successfully!\n";
            return;
        }

        temp = temp->next;
    }

    cout << "Student Not Found!\n";
}

// Enroll Course
void enrollCourse(int rollNo)
{
    int index = hashFunction(rollNo);

    Student* temp = hashTable[index];

    while(temp != NULL)
    {
        if(temp->rollNo == rollNo)
        {
            cout << "Enter Course Name: ";
            cin.ignore();
            getline(cin, temp->course);

            cout << "Course Enrolled Successfully!\n";
            return;
        }

        temp = temp->next;
    }

    cout << "Student Not Found!\n";
}

// Withdraw Course
void withdrawCourse(int rollNo)
{
    int index = hashFunction(rollNo);

    Student* temp = hashTable[index];

    while(temp != NULL)
    {
        if(temp->rollNo == rollNo)
        {
            temp->course = "No Course";

            cout << "Course Withdrawn Successfully!\n";
            return;
        }

        temp = temp->next;
    }

    cout << "Student Not Found!\n";
}

// Delete Student
void deleteStudent(int rollNo)
{
    int index = hashFunction(rollNo);

    Student* temp = hashTable[index];
    Student* prev = NULL;

    while(temp != NULL)
    {
        if(temp->rollNo == rollNo)
        {
            if(prev == NULL)
                hashTable[index] = temp->next;
            else
                prev->next = temp->next;

            delete temp;

            cout << "Student Record Deleted!\n";
            return;
        }

        prev = temp;
        temp = temp->next;
    }

    cout << "Student Not Found!\n";
}

// Display All Students
void displayStudents()
{
    cout << "\n===== STUDENT RECORDS =====\n";

    for(int i = 0; i < SIZE; i++)
    {
        Student* temp = hashTable[i];

        while(temp != NULL)
        {
            cout << "\nRoll No: " << temp->rollNo;
            cout << "\nName: " << temp->name;
            cout << "\nCourse: " << temp->course;
            cout << "\n--------------------";

            temp = temp->next;
        }
    }
}

int main()
{
    for(int i = 0; i < SIZE; i++)
        hashTable[i] = NULL;

    int choice, rollNo;
    string name, course;

    do
    {
        cout << "\n\n===== STUDENT REGISTRATION SYSTEM =====";
        cout << "\n1. Register Student";
        cout << "\n2. Search Student";
        cout << "\n3. Update Student";
        cout << "\n4. Enroll Course";
        cout << "\n5. Withdraw Course";
        cout << "\n6. Delete Student";
        cout << "\n7. Display All Students";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
                cout << "Enter Roll No: ";
                cin >> rollNo;
                cin.ignore();

                cout << "Enter Name: ";
                getline(cin, name);

                cout << "Enter Course: ";
                getline(cin, course);

                addStudent(rollNo, name, course);
                break;

            case 2:
                cout << "Enter Roll No: ";
                cin >> rollNo;
                searchStudent(rollNo);
                break;

            case 3:
                cout << "Enter Roll No: ";
                cin >> rollNo;
                updateStudent(rollNo);
                break;

            case 4:
                cout << "Enter Roll No: ";
                cin >> rollNo;
                enrollCourse(rollNo);
                break;

            case 5:
                cout << "Enter Roll No: ";
                cin >> rollNo;
                withdrawCourse(rollNo);
                break;

            case 6:
                cout << "Enter Roll No: ";
                cin >> rollNo;
                deleteStudent(rollNo);
                break;

            case 7:
                displayStudents();
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