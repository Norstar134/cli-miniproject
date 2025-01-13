import menus
import csv
import read_write

def new_item(data):
    new_data = input("Please enter a new item > ")
    data.append(new_data)
    menus.list_data(data)

def update_item(data):
    print("")
    menus.list_index(data)
    update_data_index = input("Please give me an index number to update the item > ")

    try:
        update_data_index = int(update_data_index)
        update_data = input("Please give me a new item > ")
        data[update_data_index] = update_data
        menus.list_data(data)
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

def delete_item(data):
    print("")
    menus.list_index(data)

    delete_data_index = input("Please give me an index number to delete the item > ")
    try:
        delete_data_index = int(delete_data_index)
        data.pop(delete_data_index)
        menus.list_data(data)
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

def new_cust_data(data, cust_data):
    customer_name = input("Please enter your name > ")
    cust_data["customer_name"] = customer_name
    customer_address = input("Please enter your address > ")
    cust_data["customer_address"] = customer_address
    customer_phone_num = input("Please enter your phone number > ")
    cust_data["customer_phone"] = customer_phone_num
    cust_data["status"] = "preparing"
    data.append(cust_data)

    read_write.write_orders(data)
    
    data.clear()

    read_write.read_orders(data)
    
    cust_data.clear()
    
    print(data)

def update_order_status(data):
    menus.list_index(data)
    order_index = input("Please enter an index for the order status you wish to update > ")
    try:
        order_index = int(order_index)
        order_update = data[order_index]
        order_status = input("Please enter the new status of the order > ")
        order_update["status"] = order_status

        print(order_update)

    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")

def update_order(data):
    menus.list_index(data)

    order_index = input("Please enter an index for the order you wish to update > ")

    try:
        order_index = int(order_index)
        order_update = data[order_index]

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

def delete_order(data):
    menus.list_index(data)
    order_index = input("What order do you wish to delete? > ")
    try:
        order_index = int(order_index)
        order_delete = data[order_index]

        order_delete.clear()
        data.pop(order_index)
        print(data)
    except Exception as err:
        print(f"Sorry! We've run into a problem: {err}")