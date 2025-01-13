from menus import list_index, list_data
from read_write import write_orders, read

def new_cust_data(data, cour_data, prod_data):
    # Empty dict
    cust_data = {}
    # Asks user for multiple inputs for each piece of data needed
    customer_name = input("Please enter your name > ")
    cust_data["customer_name"] = customer_name
    customer_address = input("Please enter your address > ")
    cust_data["customer_address"] = customer_address
    customer_phone_num = input("Please enter your phone number > ")
    cust_data["customer_phone"] = customer_phone_num

    # Prints the courier list
    list_index(cour_data)
    # Ask user for input
    customer_courier = input("Please enter the index of the courier you want > ")

    try:
        # Tries to convert it to int
        customer_courier = int(customer_courier)
        # Goes to data in list
        cust_data["courier"] = customer_courier
    # Throws error if it can't convert
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")
    # Sets status as preparing
    cust_data["status"] = "preparing"
    # Lists product data
    list_index(prod_data)

    # Asks for input, can accept those with ,
    customer_order = input("Please enter the index of the items you want > ")
    try:
        cust_data["items"] = customer_order
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")
    
    # Appends data to list
    data.append(cust_data)
    # Write list to file
    write_orders(data)
    # Clears the list
    data.clear()
    # Re-reads data into list
    read("orders.csv", data)
    
    # Clears dict for future use
    cust_data.clear()
    # Sorts data by status
    sorted_data = sorted(data, key=lambda d: d["status"], reverse=True)

    # Prints list_data with sorted data.
    list_data(sorted_data)

# Unit test
# def new_cust_data(data, cust_name, cust_address, cust_phone, cust_courier, cust_status, cust_items):
#     # Empty dict
#     cust_data = {}
#     # Asks user for multiple inputs for each piece of data needed
#     cust_data["customer_name"] = cust_name
#     cust_data["customer_address"] = cust_address
#     cust_data["customer_phone"] = cust_phone
#     cust_data["courier"] = cust_courier
#     cust_data["status"] = cust_status
#     cust_data["items"] = cust_items

#     # Appends data to list
#     data.append(cust_data)

#     return data

def update_order_status(data):
    # Lists index of each order
    list_index(data)
    # Asks for input
    order_index = input("Please enter an index for the order status you wish to update > ")
    try:

        # Tries to convert to int
        order_index = int(order_index)
        # Tries to find the int in the list
        order_update = data[order_index]
        # Asks user to updated new status
        order_status = input("Please enter the new status of the order > ")
        # Update status
        order_update["status"] = order_status

        # Makes the dict more readable
        for key, value in order_update.items():
            print("{}: {}".format(key, value), end=" | ")
        print("")
        # Throws error if it cannot be converted or can't find order
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# Unit test
# def update_order_status(data, update_index, new_status):
#     # Lists index of each order
    
#         # Tries to find the int in the list
#         order_update = data[update_index]
#         # Asks user to updated new status
#         # Update status
#         order_update["status"] = new_status

#         return data

def delete_order(data):
    # Lists index of list
    list_index(data)
    # Asks for input
    order_index = input("What order do you wish to delete? > ")
    try:
        # Tries to convert input to int
        order_index = int(order_index)

        # Pops/deletes index from list
        data.pop(order_index)
        # Sorts the data
        sorted_data = sorted(data, key=lambda d: d["status"], reverse=True)
        # Prints the sorted data
        list_data(sorted_data)
        # Throws error if it can't convert or find index
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

# Unit test
# def delete_order(data, delete_index):
#     data.pop(delete_index)

#     return data
        