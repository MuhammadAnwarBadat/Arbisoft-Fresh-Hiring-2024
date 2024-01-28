# eCommerce Store Design Problem

Congratulations on being appointed as the founding CTO of the next big ecommerce startup! Your first task is to design and build the initial version of the system's functionality based on the given requirements, using Object-Oriented Design patterns.

## System Design Requirements:

The system should allow:

- **Multiple Vendors:**
  - Ability to have items from many different vendors.
  - Many different items from each vendor, with thousands of items in total.

- **User Roles:**
  - Three types of users with different permissions:
    - **normal_user:** Can view and buy items.
    - **store_manager:** Can perform tasks of a normal_user and add new items to existing vendors.
    - **admin:** Can perform tasks of a store manager, create new vendors, and new users in the system.

- **User Management:**
  - Creation and authentication of users.

- **Vendor Management:**
  - Creation of new vendors.
  - Addition of new items to vendors.

- **Item Management:**
  - Viewing items (all items, all items from a vendor, or details of a specific item using a unique identifier).
  - Tracking available stock for each item.
  - Ability to buy items while updating available stock.

## Object-Oriented Design Approach:

You should create classes and utilize object-oriented principles to address the requirements. Feel free to make assumptions, document them as part of your code, and extend the requirements if necessary.

Your program should include testing code to demonstrate that the requirements are met. There is no need to persist data to a database or file system; you can use hardcoded test data. Ensure that your final code is well-commented and readable.

Let's design and build an efficient and scalable ecommerce system together! Happy coding!