import os
import psycopg2 as psycopg
from dotenv import load_dotenv
from menu_products import new_product, delete_product, update_product

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

    def test_new_product():
        new_product_name = "BLT Sandwich"
        new_product_price = 1.99

        expected = [(1, 'BLT Sandwich', 1.99)]

        actual = new_product(cursor, connection, new_product_name, new_product_price)
        assert expected == actual, f"expected '{expected}' got '{actual}'"

    def test_update_product():
        update_product_id = 14
        update_product_name = ''
        update_product_price = 2.99

        expected = [()]

        actual = update_product(cursor, connection, update_product_id, update_product_name, update_product_price)
        assert expected == actual, f"expected '{expected}' got '{actual}'"

    def test_delete_product():
        delete_product_id = 14

        expected = [()]

        actual = delete_product(cursor, delete_product_id)
        assert expected == actual, f"expected '{expected}' got '{actual}'"
    
except Exception as ex:
    print('Failed to:', ex)