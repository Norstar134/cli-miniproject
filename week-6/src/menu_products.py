from menus import list_database, list_id_database

# Asks for cursor and connection from app.py
def new_product(cursor, connection):
    # Asks user for a new item and price, which is then converted to a float for the database
    new_data = input("Please enter a new item > ")
    price = input("Please enter a price > ")
    # Tries to convert to float
    try:
        price = float(price)

    # Sets the SQL to insert into the product table
        sql = """INSERT INTO product (product_name, product_price)
        VALUES (%s, %s)
        RETURNING product_id, product_name, product_price"""

    #Sets the data values to be inserted
        data_values = (new_data, price)
    # Executes the SQL and fetches it
        cursor.execute(sql, data_values)
        rows = cursor.fetchall()

    # Prints what was inserted
        print('Inserted = ', rows[0])

    # Commits data to database
        connection.commit()
# Throw exception if it can't convert to float.
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# As well as cursor, it asks for the product id that was asked for in the menu options along with menu_dict
def delete_product(cursor, product_id, menu_dict):
    # Checks to see if there's an entry with that ID
    cursor.execute('SELECT EXISTS (SELECT * FROM product WHERE product_id = %s)' % product_id)
    check_row = cursor.fetchone()
    # If it exists, deletes it from the database and then lists the whole table
    if check_row == (True,):
        cursor.execute(f'DELETE FROM product WHERE product_id = {product_id}')
        list_database(cursor, menu_dict)
    # Else it prints a statement telling the user that it doesn't exist
    else:
        print("Sorry! That ID doesn't exist on product table!")

# Asks the same as delete
def update_product(cursor, connection, menu_dict):
    # Lists the id of every item in the database through a function
    list_id_database(cursor, menu_dict)
    # Asks user for an ID
    data_id = input("\nPlease enter an ID for what you wish to update > ")
    try:
        # Tries to convert it to an int first
        data_id = int(data_id)
        # Checks if the id exists in the product table
        cursor.execute('SELECT EXISTS (SELECT product_name FROM product WHERE product_id = %s)' % data_id)
        check_row = cursor.fetchone()
        if check_row == (True,):
            # If it exists, executes a search for product_name
            cursor.execute('SELECT product_name FROM product WHERE product_id = %s' % data_id)
            row = cursor.fetchall()
            # Prints out the name for the user
            print(f"Name: {row}")
            # Asks user for an updated product name
            inp_update_name = input(f"\nPlease update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
            if (inp_update_name):
                # Converts input to a string, just in case
                inp_update_name = str(inp_update_name)
                # SQL query for updating the product name
                sql = """UPDATE product SET product_name = (%s) WHERE product_id = (%s)"""
                # Sets data values
                data_value = (inp_update_name, data_id)
                # Executes the SQL
                cursor.execute(sql, data_value)
                print("Data value updated!")
            else:
                # If not, continues
                print("Empty string")
            # Executes a new query, this time for product price
            cursor.execute(f'SELECT product_price FROM product WHERE product_id = {data_id}')
            row = cursor.fetchall()
            # Prints the price of what they want to update
            print(f"Price: {row}")

            # Asks user for input
            inp_update_price = input(f"\nPlease update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
            if (inp_update_price):
                try:
                    # Tries to convert input to float
                    inp_update_price = float(inp_update_price)
                    # Sets sql query
                    sql = """UPDATE product SET product_price = (%s) WHERE product_id = (%s)"""
                    # Sets data values
                    data_value = (inp_update_price, data_id)
                    # Executes sql
                    cursor.execute(sql, data_value)
                    print("Data value updated!")
                # Throws exception if it can't convert to a float
                except Exception as err:
                    print(f"Sorry! We've run into a problem: {err}")
            else:
                # If not, continues
                print("Empty string")
            # Commits to database
            connection.commit()
        # If it can't find the ID, tells the user that it doesn't exist
        else:
            print("Sorry! That ID doesn't exist on product table!")
    
    # Throws exception if it can't convert to int
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")