def main_menu():
    return """
    Please enter a menu number for what you want:
        0 - Exit app
        1 - Product Menu
        2 - Order Menu
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

def list_product_index(products):
    # For loop through each index in array, which is stored into x
    # allows for each product to have their index shown
    for x in range(len(products)):
        print(f"{products[x]} index is {x}")

def list_products(products):
    for x in range(len(products)):
        print(f"{products[x]}")

def list_order_index(orders):
    for x in range(len(orders)):
        print(f"{orders[x]} index is {x}")