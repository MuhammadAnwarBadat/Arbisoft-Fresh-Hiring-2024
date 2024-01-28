class User:
    def __init__(self, user_type, username, password):
        self.user_type = user_type
        self.username = username
        self.password = password

    def can_create_vendor(self):
        return self.user_type == "admin"

    def can_add_item(self):
        return self.user_type in ["admin", "store_manager"]

    def can_buy_item(self):
        return self.user_type in ["normal_user", "store_manager", "admin"]


class Vendor:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Item:
    def __init__(self, name, price, stock, vendor_id):
        self.name = name
        self.price = price
        self.stock = stock
        self.vendor_id = vendor_id


class EcommerceSystem:
    def __init__(self):
        self.users = []
        self.vendors = []
        self.logged_in_user = None

    def create_user(self, user_type, username, password):
        user = User(user_type, username, password)
        self.users.append(user)

    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                return True
        return False

    def create_vendor(self, name):
        vendor = Vendor(name)
        self.vendors.append(vendor)

    def add_item_to_vendor(self, item_name, price, stock, vendor_name):
        vendor = self.find_vendor_by_name(vendor_name)
        if vendor:
            item = Item(item_name, price, stock, vendor_name)
            vendor.add_item(item)

    def view_all_items(self):
        for vendor in self.vendors:
            for item in vendor.items:
                print(f"{item.name} by {vendor.name}: ${item.price} (Stock: {item.stock})")

    def view_items_by_vendor(self, vendor_name):
        vendor = self.find_vendor_by_name(vendor_name)
        if vendor:
            for item in vendor.items:
                print(item.name, item.price, item.stock)
        else:
            print("Vendor not found.")

    def buy_item(self, item_id):
        # Code to handle item purchase, including stock management
        pass

    def find_vendor_by_name(self, name):
        for vendor in self.vendors:
            if vendor.name == name:
                return vendor
        return None

# Testing code
system = EcommerceSystem()

# Create users
system.create_user("admin", "admin1", "password1")
system.create_user("store_manager", "manager1", "password2")
system.create_user("normal_user", "user1", "password3")

# Login as admin
system.login_user("admin1", "password1")

# Create vendors
system.create_vendor("Vendor A")
system.create_vendor("Vendor B")

# Add items to vendors
system.add_item_to_vendor("Item 1", 10, 5, "Vendor A")
system.add_item_to_vendor("Item 2", 15, 3, "Vendor B")

# View all items
system.view_all_items()

# Buy an item (assuming admin is logged in)
system.buy_item(1)  # Assuming item 1 has ID 1

# # Driver's code for the above implementation
# # Create an instance of the EcommerceSystem
# system = EcommerceSystem()

# # Create users (assuming you have a secure way to get user information)
# user_type = input("Enter user type (admin, store_manager, normal_user): ")
# username = input("Enter username: ")
# password = input("Enter password: ")
# system.create_user(user_type, username, password)

# # Login user
# logged_in = system.login_user(username, password)
# if logged_in:
#     print("Login successful!")
# else:
#     print("Invalid username or password.")

# # Perform actions based on user type
# if user_type == "admin":
#     # Create vendors
#     vendor_name = input("Enter vendor name: ")
#     system.create_vendor(vendor_name)

#     # Add items to vendors
#     item_name = input("Enter item name: ")
#     price = float(input("Enter price: "))
#     stock = int(input("Enter stock: "))
#     vendor_name = input("Enter vendor name: ")
#     system.add_item_to_vendor(item_name, price, stock, vendor_name)

# elif user_type in ["admin", "store_manager"]:
#     # View items by vendor
#     vendor_name = input("Enter vendor name to view items: ")
#     system.view_items_by_vendor(vendor_name)

# # Allow all user types to view items
# choice = input("Do you want to view all items? (y/n): ")
# if choice.lower() == "y":
#     system.view_all_items()

# # Allow eligible users to buy items
# if system.logged_in_user.can_buy_item():
#     item_id = int(input("Enter item ID to buy: "))
#     system.buy_item(item_id)  # Assuming item IDs are assigned
