import csv

def read_products(prod_data):
    try:
        with open("products.txt", "r") as file:
            data = file.readlines()
            for line in data:
                prod_data.append(line.rstrip())
    except Exception as err:
        with open("products.txt", "w+") as file:
            data = file.readlines()
            for line in data:
                prod_data.append(line.rstrip())
        
        print(f"File doesn't exist, creating file")
    
    return prod_data

def read_couriers(cour_data):
    try:
        with open("couriers.txt", "r") as file:
            data = file.readlines()
            for line in data:
                cour_data.append(line.rstrip())
    except Exception as err:
        with open("couriers.txt", "w+") as file:
            data = file.readlines()
            for line in data:
                cour_data.append(line.rstrip())
        
        print(f"File doesn't exist, creating file")
    return cour_data

def read_orders(ord_data):
    try:
        with open("orders.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                ord_data.append(row)
    except Exception as err:
        with open("orders.csv", "w+") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                ord_data.append(row)
        print(f"File doesn't exist, creating file")
        
    return ord_data

def write_products(prod_data):
    with open("products.txt", "w") as file:
         for product in prod_data:
             file.write(f"{product}\n")

def write_couriers(cour_data):
    with open("couriers.txt", "w") as file:
         for courier in cour_data:
             file.write(f"{courier}\n")

def write_orders(ord_data):
    with open("orders.csv", "w", newline="") as file:
        column_names = ["customer_name","customer_address","customer_phone","status"]
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(ord_data)