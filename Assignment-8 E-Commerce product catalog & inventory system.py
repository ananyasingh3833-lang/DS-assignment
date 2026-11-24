#include <iostream>
using namespace std;

const int SIZE = 10;

// Product Node
struct Product
{
    int id;
    string name;
    float price;
    int quantity;

    Product* next;
};

// Hash Table
Product* hashTable[SIZE];

// Hash Function
int hashFunction(int id)
{
    return id % SIZE;
}

// Add Product
void addProduct(int id, string name, float price, int quantity)
{
    int index = hashFunction(id);

    Product* newProduct = new Product;
    newProduct->id = id;
    newProduct->name = name;
    newProduct->price = price;
    newProduct->quantity = quantity;

    newProduct->next = hashTable[index];
    hashTable[index] = newProduct;

    cout << "Product Added Successfully!\n";
}

// Search Product
void searchProduct(int id)
{
    int index = hashFunction(id);

    Product* temp = hashTable[index];

    while(temp != NULL)
    {
        if(temp->id == id)
        {
            cout << "\nProduct Found\n";
            cout << "ID: " << temp->id << endl;
            cout << "Name: " << temp->name << endl;
            cout << "Price: " << temp->price << endl;
            cout << "Quantity: " << temp->quantity << endl;
            return;
        }

        temp = temp->next;
    }

    cout << "Product Not Found!\n";
}

// Update Product
void updateProduct(int id)
{
    int index = hashFunction(id);

    Product* temp = hashTable[index];

    while(temp != NULL)
    {
        if(temp->id == id)
        {
            cout << "Enter New Name: ";
            cin.ignore();
            getline(cin, temp->name);

            cout << "Enter New Price: ";
            cin >> temp->price;

            cout << "Enter New Quantity: ";
            cin >> temp->quantity;

            cout << "Product Updated Successfully!\n";
            return;
        }

        temp = temp->next;
    }

    cout << "Product Not Found!\n";
}

// Delete Product
void deleteProduct(int id)
{
    int index = hashFunction(id);

    Product* temp = hashTable[index];
    Product* prev = NULL;

    while(temp != NULL)
    {
        if(temp->id == id)
        {
            if(prev == NULL)
                hashTable[index] = temp->next;
            else
                prev->next = temp->next;

            delete temp;

            cout << "Product Removed Successfully!\n";
            return;
        }

        prev = temp;
        temp = temp->next;
    }

    cout << "Product Not Found!\n";
}

// Display All Products
void displayProducts()
{
    cout << "\n===== PRODUCT CATALOG =====\n";

    for(int i = 0; i < SIZE; i++)
    {
        Product* temp = hashTable[i];

        while(temp != NULL)
        {
            cout << "\nID: " << temp->id;
            cout << "\nName: " << temp->name;
            cout << "\nPrice: " << temp->price;
            cout << "\nQuantity: " << temp->quantity;
            cout << "\n----------------------";

            temp = temp->next;
        }
    }
}

int main()
{
    for(int i = 0; i < SIZE; i++)
        hashTable[i] = NULL;

    int choice, id, quantity;
    string name;
    float price;

    do
    {
        cout << "\n\n===== E-COMMERCE PRODUCT CATALOG =====";
        cout << "\n1. Add Product";
        cout << "\n2. Search Product";
        cout << "\n3. Update Product";
        cout << "\n4. Delete Product";
        cout << "\n5. Display All Products";
        cout << "\n0. Exit";

        cout << "\nEnter Choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
                cout << "Enter Product ID: ";
                cin >> id;
                cin.ignore();

                cout << "Enter Product Name: ";
                getline(cin, name);

                cout << "Enter Price: ";
                cin >> price;

                cout << "Enter Quantity: ";
                cin >> quantity;

                addProduct(id, name, price, quantity);
                break;

            case 2:
                cout << "Enter Product ID: ";
                cin >> id;
                searchProduct(id);
                break;

            case 3:
                cout << "Enter Product ID: ";
                cin >> id;
                updateProduct(id);
                break;

            case 4:
                cout << "Enter Product ID: ";
                cin >> id;
                deleteProduct(id);
                break;

            case 5:
                displayProducts();
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
