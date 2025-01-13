import csv

# Writes to products file
def write_products(prod_data):
    with open("products.csv", "w", newline="") as file:
         column_names = ["name", "price"]
         writer = csv.DictWriter(file, fieldnames=column_names)
         writer.writeheader()
         writer.writerows(prod_data)

# Writes to couriers file
def write_couriers(cour_data):
    with open("couriers.csv", "w", newline="") as file:
        column_names = ["name", "phone"]
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(cour_data)

# Writes to orders file
def write_orders(ord_data):
    with open("orders.csv", "w", newline="") as file:
        column_names = ["customer_name","customer_address","customer_phone","courier","status","items"]
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(ord_data)

# Opens file that is states and asks for list
def read(file_name, list):
    try:
        # Sees if it can find the file
        with open(file_name, "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list.append(row)
    except Exception as err:
        # If it can't find the file, creates it and reads it
        with open(file_name, "w+") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list.append(row)
        print(f"File doesn't exist, creating file")