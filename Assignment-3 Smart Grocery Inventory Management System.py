#include <iostream>
#include <string>
using namespace std;

const int MAX = 100;

struct Product {
    int productID;
    string productName;
    string category;
    double price;
    int quantity;
    string expiryDate; // Format: YYYY-MM-DD
};

Product products[MAX];
int totalProducts = 0;

// Add Product
void addProduct() {
    if (totalProducts >= MAX) {
        cout << "Inventory Full!\n";
        return;
    }

    cout << "Enter Product ID: ";
    cin >> products[totalProducts].productID;
    cin.ignore();

    cout << "Enter Product Name: ";
    getline(cin, products[totalProducts].productName);

    cout << "Enter Category: ";
    getline(cin, products[totalProducts].category);

    cout << "Enter Price: ";
    cin >> products[totalProducts].price;

    cout << "Enter Quantity: ";
    cin >> products[totalProducts].quantity;
    cin.ignore();

    cout << "Enter Expiry Date (YYYY-MM-DD): ";
    getline(cin, products[totalProducts].expiryDate);

    totalProducts++;

    cout << "Product Added Successfully!\n";
}

// Search by Product ID
int searchByID(int id) {
    for (int i = 0; i < totalProducts; i++) {
        if (products[i].productID == id)
            return i;
    }
    return -1;
}

// Search by Product Name
int searchByName(string name) {
    for (int i = 0; i < totalProducts; i++) {
        if (products[i].productName == name)
            return i;
    }
    return -1;
}

// Update Product
void updateProduct() {
    int id;
    cout << "Enter Product ID to Update: ";
    cin >> id;

    int index = searchByID(id);

    if (index == -1) {
        cout << "Product Not Found!\n";
        return;
    }

    cin.ignore();

    cout << "Enter New Product Name: ";
    getline(cin, products[index].productName);

    cout << "Enter New Category: ";
    getline(cin, products[index].category);

    cout << "Enter New Price: ";
    cin >> products[index].price;

    cout << "Enter New Quantity: ";
    cin >> products[index].quantity;
    cin.ignore();

    cout << "Enter New Expiry Date: ";
    getline(cin, products[index].expiryDate);

    cout << "Product Updated Successfully!\n";
}

// Delete Product
void deleteProduct() {
    int id;
    cout << "Enter Product ID to Delete: ";
    cin >> id;

    int index = searchByID(id);

    if (index == -1) {
        cout << "Product Not Found!\n";
        return;
    }

    for (int i = index; i < totalProducts - 1; i++) {
        products[i] = products[i + 1];
    }

    totalProducts--;

    cout << "Product Deleted Successfully!\n";
}

// Display All Products
void displayProducts() {
    if (totalProducts == 0) {
        cout << "\nNo Products Available!\n";
        return;
    }

    cout << "\n=====================================================================\n";
    cout << "ID\tName\t\tCategory\tPrice\tQty\tExpiry Date\n";
    cout << "=====================================================================\n";

    for (int i = 0; i < totalProducts; i++) {
        cout << products[i].productID << "\t"
             << products[i].productName << "\t\t"
             << products[i].category << "\t\t"
             << products[i].price << "\t"
             << products[i].quantity << "\t"
             << products[i].expiryDate << endl;
    }
}

// Sort by Price
void sortByPrice() {
    for (int i = 0; i < totalProducts - 1; i++) {
        for (int j = 0; j < totalProducts - i - 1; j++) {
            if (products[j].price > products[j + 1].price) {
                swap(products[j], products[j + 1]);
            }
        }
    }

    cout << "Products Sorted By Price.\n";
}

// Sort by Quantity
void sortByQuantity() {
    for (int i = 0; i < totalProducts - 1; i++) {
        for (int j = 0; j < totalProducts - i - 1; j++) {
            if (products[j].quantity > products[j + 1].quantity) {
                swap(products[j], products[j + 1]);
            }
        }
    }

    cout << "Products Sorted By Quantity.\n";
}

// Sort by Expiry Date
void sortByExpiryDate() {
    for (int i = 0; i < totalProducts - 1; i++) {
        for (int j = 0; j < totalProducts - i - 1; j++) {
            if (products[j].expiryDate > products[j + 1].expiryDate) {
                swap(products[j], products[j + 1]);
            }
        }
    }

    cout << "Products Sorted By Expiry Date.\n";
}

int main() {
    int choice;

    do {
        cout << "\n\n===== SMART GROCERY INVENTORY MANAGEMENT SYSTEM =====";
        cout << "\n1. Add Product";
        cout << "\n2. Update Product";
        cout << "\n3. Delete Product";
        cout << "\n4. Search Product by ID";
        cout << "\n5. Search Product by Name";
        cout << "\n6. Display All Products";
        cout << "\n7. Sort by Price";
        cout << "\n8. Sort by Quantity";
        cout << "\n9. Sort by Expiry Date";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch (choice) {

        case 1:
            addProduct();
            break;

        case 2:
            updateProduct();
            break;

        case 3:
            deleteProduct();
            break;

        case 4: {
            int id;
            cout << "Enter Product ID: ";
            cin >> id;

            int index = searchByID(id);

            if (index != -1) {
                cout << "\nProduct Found:";
                cout << "\nID: " << products[index].productID;
                cout << "\nName: " << products[index].productName;
                cout << "\nCategory: " << products[index].category;
                cout << "\nPrice: " << products[index].price;
                cout << "\nQuantity: " << products[index].quantity;
                cout << "\nExpiry Date: " << products[index].expiryDate << endl;
            } else {
                cout << "Product Not Found!\n";
            }
            break;
        }

        case 5: {
            string name;
            cin.ignore();
            cout << "Enter Product Name: ";
            getline(cin, name);

            int index = searchByName(name);

            if (index != -1) {
                cout << "\nProduct Found:";
                cout << "\nID: " << products[index].productID;
                cout << "\nName: " << products[index].productName;
                cout << "\nCategory: " << products[index].category;
                cout << "\nPrice: " << products[index].price;
                cout << "\nQuantity: " << products[index].quantity;
                cout << "\nExpiry Date: " << products[index].expiryDate << endl;
            } else {
                cout << "Product Not Found!\n";
            }
            break;
        }

        case 6:
            displayProducts();
            break;

        case 7:
            sortByPrice();
            displayProducts();
            break;

        case 8:
            sortByQuantity();
            displayProducts();
            break;

        case 9:
            sortByExpiryDate();
            displayProducts();
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