class Item:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

class Bookstore:
    def __init__(self):
        self.inventory = []

    def add_book(self, item):
        self.inventory.append(item)

    def remove_book(self, item):
        self.inventory.remove(item)

    def display_books(self):
        for item in self.inventory:
            print(f'Title: {item.title}, Author: {item.author}, Price: {item.price}, Stock: {item.stock}')
          

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.purchase_history = []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)

class Transaction:
    def __init__(self, customer, item, total_cost):
        self.customer = customer
        self.item = item
        self.total_cost = total_cost

class Discount:
    def __init__(self, threshold, discount_rate):
        self.threshold = threshold
        self.discount_rate = discount_rate

def apply_discount(self, customer):
    total_spent = sum([transaction.total_cost for transaction in customer.purchase_history])
    if total_spent > self.threshold:
        return total_spent * self.discount_rate
    else:
        return 0

def interactive_menu():
    bookstore = Bookstore()
    customers = []

    while True:
        print("1. Add book")
        print("2. Display books")
        print("3. Make a purchase")
        print("4. View purchase history")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            stock = int(input("Enter book stock: "))
            bookstore.add_book(Item(title, author, price, stock))

        elif choice == '2':
            bookstore.display_books()

        elif choice == '3':
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter customer address: ")
            book_title = input("Enter book title: ")
            customer = next((c for c in customers if c.name == customer_name), None)
                        
            if not customer:
                customer = Customer(customer_name, customer_address)
                customers.append(customer)
                book = next((b for b in bookstore.inventory if b.title == book_title), None)

            if book and book.stock > 0:
                book.stock -= 1
                transaction = Transaction(customer, book, book.price)
                customer.add_purchase(transaction)

            else:
                print("Book not available")

        elif choice == '4':
            customer_name = input("Enter customer name: ")
            customer = next((c for c in customers if c.name == customer_name), None)
            if customer:
                for transaction in customer.purchase_history:
                    print(f'Book: {transaction.item.title}, Cost: {transaction.total_cost}')
            else:
                print("Customer not found")    

        elif choice == '5':
            print("Thank You :)")
        
            break

        else:
            print("Pilihan anada tidak valid")

interactive_menu()