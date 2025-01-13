from menus import list_id_database, list_database

def delete_courier(cursor, courier_id, menu_dict):
    # Fetches the delete_data_index from the argument after it has been converted to int
    # And uses it to parse it into a query for the database that checks if it exists
    cursor.execute('SELECT EXISTS (SELECT courier_name FROM courier WHERE courier_id = %s)' % courier_id)
    # Fetches the bool value from one
    check_row = cursor.fetchone()
    # Checks if check_row is True
    if check_row == (True,):
        # If true, it deletes the data from the database
        cursor.execute(f'DELETE FROM courier WHERE courier_id = {courier_id}')
        # Then lists what the database has in it now
        list_database(cursor, menu_dict)
    # If it can't find it, tells the user that the id doesn't exist on the table.
    else:
        print("Sorry! That ID doesn't exist on courier table!")

def new_courier(cursor, connection):
    # Asks user for name and phone number
    new_data = input("Please enter a name > ")
    phone = input("Please enter a phone number > ")

    # Set out the sql
    sql = """INSERT INTO courier (courier_name, courier_phone)
    VALUES (%s, %s)
    RETURNING courier_id, courier_name, courier_phone"""
# Creates data_values and inserts name and the phone into it
    data_values = (new_data, phone)
    # Executes it with the sql and values
    cursor.execute(sql, data_values)
    # Fetches everything that was inserted and prints it out
    rows = cursor.fetchall()
    print('Inserted = ', rows[0])
# commits it to the database
    connection.commit()

def update_courier(cursor, connection, menu_dict):
    # Uses function to list every id in the database
    list_id_database(cursor, menu_dict)
    # Asks user for input for the id
    data_id = input("\nPlease enter an index for what you wish to update > ")
    try:
        # Tries to convert it to int
        data_id = int(data_id)
        # Parses the data_id into the below statement that checks if the entry exists
        cursor.execute('SELECT EXISTS (SELECT courier_name FROM courier WHERE courier_id = %s)' % data_id)
        # Fetches only one result from the execute
        check_row = cursor.fetchone()
        # If the entry exists
        if check_row == (True,):
            # Fetches the name using the below SQL
            cursor.execute(f'SELECT courier_name FROM courier WHERE courier_id = {data_id}')
            row = cursor.fetchone()
            # Prints the name from the SQL
            print(f"Name: {row}")
            # Asks user for input of a name
            inp_update_name = input("\nPlease update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
            if (inp_update_name):
                # Converts the name to string just in case for the database
                inp_update_name = str(inp_update_name)
                # Updates the name where the id is equal to the id the user entered
                sql = """UPDATE courier SET courier_name = (%s) WHERE courier_id = (%s)"""
                # Sets value
                data_value = (inp_update_name, data_id)
                # Executes
                cursor.execute(sql, data_value)
                print("Data value updated!")
            else:
                # If not
                print("Empty string")
            # Repeats but with phone number
            cursor.execute(f'SELECT courier_phone FROM courier WHERE courier_id = {data_id}')
            row = cursor.fetchone()
            print(f"Phone: {row}")

            inp_update_phone = input(f"\nPlease update the data or hit enter if you wish to keep it the same > ")
            # Checks if there was an input
            if (inp_update_phone):
                sql = """UPDATE courier SET courier_phone = (%s) WHERE courier_id = (%s)"""
                data_value = (inp_update_phone, data_id)
                cursor.execute(sql, data_value)
                print("Data value updated!")
            else:
                # If not, continues
                print("Empty string")
            # Commits the changes to the database
            connection.commit()
        # If it can't find the entry, tells the user
        else:
            print("Sorry! That ID doesn't exist on courier table!")

# Catches the exception if it cannot convert to an int
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")