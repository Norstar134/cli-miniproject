products = ["Coke Cola", "Coffee", "Mocha", "Cheese Sandwich", "Cream Cheese Bagel", "Cookie"]
couriers = ["Deliveroo", "Uber Eats", "Just Eat"]
# For while loop, checks if the exit is 0
exit = 1
# While loop to keep the menu going until the user enters 0
while exit != 0:

    print("""
    Please enter a menu number for what you want:
        0 - Exit app
        1 - List of products
        2 - Create a new product
        3 - Update existing product
        4 - Delete product
    """)

    user_input = int(input("> "))

    if (user_input == 0):
        exit = 0

    elif (user_input == 1):
        print("\n~Products~\n")
        for x in range(len(products)):
            print(f"{products[x]}")

    elif (user_input == 2):
        new_product = input("Please enter a new product > ")
        # Adds new product at the end
        products.append(new_product)
        print("\n~Products~\n")
        for x in range(len(products)):
            print(f"{products[x]}")

    elif (user_input == 3):
        print("")
        # For loop through each index in array, which is stored into x
        # allows for each product to have their index shown
        for x in range(len(products)):
            print(f"{products[x]} index is {x}")
    
        update_product_index = int(input("Please give me an index number to update the product > "))
        # Trys to see if the index exists first
        try:
            products[update_product_index]
            update_product = input("Please give me a new product > ")
        # Updates the product index using the product index the user gave with the new product
            products[update_product_index] = update_product
            print("\n~Products~\n")
            for x in range(len(products)):
                print(f"{products[x]}")
        # If the index doesn't exists, throws and error and takes them back to the main menu
        except IndexError:
            print("Index doesn't exist!")

    elif (user_input == 4):
        print("")
        for x in range(len(products)):
            print(f"{products[x]} index is {x}")

        delete_product_index = int(input("Please give me an index number to delete the product > "))
        try:
            products[delete_product_index]
            # Deletes or pops the product using the index given, 
            # .remove("") works but only with string and if it exists in the list
            products.pop(delete_product_index)
            print("\n~Products~\n")
            for x in range(len(products)):
                print(f"{products[x]}")
        except IndexError:
            print("Index doesn't exist!")

    else:
        print("Sorry that number doesn't exist on the menu!")