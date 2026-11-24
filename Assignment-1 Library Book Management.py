#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

// Book Structure
struct Book {
    int bookID;
    string title;
    string author;
    string department;
};

// BST Node
class Node {
public:
    Book book;
    Node *left, *right;

    Node(Book b) {
        book = b;
        left = right = NULL;
    }
};

// BST Class
class LibraryBST {
private:
    Node* root;

    Node* insert(Node* root, Book b) {
        if (root == NULL)
            return new Node(b);

        if (b.bookID < root->book.bookID)
            root->left = insert(root->left, b);
        else
            root->right = insert(root->right, b);

        return root;
    }

    Node* findMin(Node* root) {
        while (root && root->left)
            root = root->left;
        return root;
    }

    Node* deleteBook(Node* root, int id) {
        if (!root)
            return root;

        if (id < root->book.bookID)
            root->left = deleteBook(root->left, id);
        else if (id > root->book.bookID)
            root->right = deleteBook(root->right, id);
        else {
            if (!root->left) {
                Node* temp = root->right;
                delete root;
                return temp;
            }
            else if (!root->right) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            Node* temp = findMin(root->right);
            root->book = temp->book;
            root->right = deleteBook(root->right,
                                     temp->book.bookID);
        }
        return root;
    }

    Node* search(Node* root, int id) {
        if (!root || root->book.bookID == id)
            return root;

        if (id < root->book.bookID)
            return search(root->left, id);

        return search(root->right, id);
    }

    void inorder(Node* root) {
        if (!root)
            return;

        inorder(root->left);

        cout << "\nID: " << root->book.bookID
             << "\nTitle: " << root->book.title
             << "\nAuthor: " << root->book.author
             << "\nDepartment: " << root->book.department
             << "\n---------------------";

        inorder(root->right);
    }

    void preorder(Node* root) {
        if (!root)
            return;

        cout << root->book.bookID << " ";
        preorder(root->left);
        preorder(root->right);
    }

    void postorder(Node* root) {
        if (!root)
            return;

        postorder(root->left);
        postorder(root->right);
        cout << root->book.bookID << " ";
    }

public:
    LibraryBST() {
        root = NULL;
    }

    void insertBook(Book b) {
        root = insert(root, b);
    }

    void deleteBook(int id) {
        root = deleteBook(root, id);
    }

    void searchBook(int id) {
        Node* result = search(root, id);

        if (result) {
            cout << "\nBook Found:";
            cout << "\nID: " << result->book.bookID;
            cout << "\nTitle: " << result->book.title;
            cout << "\nAuthor: " << result->book.author;
            cout << "\nDepartment: "
                 << result->book.department << endl;
        }
        else {
            cout << "\nBook not found.\n";
        }
    }

    void displayBooks() {
        inorder(root);
    }

    void displayPreorder() {
        preorder(root);
        cout << endl;
    }

    void displayPostorder() {
        postorder(root);
        cout << endl;
    }
};

int main() {
    LibraryBST library;
    vector<Book> books;
    map<string, vector<Book>> departments;

    int choice;

    do {
        cout << "\n===== SMART LIBRARY MANAGEMENT =====";
        cout << "\n1. Add Book";
        cout << "\n2. Delete Book";
        cout << "\n3. Search Book by ID";
        cout << "\n4. Display All Books";
        cout << "\n5. Sort Books by Title";
        cout << "\n6. Department-wise Books";
        cout << "\n7. Preorder Traversal";
        cout << "\n8. Postorder Traversal";
        cout << "\n0. Exit";
        cout << "\nEnter Choice: ";
        cin >> choice;

        switch(choice) {

        case 1: {
            Book b;
            cout << "Enter Book ID: ";
            cin >> b.bookID;
            cin.ignore();

            cout << "Enter Title: ";
            getline(cin, b.title);

            cout << "Enter Author: ";
            getline(cin, b.author);

            cout << "Enter Department: ";
            getline(cin, b.department);

            books.push_back(b);
            departments[b.department].push_back(b);
            library.insertBook(b);

            cout << "Book Added Successfully!\n";
            break;
        }

        case 2: {
            int id;
            cout << "Enter Book ID to Delete: ";
            cin >> id;

            library.deleteBook(id);

            cout << "Book Deleted Successfully!\n";
            break;
        }

        case 3: {
            int id;
            cout << "Enter Book ID: ";
            cin >> id;
            library.searchBook(id);
            break;
        }

        case 4:
            cout << "\n--- Library Books (Inorder) ---\n";
            library.displayBooks();
            break;

        case 5:
            sort(books.begin(), books.end(),
                 [](Book a, Book b) {
                    return a.title < b.title;
                 });

            cout << "\nBooks Sorted By Title:\n";

            for (auto &b : books) {
                cout << b.bookID << " - "
                     << b.title << endl;
            }
            break;

        case 6:
            cout << "\nDepartment-wise Books:\n";

            for (auto &dept : departments) {
                cout << "\nDepartment: "
                     << dept.first << endl;

                for (auto &b : dept.second) {
                    cout << b.bookID
                         << " - "
                         << b.title << endl;
                }
            }
            break;

        case 7:
            cout << "\nPreorder Traversal: ";
            library.displayPreorder();
            break;

        case 8:
            cout << "\nPostorder Traversal: ";
            library.displayPostorder();
            break;

        case 0:
            cout << "Exiting...\n";
            break;

        default:
            cout << "Invalid Choice!\n";
        }

    } while(choice != 0);

    return 0;
}