from menus import list_index, list_data, list_id_database, list_database

def delete_item(data):
    # Prints empty line for readability
    print("")
    # Prints list_index from a function
    list_index(data)

    # Asks user for index input
    delete_data_index = input("Please give me an index number to delete the item > ")
    try:
        # Tries to convert to int
        delete_data_index = int(delete_data_index)
        # Pops/deletes the data in the array
        data.pop(delete_data_index)
        # Prints the list_data
        list_data(data)
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

def update_data(data):
    # Prints list_index for array
    list_index(data)

    # Asks for user input
    data_index = input("Please enter an index for what you wish to update > ")

    try:
        # Checks if the input is an int
        data_index = int(data_index)
        # Goes to correct index the user asks for
        data_update = data[data_index]

        # Goes through each value in the dict
        for key, value in data_update.items():
            # Prints the key and value
            print(f"{key}: {value}")
            # Asks for user input
            inp_update = input(f"Please update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
            if (inp_update):
                data_update[key] = inp_update
            else:
                # If not, continues
                print("Empty string")
                continue
        # Prints the data_update dict 
        print(data_update)
        # Will throw error if it isn't an int
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# def update_data(data, prod_index, data_name, data_price):
    
#     data_update = data[prod_index]
    
#     for key, value in data_update.items():
#         if key == "name":
#             data_update[key] = data_name
#         elif key == "price":
#             data_update[key] = data_price
#     print(data_update)
    
#     return data_update

def delete_data(cursor, menu_dict):

    list_id_database(cursor, menu_dict)

    # Asks user for index input
    delete_data_index = input("Please give me an index number to delete the item > ")
    try:
        # Tries to convert to int
        delete_data_id = int(delete_data_index)
        if menu_dict == "product":
            cursor.execute('SELECT EXISTS (SELECT * FROM product WHERE product_id = %s)' % delete_data_id)
            check_row = cursor.fetchone()
            if check_row == (True,):
                cursor.execute(f'DELETE FROM product WHERE product_id = {delete_data_id}')
                list_database(cursor, menu_dict)
            else:
                print("Sorry! That ID doesn't exist on product table!")
        if menu_dict == "courier":
            cursor.execute('SELECT EXISTS (SELECT courier_name FROM courier WHERE courier_id = %s)' % delete_data_id)
            check_row = cursor.fetchone()
            if check_row == (True,):
                cursor.execute(f'DELETE FROM courier WHERE courier_id = {delete_data_id}')
                list_database(cursor, menu_dict)
            else:
                print("Sorry! That ID doesn't exist on courier table!")
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

def new_data(cursor, connection, menu_dict):

    if menu_dict == "product":
        new_data = input("Please enter a new item > ")
        price = input("Please enter a price > ")
        price = float(price)
        sql = """INSERT INTO product (product_name, product_price)
        VALUES (%s, %s)
        RETURNING product_id, product_name, product_price"""

        data_values = (new_data, price)
        cursor.execute(sql, data_values)
        rows = cursor.fetchall()
        print('insert result id = ', rows[0])

        connection.commit()

    if menu_dict == "courier":
        new_data = input("Please enter a name > ")
        phone = input("Please enter a phone number > ")

        sql = """INSERT INTO courier (courier_name, courier_phone)
        VALUES (%s, %s)
        RETURNING courier_id, courier_name, courier_phone"""

        data_values = (new_data, phone)
        cursor.execute(sql, data_values)
        rows = cursor.fetchall()
        print('insert result id = ', rows[0])

        connection.commit()

def update_database(cursor, connection, menu_dict):
    if menu_dict == "product":
        list_id_database(cursor, menu_dict)
        data_id = input("Please enter an index for what you wish to update > ")
        try:
            data_id = int(data_id)
            cursor.execute('SELECT EXISTS (SELECT product_name FROM product WHERE product_id = %s)' % data_id)
            check_row = cursor.fetchone()
            print(check_row)
            if check_row == (True,):
                cursor.execute('SELECT product_name FROM product WHERE product_id = %s' % data_id)
                row = cursor.fetchall()
                print(f"Name: {row}")
                inp_update_name = input(f"Please update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
                if (inp_update_name):
                    inp_update_name = str(inp_update_name)
                    sql = """UPDATE product SET product_name = (%s) WHERE product_id = (%s)"""
                    data_value = (inp_update_name, data_id)
                    cursor.execute(sql, data_value)
                else:
                # If not, continues
                    print("Empty string")
            
                cursor.execute(f'SELECT product_price FROM product WHERE product_id = {data_id}')
                row = cursor.fetchall()
                print(f"Price: {row}")

                inp_update_price = input(f"Please update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
                if (inp_update_price):
                    inp_update_price = float(inp_update_price)
                    sql = """UPDATE product SET product_price = (%s) WHERE product_id = (%s)"""
                    data_value = (inp_update_price, data_id)
                    cursor.execute(sql, data_value)
                else:
                # If not, continues
                    print("Empty string")
            
                connection.commit()
            else:
                print("Sorry! That ID doesn't exist on product table!")

        except Exception as err:
            print(f"Sorry! We've run into a problem: {err}")

    elif (menu_dict == "courier"):
        list_id_database(cursor, menu_dict)
        data_id = input("Please enter an index for what you wish to update > ")
        try:
            data_id = int(data_id)
            cursor.execute('SELECT EXISTS (SELECT courier_name FROM courier WHERE courier_id = %s)' % data_id)
            check_row = cursor.fetchone()
            if check_row == (True,):
                cursor.execute(f'SELECT courier_name FROM courier WHERE courier_id = {data_id}')
                row = cursor.fetchone()
                print(f"Name: {row}")
                inp_update_name = input(f"Please update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
                if (inp_update_name):
                    inp_update_name = str(inp_update_name)
                    sql = """UPDATE courier SET courier_name = (%s) WHERE courier_id = (%s)"""
                    data_value = (inp_update_name, data_id)
                    cursor.execute(sql, data_value)
                else:
                # If not, continues
                    print("Empty string")
            
                cursor.execute(f'SELECT courier_phone FROM courier WHERE courier_id = {data_id}')
                row = cursor.fetchone()
                print(f"Price: {row}")

                inp_update_phone = input(f"Please update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
                if (inp_update_phone):
                    sql = """UPDATE courier SET courier_phone = (%s) WHERE courier_id = (%s)"""
                    data_value = (inp_update_price, data_id)
                    cursor.execute(sql, data_value)
                else:
                # If not, continues
                    print("Empty string")
            
                connection.commit()
            else:
                print("Sorry! That ID doesn't exist on courier table!")


        except Exception as err:
            print(f"Sorry! We've run into a problem: {err}")