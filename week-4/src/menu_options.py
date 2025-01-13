from menus import list_index, list_data
from read_write import write_products, read, write_couriers


def new_product(data):
    # Empty dict
    dict_data = {}
    # Gets two user inputs and adds them to the dict
    new_prod = input("Please enter a new item > ")
    dict_data["name"] = new_prod
    price = input("Please enter a price > ")
    dict_data["price"] = price
    # Appends the dict to the list
    data.append(dict_data)

    # To allow multiple products to be added, the appended list is writen to first
    write_products(data)

    # The list is then emptied
    data.clear()

    # The data is then re-read to the array, called data
    read("products.csv", data)

    # It then clears the dict, freeing it up for future use
    dict_data.clear()
    
    # Prints out the new data list using list_data
    list_data(data)

def new_courier(data):
    # Empty dict
    dict_data = {}
    # Asks for two inputs to add to dict
    new_cour = input("Please enter a new item > ")
    dict_data["name"] = new_cour
    phone = input("Please enter your phone number > ")
    dict_data["phone"] = phone
    # Appends to the list (data)
    data.append(dict_data)

    # Writes the appended list to file
    write_couriers(data)

    # Clears the list
    data.clear()

    # Re-reads the file into the list
    read("couriers.csv", data)
    
    # Clears the dict for further use
    dict_data.clear()
    
    # Prints the data using list_data
    list_data(data)


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
    
# Unit test

# def update_data(data, prod_index, data_name, data_price):
    
#     data_update = data[prod_index]
    
#     for key, value in data_update.items():
#         if key == "name":
#             data_update[key] = data_name
#         elif key == "price":
#             data_update[key] = data_price
#     print(data_update)
    
#     return data_update

# Unit test

# def new_courier(data, courier_name, courier_phone):
#     # Empty dict
#     dict_data = {}
#     # Asks for two inputs to add to dict
    
#     dict_data["name"] = courier_name
#     dict_data["phone"] = courier_phone
#     # Appends to the list (data)
#     data.append(dict_data)

#     return data




# def new_product(data, new_prod_name, new_prod_price):
#     # Empty dict
#     dict_data = {}
#     # Gets two user inputs and adds them to the dict

#     dict_data["name"] = new_prod_name
#     dict_data["price"] = new_prod_price
#     # Appends the dict to the list
#     data.append(dict_data)

#     return data

# # Unit test
# def delete_item(data, delete_index):

#     data.pop(delete_index)

#     return data