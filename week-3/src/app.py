import menus
import menu_options
import read_write

products = []
couriers = []
orders = []

read_write.read_products(products)

read_write.read_couriers(couriers)

read_write.read_orders(orders)

user_order = {}

order_status = ["preparing", "out for delievery", "delievered"]


# For while loop, checks if the exit is False
main_exit = True
product_exit = True
orders_exit = True
couriers_exit = True

# While loop to keep the menu going until the user enters 0
while main_exit != False:
    #rests each loop variable so they can go back into the menu.
    product_exit = True
    orders_exit = True
    couriers_exit = True
    # Have to print out the menu as the return doesn't output otherwise
    print(menus.main_menu())
    user_input = input("> ")

    try:
        user_input = int(user_input)
        if (user_input == 0):
            main_exit = False

            read_write.write_products(products)

            read_write.write_couriers(couriers)

            read_write.write_orders(orders)

        elif (user_input == 1):
            while product_exit != False:
                print(menus.products_menu())
                user_input2 = int(input("> "))

                if (user_input2 == 0):
                    product_exit = False

                elif (user_input2 == 1):
                    print("\n~Products~\n")
                #Function
                    menus.list_data(products)

                elif (user_input2 == 2):
                    menu_options.new_item(products)
            
                elif (user_input2 == 3):
                    menu_options.update_item(products)

                elif (user_input2 == 4):
                    menu_options.delete_item(products)
                else:
                    print("Sorry that number doesn't exist on the menu!")

        elif (user_input == 2):
            while couriers_exit != False:
                print(menus.couriers_menu())
                user_input4 = int(input("> "))

                if (user_input4 == 0):
                    couriers_exit = False
            
                elif (user_input4 == 1):
                    menus.list_data(couriers)
            
                elif (user_input4 == 2):
                    menu_options.new_item(couriers)

                elif (user_input4 == 3):
                    menu_options.update_item(couriers)
                    
                elif (user_input4 == 4):
                    menu_options.delete_item(couriers)
            
                else:
                    print("Sorry that number doesn't exist on the menu!")

        elif (user_input == 3):

            while orders_exit != False:
                print(menus.orders_menu())
                user_input3 = int(input("> "))

                if (user_input3 == 0):
                    orders_exit = False
            
                elif (user_input3 == 1):
                    print(orders)

                elif (user_input3 == 2):
                    menu_options.new_cust_data(orders, user_order)

                elif (user_input3 == 3):
                    menu_options.update_order_status(orders)

                elif (user_input3 == 4):
                    menu_options.update_order(orders)
            
                elif (user_input3 == 5):
                    menu_options.delete_order(orders)
            
                else:
                    print("Sorry that number doesn't exist on the menu!")
        else:
            print("Sorry that number doesn't exist on the menu!")
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")