#include <iostream>
#include <string>
using namespace std;

const int MAX = 100;

struct Student {
    int rollNo;
    string name;
    string program;
    float marks;
};

Student students[MAX];
int countStudents = 0;

// Add Student
void addStudent() {
    if (countStudents >= MAX) {
        cout << "Student limit reached!\n";
        return;
    }

    cout << "Enter Roll Number: ";
    cin >> students[countStudents].rollNo;
    cin.ignore();

    cout << "Enter Name: ";
    getline(cin, students[countStudents].name);

    cout << "Enter Program: ";
    getline(cin, students[countStudents].program);

    cout << "Enter Total Marks: ";
    cin >> students[countStudents].marks;

    countStudents++;
    cout << "Student Added Successfully!\n";
}

// Search Student
int searchStudent(int roll) {
    for (int i = 0; i < countStudents; i++) {
        if (students[i].rollNo == roll)
            return i;
    }
    return -1;
}

// Update Student
void updateStudent() {
    int roll;
    cout << "Enter Roll Number to Update: ";
    cin >> roll;

    int index = searchStudent(roll);

    if (index == -1) {
        cout << "Student Not Found!\n";
        return;
    }

    cin.ignore();

    cout << "Enter New Name: ";
    getline(cin, students[index].name);

    cout << "Enter New Program: ";
    getline(cin, students[index].program);

    cout << "Enter New Marks: ";
    cin >> students[index].marks;

    cout << "Record Updated Successfully!\n";
}

// Delete Student
void deleteStudent() {
    int roll;
    cout << "Enter Roll Number to Delete: ";
    cin >> roll;

    int index = searchStudent(roll);

    if (index == -1) {
        cout << "Student Not Found!\n";
        return;
    }

    for (int i = index; i < countStudents - 1; i++) {
        students[i] = students[i + 1];
    }

    countStudents--;
    cout << "Record Deleted Successfully!\n";
}

// Display Records
void displayStudents() {
    if (countStudents == 0) {
        cout << "\nNo Records Available!\n";
        return;
    }

    cout << "\n---------------------------------------------\n";
    cout << "Roll No\tName\t\tProgram\t\tMarks\n";
    cout << "---------------------------------------------\n";

    for (int i = 0; i < countStudents; i++) {
        cout << students[i].rollNo << "\t"
             << students[i].name << "\t\t"
             << students[i].program << "\t\t"
             << students[i].marks << endl;
    }
}

// Sort by Roll Number
void sortByRollNo() {
    for (int i = 0; i < countStudents - 1; i++) {
        for (int j = 0; j < countStudents - i - 1; j++) {
            if (students[j].rollNo > students[j + 1].rollNo) {
                swap(students[j], students[j + 1]);
            }
        }
    }

    cout << "Sorted by Roll Number.\n";
}

// Sort by Name
void sortByName() {
    for (int i = 0; i < countStudents - 1; i++) {
        for (int j = 0; j < countStudents - i - 1; j++) {
            if (students[j].name > students[j + 1].name) {
                swap(students[j], students[j + 1]);
            }
        }
    }

    cout << "Sorted by Name.\n";
}

// Merit List (Marks Descending)
void generateMeritList() {
    for (int i = 0; i < countStudents - 1; i++) {
        for (int j = 0; j < countStudents - i - 1; j++) {
            if (students[j].marks < students[j + 1].marks) {
                swap(students[j], students[j + 1]);
            }
        }
    }

    cout << "\n===== MERIT LIST =====\n";
    cout << "Rank\tRoll No\tName\t\tMarks\n";

    for (int i = 0; i < countStudents; i++) {
        cout << i + 1 << "\t"
             << students[i].rollNo << "\t"
             << students[i].name << "\t\t"
             << students[i].marks << endl;
    }
}

int main() {
    int choice;

    do {
        cout << "\n\n===== STUDENT PERFORMANCE & RANKING MANAGEMENT SYSTEM =====";
        cout << "\n1. Add Student";
        cout << "\n2. Update Student";
        cout << "\n3. Delete Student";
        cout << "\n4. Search Student";
        cout << "\n5. Display All Students";
        cout << "\n6. Sort by Roll Number";
        cout << "\n7. Sort by Name";
        cout << "\n8. Generate Merit List";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch (choice) {

        case 1:
            addStudent();
            break;

        case 2:
            updateStudent();
            break;

        case 3:
            deleteStudent();
            break;

        case 4: {
            int roll;
            cout << "Enter Roll Number to Search: ";
            cin >> roll;

            int index = searchStudent(roll);

            if (index != -1) {
                cout << "\nStudent Found:";
                cout << "\nRoll No: " << students[index].rollNo;
                cout << "\nName: " << students[index].name;
                cout << "\nProgram: " << students[index].program;
                cout << "\nMarks: " << students[index].marks << endl;
            } else {
                cout << "Student Not Found!\n";
            }
            break;
        }

        case 5:
            displayStudents();
            break;

        case 6:
            sortByRollNo();
            displayStudents();
            break;

        case 7:
            sortByName();
            displayStudents();
            break;

        case 8:
            generateMeritList();
            break;

        case 0:
            cout << "Exiting Program...\n";
            break;

        default:
            cout << "Invalid Choice!\n";
        }

    } while (choice != 0);

    return 0;
}
