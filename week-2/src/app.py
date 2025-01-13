import menus

products = ["Coke Cola", "Coffee", "Mocha", "Cheese Sandwich", "Cream Cheese Bagel", "Cookie"]
couriers = ["Deliveroo", "Uber Eats", "Just Eat"]

order_1 = {
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
}

order_2 = {
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
}

order_3 = {
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
}

user_order = {}

orders = [order_1, order_2, order_3]


# For while loop, checks if the exit is False
main_exit = True
product_exit = True
orders_exit = True
# While loop to keep the menu going until the user enters 0
while main_exit != False:
    #rests each loop variable so they can go back into the menu.
    product_exit = True
    orders_exit = True
    # Have to print out the menu as the return doesn't output otherwise
    print(menus.main_menu())

    user_input = int(input("> "))


    if (user_input == 0):
        main_exit = False

    elif (user_input == 1):
        while product_exit != False:
            print(menus.products_menu())
            user_input2 = int(input("> "))

            if (user_input2 == 0):
                product_exit = False

            elif (user_input2 == 1):
                print("\n~Products~\n")
                #Function
                menus.list_products(products)

            elif (user_input2 == 2):
                new_product = input("Please enter a new product > ")
                # Adds new product at the end
                products.append(new_product)
                print("\n~Products~\n")
                #function
                menus.list_products(products)
            
            elif (user_input2 == 3):
                print("")
                #function
                menus.list_product_index(products)
    
                update_product_index = input("Please give me an index number to update the product > ")
                # Trys to see if the index exists first
                try:
                    update_product_index = int(update_product_index)
                    products[update_product_index]
                    update_product = input("Please give me a new product > ")
                    # Updates the product index using the product index the user gave with the new product
                    products[update_product_index] = update_product
                    print("\n~Products~\n")
                    menus.list_products(products)
                    # If the index doesn't exists, throws and error and takes them back to the main menu
                except Exception as err:
                     print(f"Sorry! We've run into a problem: {err}")

            elif (user_input2 == 4):
                print("")
                menus.list_product_index(products)

                delete_product_index = input("Please give me an index number to delete the product > ")
                try:
                    delete_product_index = int(delete_product_index)
                    products[delete_product_index]
                    # Deletes or pops the product using the index given, 
                    # .remove("") works but only with string and if it exists in the list
                    products.pop(delete_product_index)
                    print("\n~Products~\n")
                    menus.list_products(products)
                except Exception as err:
                     print(f"Sorry! We've run into a problem: {err}")
            else:
                print("Sorry that number doesn't exist on the menu!")

    elif (user_input == 2):

        while orders_exit != False:
            print(menus.orders_menu())
            user_input3 = int(input("> "))

            if (user_input3 == 0):
                orders_exit = False
            
            elif (user_input3 == 1):
                print(orders)

            elif (user_input3 == 2):
                customer_name = input("Please enter your name > ")
                user_order["customer_name"] = customer_name
                customer_address = input("Please enter your address > ")
                user_order["customer_address"] = customer_address
                customer_phone_num = input("Please enter your phone number > ")
                user_order["customer_phone"] = customer_phone_num
                user_order["status"] = "preparing"
                orders.append(user_order)

                print(orders)

            elif (user_input3 == 3):
                menus.list_order_index(orders)

                order_index = input("Please enter an index for the order status you wish to update > ")
                try:
                    order_index = int(order_index)
                    order_update = orders[order_index]
                    order_status = input("Please enter the new status of the order > ")
                    order_update["status"] = order_status
                    print(order_update)

                except Exception as err:
                    print(f"Sorry! We've run into a problem: {err}")

            elif (user_input3 == 4):
                menus.list_order_index(orders)
                order_index = input("Please enter an index for the order you wish to update > ")

                try:
                    order_index = int(order_index)
                    order_update = orders[order_index]

                    for x, y in order_update.items():
                        print(f"{x}: {y}")
                        order_inp_update = input(f"Please update the order or hit enter if you wish to keep it the same > ")
                        if (order_inp_update == ""):
                            continue
                        else:
                            order_update[x] = order_inp_update
                    
                    print(order_update)
                except Exception as err:
                     print(f"Sorry! We've run into a problem: {err}")
            
            elif (user_input3 == 5):
                menus.list_order_index(orders)
                
                order_index = input("What order do you wish to delete? > ")
                try:
                    order_index = int(order_index)
                    order_delete = orders[order_index]

                    order_delete.clear()
                    orders.pop(order_index)
                    print(orders)
                except Exception as err:
                     print(f"Sorry! We've run into a problem: {err}")
            
            else:
                print("Sorry that number doesn't exist on the menu!")
    else:
        print("Sorry that number doesn't exist on the menu!")
