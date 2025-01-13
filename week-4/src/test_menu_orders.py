from menu_orders import new_cust_data, update_order_status, delete_order

# Passed
def test_new_cust_data():
    test_customers = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334",
                       "courier": "1", "status": "preparing", "items": "1, 3, 4"},
                       {"customer_name": "Jing Yuan", "customer_address": "The Seat of Divine Foresight", "customer_phone":"0758583478",
                        "courier": "0", "status": "out for delievery", "items": "0, 5, 3"}]
    
    new_cust_name = "Dave"
    new_cust_address = "Birmingham"
    new_cust_phone = "0768593829"
    new_cust_courier = "1"
    new_cust_status = "preparing"
    new_cust_items = "8, 5, 3"

    expected = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334",
                "courier": "1", "status": "preparing", "items": "1, 3, 4"},
                {"customer_name": "Jing Yuan", "customer_address": "The Seat of Divine Foresight", "customer_phone":"0758583478",
                "courier": "0", "status": "out for delievery", "items": "0, 5, 3"},
                {"customer_name": "Dave", "customer_address": "Birmingham", "customer_phone": "0768593829",
                 "courier": "1", "status": "preparing", "items": "8, 5, 3"}]
    
    actual = new_cust_data(test_customers, new_cust_name, new_cust_address, new_cust_phone, new_cust_courier, new_cust_status, new_cust_items)
    
    assert expected == actual, f"expected '{expected}' got '{actual}'"

# Passed
def test_update_order_status():
     test_customers = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334",
                "courier": "1", "status": "preparing", "items": "1, 3, 4"},
                {"customer_name": "Jing Yuan", "customer_address": "The Seat of Divine Foresight", "customer_phone":"0758583478",
                "courier": "0", "status": "out for delievery", "items": "0, 5, 3"},
                {"customer_name": "Dave", "customer_address": "Birmingham", "customer_phone": "0768593829",
                 "courier": "1", "status": "preparing", "items": "8, 5, 3"}]
     
     test_update_index = 2
     new_status = "out for delivery"

     expected = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334",
                "courier": "1", "status": "preparing", "items": "1, 3, 4"},
                {"customer_name": "Jing Yuan", "customer_address": "The Seat of Divine Foresight", "customer_phone":"0758583478",
                "courier": "0", "status": "out for delievery", "items": "0, 5, 3"},
                {"customer_name": "Dave", "customer_address": "Birmingham", "customer_phone": "0768593829",
                 "courier": "1", "status": "out for delivery", "items": "8, 5, 3"}]
     
     actual = update_order_status(test_customers, test_update_index, new_status)

     assert expected == actual, f"expected '{expected}' got '{actual}'"

# Passed
def test_delete_order():
     test_customers = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334",
                        "courier": "1", "status": "preparing", "items": "1, 3, 4"},
                        {"customer_name": "Jing Yuan", "customer_address": "The Seat of Divine Foresight", "customer_phone":"0758583478",
                        "courier": "0", "status": "out for delievery", "items": "0, 5, 3"},
                        {"customer_name": "Dave", "customer_address": "Birmingham", "customer_phone": "0768593829",
                        "courier": "1", "status": "out for delivery", "items": "8, 5, 3"}]
     
     test_delete_index = 2

     expected = [{"customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334",
                        "courier": "1", "status": "preparing", "items": "1, 3, 4"},
                        {"customer_name": "Jing Yuan", "customer_address": "The Seat of Divine Foresight", "customer_phone":"0758583478",
                        "courier": "0", "status": "out for delievery", "items": "0, 5, 3"}]
     
     actual = delete_order(test_customers, test_delete_index)

     assert expected == actual, f"expected '{expected}' got '{actual}'"