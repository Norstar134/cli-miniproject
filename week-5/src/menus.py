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
# Prints out the index of each list
def list_index(datas):
    for i in range(len(datas)):
        dict_data = datas[i]
        print(f"{i} index is:")
        for key, value in dict_data.items():
            print("{}: {}".format(key, value), end=" | ")
        print("")

# Prints out the key, value of each dict in the list
def list_data(data):
    for i in range(len(data)):
        dict_data = data[i]
        print("")
        for key, value in dict_data.items():
            print("{}: {}".format(key, value), end=" | ")
        
    print("")

def list_id_database(cursor, menu_dict):

    if menu_dict == "product":
        cursor.execute('SELECT * FROM product ORDER BY product_id ASC')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif menu_dict == "courier":
        cursor.execute('SELECT * FROM courier ORDER BY courier_id ASC')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def list_database(cursor, menu_dict):
    if menu_dict == "product":
        cursor.execute('SELECT product_name, product_price FROM product ORDER BY product_id ASC')
        rows = cursor.fetchall()
        for row in rows:
            print("Product Name: %s, Price: %s" % row)
    elif menu_dict == "courier":
        cursor.execute('SELECT courier_name, courier_phone FROM courier ORDER BY courier_id ASC')
        rows = cursor.fetchall()
        for row in rows:
            print("Courier Name: %s, Phone: %s" % row)