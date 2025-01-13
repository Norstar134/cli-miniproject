# Returns main menu
def main_menu():
    return """
    Please enter a menu number for what you want:
        0 - Exit app
        1 - Product Menu
        2 - Couriers Menu
        3 - Order Menu
    """
# Returns product menu
def products_menu():
    return """
    Please enter a menu number for what you want:
        0 - Return to main menu
        1 - List of products
        2 - Create a new product
        3 - Update existing product
        4 - Delete product
    """
# Returns orders menu
def orders_menu():
    return """
    Please enter a menu number for what you want:
        0 - Return to main menu
        1 - List of orders
        2 - Customer data
        3 - Update existing order status
        4 - Update existing order
        5 - Delete order
    """
# Returns couriers menu
def couriers_menu():
    return """
    Please enter a menu number for what you want:
        0 - Return to main menu
        1 - List of courier
        2 - Create a new courier
        3 - Update existing courier
        4 - Delete courier
"""
# Function to list the id of a table
def list_id_database(cursor, menu_dict):
# uses the argument that is passed to see what menu directory the user is in
    if menu_dict == "product":
        # Executes an sql to fetch from product table
        cursor.execute('SELECT * FROM product ORDER BY product_id ASC')
        rows = cursor.fetchall()
        # Uses a for loop to print in rows with the id, name and price
        for row in rows:
            print("ID: %s, Product Name: %s, Price: %s" % row)
    # Checks if the user is in the courier menu directory
    elif menu_dict == "courier":
        # Executes sql to fetch all from the courier table
        cursor.execute('SELECT * FROM courier ORDER BY courier_id ASC')
        rows = cursor.fetchall()
        # Uses a for loop to print in rows with the id, name and phone
        for row in rows:
            print("ID: %s, Courier Name: %s, Phone: %s" % row)
    # Checks if the user is in the order menu directory
    elif menu_dict == "order":
        # Executes sql to fetch order_id, customer_name, customer_address, customer_phone, courier_name, order_stats and product name using inner joins to show everything listed
        cursor.execute('SELECT t1.order_id, t3.customer_name, t3.customer_address, t3.customer_phone, t6.courier_name, t4.order_status, t5.product_name FROM orders t1 INNER JOIN order_number t2 ON t1.order_id = t2.order_id INNER JOIN customer t3 ON t2.customer_id = t3.customer_id INNER JOIN order_status t4 ON t2.status_id = t4.status_id INNER JOIN product t5 ON t1.product_id = t5.product_id INNER JOIN courier t6 ON t1.courier_id = t6.courier_id ORDER BY t4.status_id ASC')
        rows = cursor.fetchall()
        # Uses a for loop to print in rows with the id, customer name, customer address, customer phone, courier name, order status and product name
        for row in rows:
            print("Order ID: %s, Customer Name: %s, Customer Address: %s, Customer Phone: %s, Courier Name: %s, Order Status: %s, Product Name: %s" % row)

# Function to list just the basic information of the tables, used for the first option in each menu
def list_database(cursor, menu_dict):
    # Checks if the user is in the product menu directory
    if menu_dict == "product":
         # Executes sql to fetch product name and price from the product table
        cursor.execute('SELECT product_name, product_price FROM product ORDER BY product_id ASC')
        rows = cursor.fetchall()
        # Uses a for loop to print in rows with product name, price
        for row in rows:
            print("Product Name: %s, Price: %s" % row)
    # Checks if the user is in the courier menu directory
    elif menu_dict == "courier":
        # Executes sql to fetch courier name and phone from the product table
        cursor.execute('SELECT courier_name, courier_phone FROM courier ORDER BY courier_id ASC')
        rows = cursor.fetchall()
        # Uses a for loop to print in rows with courier name, phone
        for row in rows:
            print("Courier Name: %s, Phone: %s" % row)
    # Checks if the user is in the order menu directory
    elif menu_dict == "order":
        # Executes sql to fetch order_id, customer_name, customer_address, customer_phone, courier_name, order_stats and product name using inner joins to show everything listed
        cursor.execute('SELECT t1.order_id, t3.customer_name, t3.customer_address, t3.customer_phone, t6.courier_name, t4.order_status, t5.product_name FROM orders t1 INNER JOIN order_number t2 ON t1.order_id = t2.order_id INNER JOIN customer t3 ON t2.customer_id = t3.customer_id INNER JOIN order_status t4 ON t2.status_id = t4.status_id INNER JOIN product t5 ON t1.product_id = t5.product_id INNER JOIN courier t6 ON t1.courier_id = t6.courier_id ORDER BY t4.status_id ASC')
        rows = cursor.fetchall()
        # Uses a for loop to print in rows with the id, customer name, customer address, customer phone, courier name, order status and product name
        for row in rows:
            print("Order ID: %s, Customer Name: %s, Customer Address: %s, Customer Phone: %s, Courier Name: %s, Order Status: %s, Product Name: %s" % row)