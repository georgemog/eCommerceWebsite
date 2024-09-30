# eCommerceWebsite
A sample eCommerceWebsite for the Udemy 100 days of code using python.

### High-Level Requirements for eCommerce Website

1. **User Authentication**:
    - Implement user registration.
    - Implement user login.
    - Implement user logout.
    - Ensure password hashing for security.

2. **Product Management**:
    - Display a list of products for sale.
    - Display individual product details.
    - Admin interface to add, update, and delete products.

3. **Shopping Cart**:
    - Allow users to add products to the cart.
    - Allow users to view the cart.
    - Allow users to update the quantity of items in the cart.
    - Allow users to remove items from the cart.

4. **Checkout Process**:
    - Implement a checkout page.
    - Integrate with a payment gateway (e.g., Stripe) to process payments.
    - Ensure secure handling of payment information.
    - Display order confirmation after successful payment.

5. **Order Management**:
    - Store order details in the database.
    - Allow users to view their order history.
    - Admin interface to manage orders.

6. **User Interface**:
    - Create a responsive and user-friendly interface.
    - Ensure easy navigation between different sections of the website.

7. **Database**:
    - Use a relational database (e.g., SQLite, PostgreSQL) to store user, product, cart, and order information.
    - Ensure proper database schema design to support the above functionalities.

These high-level requirements will guide the development of the eCommerce website, ensuring it has all the necessary features and functionalities.

To run the code download the repository and run the app.py python code. The first time that it runs it will create the ecommerce.db database.
Only an admin level user has access to the /admin/product/add /admin/products pages

If you want to add some sample products run the populate_db.py
If you want to update the user so that they are admin update the set_admin.py script and run it.

