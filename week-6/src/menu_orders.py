from menus import list_id_database, list_database

# Asks for cursor and connection from app.py
def new_order(cursor, connection):
    # Asks user for name, address and phone number
    customer_name = input("Please enter your name > ")
    customer_address = input("Please enter your address > ")
    customer_phone_num = input("Please enter your phone number > ")

    # Sets SQL query
    sql = """INSERT INTO customer (customer_name, customer_address, customer_phone)
    VALUES (%s, %s, %s) RETURNING customer_id"""
    # Sets data values of the data inputted
    data_values = (customer_name, customer_address, customer_phone_num)

# Executes sql
    cursor.execute(sql, data_values)
    # Sets id of customer so it can be used in other SQL queries due to normalisation
    id_of_customer = cursor.fetchone()[0]

# Sets second sql query
    sql2 = """INSERT INTO order_number (customer_id, status_id)
    VALUES (%s, %s) RETURNING order_id"""
    # Sets data value of the new customer_id and id of preparing in order_status table
    data_values2 = (id_of_customer, 1)
    cursor.execute(sql2, data_values2)
    # Stores id of the order_number for future SQL queries
    id_of_order = cursor.fetchone()[0]

# Sets the menu directory to courier to fetch everything from courier table
    menu_dict = "courier"
    # Uses the function to fetch all the ids and values
    list_id_database(cursor, menu_dict)
    # Asks user for id input
    customer_courier = input("\nPlease enter the id of the courier you want > ")
    # Sets menu directory for product to do the same as courier
    menu_dict = "product"
    list_id_database(cursor, menu_dict)
    # Asks for user input for ID
    customer_order = input("\nPlease enter the id of the items you want > ")
    # Splits the list given into a list to loop through
    customer_order = customer_order.split(",")
    try:
        # Tries to convert courier ID
        customer_courier = int(customer_courier)
        # Checks to see if the courier ID exists in the table
        cursor.execute('SELECT EXISTS (SELECT courier_name FROM courier WHERE courier_id = %s)' % customer_courier)
        check_row = cursor.fetchone()
        if check_row == (True,):
            # If its true, loops through the order list
            for order in customer_order:
                # Checks to see if each one exists on the table
                cursor.execute('SELECT EXISTS (SELECT product_name FROM product WHERE product_id = %s)' % order)
                check_row = cursor.fetchone()
                if check_row == (True,):
                    # If so, sets sql, data values and then executes them into the table
                    sql = """INSERT INTO orders (order_id, courier_id, product_id)
                    VALUES (%s, %s, %s)"""
                    data_values = (id_of_order, customer_courier, order)
                    cursor.execute(sql, data_values)
                else:
                    print("Sorry! That ID doesn't exist on the product table!")

        # Otherwise lets the user know that it doesn't exist
        else:
            print("Sorry! That ID doesn't exist on courier table!")
        
        connection.commit()
        # Sets menu directory to order to list the new order
        menu_dict = "order"
        list_database(cursor, menu_dict)

    # Errors if it can't convert the data to int
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# Same arguements as new customer with menu_dict
def update_database_status(cursor, connection, menu_dict):
    # Uses function to list all the ids in the database
    list_id_database(cursor, menu_dict)
    # Asks user for ID
    order_id = input("\nPlease enter an id for the order status you wish to update > ")
    print("")
    try:
        # tries to convert it to an int
        order_id = int(order_id)
        # Checks to see if the id exists on order_number, where the order_status is stored
        cursor.execute('SELECT EXISTS (SELECT * FROM order_number WHERE order_id = %s)' % order_id)
        check_row = cursor.fetchone()
        if check_row == (True,):
            # If it can, selects all
            cursor.execute('SELECT * FROM order_status')
            rows = cursor.fetchall()
            # For each row in table, prints out the id and status
            for row in rows:
                print("Order Status ID: %s, Status: %s" % row)
            
            # Asks for new ID input
            order_status = input("\nPlease enter the ID for the new status of the order > ")
            try:
                # Tries to convert it to int
                order_status = int(order_status)
                # Checks to see if the ID exists
                cursor.execute('SELECT EXISTS (SELECT * FROM order_status WHERE status_id = %s)' % order_status)
                check_row = cursor.fetchone()
                if check_row == (True,):
                    # If it does, sets the sql query, data values, executes and then commits it.
                    sql = """UPDATE order_number SET status_id = (%s) WHERE order_id = (%s)"""
                    data_values = (order_status, order_id)
                    cursor.execute(sql, data_values)
                    connection.commit()
                    print("Data value updated!")
                # Otherwise, tells user it doesn't exist
                else:
                    print("Sorry! That ID doesn't exist on courier table!")
            # Both times it check if an input couldn't be converted, throws an exception
            except Exception as err:
                print(f"Sorry! We've run into a problem: {err}")
        else:
            print("Sorry! That ID doesn't exist on courier table!")
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# Needs just cursor and menu dict
def delete_database_order(cursor, menu_dict):
    # Uses function to print all the data in the table needed
    list_id_database(cursor, menu_dict)
    # Asks for user input
    order_index = input("\nWhat order do you wish to delete? > ")
    try:
        # Tries to convert input to int
        order_index = int(order_index)
        # Checks to see if it exists
        cursor.execute('SELECT EXISTS (SELECT * FROM orders WHERE order_id = %s)' % order_index)
        check_row = cursor.fetchone()
        if check_row == (True,):
            # If it exists, executes data from both orders and order number
            cursor.execute(f'DELETE FROM orders WHERE order_id = {order_index}')
            # Lists new table structure
            list_database(cursor, menu_dict)
        # If it doesn't exist, lets user know
        else:
            print("Sorry! That ID doesn't exist on courier table!")
    # Throws exception if it can't convert to int
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

def update_database_order(cursor, connection, menu_dict):
    # Lists IDs from orders database
    list_id_database(cursor, menu_dict)

    # Asks user for input
    data_id = input("\nPlease enter an ID for what you wish to update > ")

    try:
        # Tries to convert it to int
        data_id = int(data_id)
        # Checks to see if it exists on the table
        cursor.execute('SELECT EXISTS (SELECT * FROM orders WHERE order_id = %s)' % data_id)
        check_row = cursor.fetchone()
        if check_row == (True,):
            # If so, shows the name of the customer from the customer table, where the customer_id matches that on order_number
            cursor.execute("""SELECT t1.customer_name FROM customer t1
                           INNER JOIN order_number t2 ON t1.customer_id = t2.customer_id
                           WHERE t2.order_id = %s""" % data_id)
            row = cursor.fetchone()
            # Replaces everything for it to be a normal string so it can be updated in the table
            row = str(row).replace('(','').replace(',','').replace(')', '').replace("'", "")
            # Prints the customer name
            print(f"Customer Name: {row}")
            # Asks user for an input
            inp_update_name = input("\nPlease update the data or hit enter if you wish to keep it the same > ")
            if (inp_update_name):
                # If there's an input, converts name to string, sets sql query, set data values and executes the sql
                inp_update_name = str(inp_update_name)
                sql = """UPDATE customer SET customer_name = (%s) WHERE customer_name = (%s)"""
                data_values = (inp_update_name, row)
                cursor.execute(sql, data_values)
                print("Data value updated!")
            else:
                # Otherwise prints an acknowledgement of an empty string
                print("Empty string")
            
            # Fetches the customer address while checking if the order ids match
            cursor.execute("""SELECT t1.customer_address FROM customer t1
                           INNER JOIN order_number t2 ON t1.customer_id = t2.customer_id
                           WHERE t2.order_id = %s""" % data_id)
            row = cursor.fetchone()
            # Makes it a normal string so it can be updated in the table
            row = str(row).replace('(','').replace(',','').replace(')', '').replace("'", "")
            # Prints address row
            print(f"Customer Address: {row}")
            # Asks user for input
            inp_update_address = input("\nPlease update the data or hit enter if you wish to keep it the same > ")

            if (inp_update_address):
                # If there's an input, converts it to string, sets sql, sets data values and executes the sql
                inp_update_address = str(inp_update_address)
                sql = """UPDATE customer SET customer_address = (%s) WHERE customer_address = (%s)"""
                data_values = (inp_update_address, row)
                cursor.execute(sql, data_values)
                print("Data value updated!")
            else:
                # If it's empty, prints Empty string
                print("Empty string")
            
            # Again, fetches customer phone while comparing the order_id
            cursor.execute("""SELECT t1.customer_phone FROM customer t1
                           INNER JOIN order_number t2 ON t1.customer_id = t2.customer_id
                           WHERE t2.order_id = %s""" % data_id)
            row = cursor.fetchone()
            # Makes it into a normal string that can be used in an SQL query
            row = str(row).replace('(','').replace(',','').replace(')', '').replace("'", "")
            # Prints phone number
            print(f"Customer Phone: {row}")
            # Asks user for input
            inp_update_phone = input(f"\nPlease update the data or hit enter if you wish to keep it the same > ")
            if (inp_update_phone):
                # If there's an input, converts it to a string, sets sql, sets data values, executes the sql
                inp_update_phone = str(inp_update_phone)
                sql = """UPDATE customer SET customer_address = (%s) WHERE customer_address = (%s)"""
                data_values = (inp_update_phone, row)
                cursor.execute(sql, data_values)
                print("Data value updated!")
            else:
                print("Empty string")

            # Sets menu_dict to courier to access courier database easily
            menu_dict = "courier"
            
            # Executes a search for courier_id on the orders table while checking the courier table for the same id 
            # where the order_id is what they entered at the start
            cursor.execute("""SELECT t1.courier_id FROM orders t1
                           INNER JOIN courier t2 ON t1.courier_id = t2.courier_id
                           WHERE t1.order_id = %s""" % data_id)
            row = cursor.fetchone()
            # Makes it into a normal string that can be used
            row = str(row).replace('(','').replace(',','').replace(')', '').replace("'", "")
            # Prints courier ID
            print(f"Courier ID: {row}")
            # Uses a function to easily access the id of all the entries in the table
            list_id_database(cursor, menu_dict)

            # Asks user for input
            inp_update_courier_id = input(f"\nPlease update the courier ID or hit enter if you wish to keep it the same > ")
            if (inp_update_courier_id):
                try:
                    # If there's an input, tries to convert it to int, checks if it exists in the courier table
                    inp_update_courier_id = int(inp_update_courier_id)
                    check_row2 = cursor.execute('SELECT EXISTS (SELECT * FROM courier WHERE courier_id = %s)' % inp_update_courier_id)
                    if check_row2 == (True,):
                        # If it exists, sets sql, sets data values and executes the sql
                        sql = """UPDATE orders SET courier_id = (%s) WHERE order_id = (%s)"""
                        data_values = (inp_update_courier_id, data_id)
                        cursor.execute(sql, data_values)
                        print("Data value updated!")
                    else:
                    # Otheriwse, tells user it doesn't exist
                        print("Sorry! That ID doesn't exist on courier table!")

                # If it can't convert to int, throws exception
                except Exception as err:
                    print(f"Sorry! We've run into a problem: {err}")
            
            else:
                print("Empty string")
            
            # Lastly, fetches all the products from the orders table where the order_id is the same as the one they entered
            cursor.execute("""SELECT t1.product_id FROM orders t1
                           INNER JOIN product t2 ON t1.product_id = t2.product_id
                           WHERE t1.order_id = %s""" % data_id)
            rows = cursor.fetchall()
            # Sets menu directory to product to access product table
            menu_dict = "product"
            # Prints the ids of the product table
            list_id_database(cursor, menu_dict)
            # Goes through the result in the result from the search, sets the id and makes it usable later using .replace
            for row in rows:
                id = row
                id = str(id).replace('(','').replace(')', '').replace("'", "").replace(",", "")
                print(f"Product ID: {id}")
                # Asks for user input
                inp_update_product_id = input(f"\nPlease update the product ID or hit enter if you wish to keep it the same > ")

                if(inp_update_product_id):
                    try:
                        # If there's an input, tries to convert it to int, checks if the id exists in product
                        inp_update_product_id = int(inp_update_product_id)
                        check_row2 = cursor.execute('SELECT EXISTS (SELECT * FROM product WHERE product_id = %s)' % inp_update_product_id)
                        if check_row2 == (True,):
                            # If it exists, sets sql, sets data values and executes it
                            sql = """UPDATE orders SET product_id = (%s) WHERE product_id = (%s) AND order_id = (%s)"""
                            data_values = (inp_update_product_id, id, data_id)
                            cursor.execute(sql, data_values)
                            print("Data value updated!")
                        else:
                            # Otherwise tells the user it doesn't exist
                            print("Sorry! That ID doesn't exist on product table!")
                    # Throws exception if it can't convert to int
                    except Exception as err:
                        print(f"Sorry! We've run into a problem: {err}")
            
        # Commits it to the database
        connection.commit()

# Throws error if it can't convert to int
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")