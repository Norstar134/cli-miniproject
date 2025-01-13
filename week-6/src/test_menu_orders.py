import os
import psycopg2 as psycopg
from dotenv import load_dotenv
from menu_orders import new_order, update_database_status, update_database_order, delete_database_order

load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:
    with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:

        cursor = connection.cursor()

        def test_new_order():
            new_customer_name = 'Moze'
            new_customer_address = 'Somewhere Road, Manchester'
            new_customer_phone = '076849382'
            courier_id = 2
            product_list = [1,5,7]

            expected = [()]

            actual = new_order(cursor, connection, new_customer_name, new_customer_address, new_customer_phone, courier_id, product_list)

            assert expected == actual, f"expected '{expected}' got '{actual}'"
        
        def test_update_database_status():
            update_order_id = 8
            new_order_status = 1

            expected = [()]

            actual = update_database_status(cursor, connection, update_order_id, new_order_status)
            assert expected == actual, f"expected '{expected}' got '{actual}'"

        def test_update_database_order():
            update_order_id = 8
            new_customer_name = ''
            new_customer_address = 'Somewhere Road, Manchester'
            new_customer_phone = ''
            courier_id = 2
            product_list = ''

            expected = [()]

            actual = update_database_order(cursor, connection, update_order_id, new_customer_name, new_customer_address, new_customer_phone, courier_id, product_list)
            assert expected == actual, f"expected '{expected}' got '{actual}'"

        def test_delete_order():
            delete_order_id = 4

            expected = [()]

            actual = delete_database_order(cursor, delete_order_id)
            assert expected == actual, f"expected '{expected}' got '{actual}'"

except Exception as ex:
    print('Failed to:', ex)