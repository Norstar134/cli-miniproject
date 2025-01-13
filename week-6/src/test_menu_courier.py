import os
import psycopg2 as psycopg
from dotenv import load_dotenv
from menu_courier import delete_courier, new_courier, update_courier

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

        def test_delete_courier():
            delete_courier_id = 3

            expected = [()]

            actual = delete_courier(cursor, delete_courier_id)
            assert expected == actual, f"expected '{expected}' got '{actual}'"

        def test_new_courier():
            new_courier_name = 'Dave'
            new_courier_phone = '078659439'

            expected = [(4, 'Dave', '078659439')]

            actual = new_courier(cursor, connection, new_courier_name, new_courier_phone)
            assert expected == actual, f"expected '{expected}' got '{actual}'"
        
        def test_update_courier():
            update_courier_id = 4
            update_courier_name = 'Shen'
            update_courier_phone = ''
            expected = [()]

            actual = update_courier(cursor, connection, update_courier_id, update_courier_name, update_courier_phone)
            assert expected == actual, f"expected '{expected}' got '{actual}'"


except Exception as ex:
    print('Failed to:', ex)