from menu_options import new_courier, new_product, delete_item, update_data

# # Passed
def test_new_courier():
    test_couriers = [{"name": "Bob", "phone": "0789887889"},
                     {"name": "Jane", "phone": "07068954838"}]
    
    new_courier_name = "Dave"
    new_courier_phone = "07969696969"
    expected = [{"name": "Bob", "phone": "0789887889"},
                {"name": "Jane", "phone": "07068954838"},
                {"name": "Dave", "phone": "07969696969"}]
    
    actual = new_courier(test_couriers, new_courier_name, new_courier_phone)

    assert expected == actual, f"expected '{expected}' got '{actual}'"

# # Passed
def test_new_product():
    test_products = [{"name": "Apple Juice", "price": "1.99"},
                     {"name": "Coffee", "price": "2.99"},
                     {"name": "Mocha", "price": "3.50"}]
    
    new_product_name = "Cheese Sandwich"
    new_product_price = "3.50"
    expected = [{"name": "Apple Juice", "price": "1.99"},
                     {"name": "Coffee", "price": "2.99"},
                     {"name": "Mocha", "price": "3.50"},
                     {"name": "Cheese Sandwich", "price": "3.50"}]
    
    actual = new_product(test_products, new_product_name, new_product_price)

    assert expected == actual, f"expected '{expected}' got '{actual}'"

# # Passed
def test_delete_items():
    test_delete = [{"name": "Apple Juice", "price": "1.99"},
                     {"name": "Coffee", "price": "2.99"},
                     {"name": "Mocha", "price": "3.50"}]
    
    test_delete_index = 1

    expected = [{"name": "Apple Juice", "price": "1.99"},
                     {"name": "Mocha", "price": "3.50"}]
    
    actual = delete_item(test_delete, test_delete_index)

    assert expected == actual, f"expected '{expected}' got '{actual}'"

# # Passed when adding a print statement for some reason
def test_update_data():
    test_update = [{"name": "Apple Juice", "price": "1.99"},
                     {"name": "Coffee", "price": "2.99"},
                     {"name": "Mocha", "price": "3.50"}]
    
    test_update_index = 2

    test_update_name = "Cookies"
    test_update_price = "2.99"

    expected = {"name": "Cookies", "price": "2.99"}
    
    actual = update_data(test_update, test_update_index, test_update_name, test_update_price)

    assert expected == actual, f"expected '{expected}' got '{actual}'"