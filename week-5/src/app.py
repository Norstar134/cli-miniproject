import os
import time
from menus import main_menu, products_menu, orders_menu, couriers_menu, list_data, list_database
from menu_options import delete_item, update_data, delete_data, new_data, update_database
from menu_orders import new_cust_data, update_order_status, delete_order
from read_write import write_couriers, write_products, write_orders, read
# imports psycopg2 and dotenv for database, installed through virtual env.
import psycopg2 as psycopg
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

# Need to refactor code and see if I figure out how to uses classes within it
# See if I can make it into a GUI using tkinter

# Stored in a list but each value from the files is stored as a dict.
products = []
couriers = []
orders = []

# Clears the console
clear = lambda: os.system('cls')
# Fetches a function that reads each file needed, which is then stored as a dict
# and stored in a list
read("products.csv", products)

read("couriers.csv", couriers)

read("orders.csv", orders)

# For future use
order_status = ["preparing", "out for delievery", "delievered"]

# Sorts orders list as order status with preparing stored at the top.
sorted_order = sorted(orders, key=lambda d: d["status"], reverse=True)
try:

    print("Connecting with database...")
    with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:

        cursor = connection.cursor()

# While loop to keep the menu going until the user enters 0
        while True:
    # Clears the console for the first menu, making it easier to read
            clear()
            menu_dict = "main"
    # Have to print out the menu as the return doesn't output otherwise
            print(main_menu())
            user_input = input("> ")

            try:
        # Converts user_input into int
                user_input = int(user_input)
                if (user_input == 0):
            # When exiting the program, it uses a writes function for each file.
                    write_products(products)

                    write_couriers(couriers)

                    write_orders(orders)
                    cursor.close()
                    #connection.close()

            # Ends the loop without using a variable.
                    break

                elif (user_input == 1):
                    while True:
                        menu_dict = "product"
                        clear()
                        print(products_menu())
                        user_input2 = input("> ")

                        try:
                    # Tries to convert user_input2 to int
                            user_input2 = int(user_input2)

                            if (user_input2 == 0):
                        # Ends the loop without using a variable.
                                break

                            elif (user_input2 == 1):
                                clear()
                                print("\n~Products~")
                    # Fetches the function "list_data" from menus, can be reused in every menu
                                list_database(cursor, menu_dict)
                                time.sleep(10)

                            elif (user_input2 == 2):
                                clear()
                        # Fetches the function "new_product" from menu_options
                                new_data(cursor, connection, menu_dict)
                                time.sleep(10)
            
                            elif (user_input2 == 3):
                                clear()
                        # Fetches the function "update_data" from menu_options
                                #update_data(products)
                                update_database(cursor, connection, menu_dict)
                                time.sleep(10)

                            elif (user_input2 == 4):
                                clear()
                        # Fetches the function "delete_item" from menu_options
                                #delete_item(products)
                                delete_data(cursor, menu_dict)
                                time.sleep(10)
                            else:
                                print("Sorry that number doesn't exist on the menu!")
                                time.sleep(5)

                # If it can't convert it into an int, it throws an error
                        except Exception as err:
                            print(f"Sorry! We've run into a problem: {err}")
                            time.sleep(5)

                elif (user_input == 2):
                    while True:
                        menu_dict = "courier"
                        clear()
                        print(couriers_menu())
                        user_input4 = input("> ")

                        try:
                    # Tries to convert input to int
                            user_input4 = int(user_input4)
                            if (user_input4 == 0):
                        # Ends loop
                                break
            
                            elif (user_input4 == 1):
                                clear()
                                print("\n~Couriers~")
                                list_database(cursor, menu_dict)
                                time.sleep(10)
            
                            elif (user_input4 == 2):
                                clear()
                        # Fetches new_courier from menu_options
                                new_data(cursor, connection, menu_dict)
                                time.sleep(10)

                            elif (user_input4 == 3):
                                clear()
                                update_database(cursor, connection, menu_dict)
                                time.sleep(10)
                    
                            elif (user_input4 == 4):
                                clear()
                                delete_data(cursor, menu_dict)
                                time.sleep(10)
            
                            else:
                                print("Sorry that number doesn't exist on the menu!")
                                time.sleep(5)
                # If it fails to convert to int, throws error
                        except Exception as err:
                            print(f"Sorry! We've run into a problem: {err}")
                            time.sleep(5)


                elif (user_input == 3):

                    while True:
                        menu_dict = "order"
                        clear()
                        print(orders_menu())
                        user_input3 = input("> ")

                        try:
                    # Tries to conver to int
                            user_input3 = int(user_input3)

                            if (user_input3 == 0):
                        # Ends loop
                                break
            
                            elif (user_input3 == 1):
                                clear()
                                print("\n~Orders~")
                        # Prints sorted data in a readable format
                                list_data(sorted_order)
                                time.sleep(10)

                            elif (user_input3 == 2):
                                clear()
                        # Fetches new_cust_data from menu_orders
                                new_cust_data(orders, couriers, products)
                                time.sleep(10)

                            elif (user_input3 == 3):
                                clear()
                        # Fetches update_order_status from menu_orders
                                update_order_status(orders)
                                time.sleep(10)

                            elif (user_input3 == 4):
                                clear()
                                update_data(orders)
                                time.sleep(10)
            
                            elif (user_input3 == 5):
                                clear()
                        # Fetches delete_order from menu_orders
                                delete_order(orders)
                                time.sleep(10)
            
                            else:
                                print("Sorry that number doesn't exist on the menu!")
                            time.sleep(5)
                # Throws error if it can't convert to int
                        except Exception as err:
                            print(f"Sorry! We've run into a problem: {err}")
                            time.sleep(5)

                else:
                    print("Sorry that number doesn't exist on the menu!")
                    time.sleep(5)
    # If it cannot covert user_input into int, throws an error but continues going
            except Exception as err:
                print(f"Sorry! We've run into a problem: {err}")
                time.sleep(5)
except Exception as ex:
    print('Failed to:', ex)