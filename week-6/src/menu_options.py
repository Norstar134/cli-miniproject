from menus import list_id_database
from menu_products import new_product, delete_product, update_product
from menu_courier import delete_courier, new_courier, update_courier

def delete_data(cursor, menu_dict):

    list_id_database(cursor, menu_dict)

    # Asks user for index input
    delete_data_index = input("Please give me an index number to delete the item > ")
    try:
        # Tries to convert to int
        delete_data_id = int(delete_data_index)
        # Checks where the user is in the menu directory to execute two different functions for their table
        if menu_dict == "product":
            delete_product(cursor, delete_data_id, menu_dict)
        elif menu_dict == "courier":
            delete_courier(cursor, delete_data_id, menu_dict)
    # Throws exception if it can't convert the input
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# Asks for cursor, connection and menu_dict from app.py
def new_data(cursor, connection, menu_dict):
# Checks which directory the user is in in the menu
    if menu_dict == "product":
# Executes either new product or new courier depending on where they are
        new_product(cursor, connection)

    elif menu_dict == "courier":
        new_courier(cursor, connection)

# Same as new_data but with update_functions
def update_database(cursor, connection, menu_dict):
    if menu_dict == "product":

        update_product(cursor, connection, menu_dict)

    elif (menu_dict == "courier"):

        update_courier(cursor, connection, menu_dict)