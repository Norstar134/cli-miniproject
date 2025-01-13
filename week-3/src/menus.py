def main_menu():
    return """
    Please enter a menu number for what you want:
        0 - Exit app
        1 - Product Menu
        2 - Couriers Menu
        3 - Order Menu
    """

def products_menu():
    return """
    Please enter a menu number for what you want:
        0 - Return to main menu
        1 - List of products
        2 - Create a new product
        3 - Update existing product
        4 - Delete product
    """

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

def couriers_menu():
    return """
    Please enter a menu number for what you want:
        0 - Return to main menu
        1 - List of courier
        2 - Create a new courier
        3 - Update existing courier
        4 - Delete courier
"""

def list_index(datas):
    # For loop through each index in array, which is stored into x
    # allows for each product to have their index shown
    # for x in range(len(data)):
    #     print(f"{data[x]} index is {x}")
    for i, data in enumerate(datas):
        print(f"{i} index is {data}")
    return True

def list_data(data):
    for x in range(len(data)):
        print(f"{data[x]}")
    return True