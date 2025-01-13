### Using structure from mini project notes

| order_id (KEY)  | customer_name     | customer_address       | customer_phone    | courier (key)    | status (key)    | items (key)    |
|-----------------|-------------------|------------------------|-------------------|-------------|------------|-----------|
| 1               | John              | Unit 2, 12 Main Street, London, WH1 2ER | 0789887334 | 2 | 1 | 1, 3, 4 |
| 2               | Jing Yuan   | The Seat of Divine Foresight | 0758583478 | 1 | 2 | 0, 5, 3 |

| order_status_id (KEY) | order_status |
|-----------------------|--------------|
| 1                     | preparing    |
| 2                     | out for delivery |
| 3                     | delivered        |

### 1NF

| order_id (KEY)  | customer_name     | customer_address       | customer_phone    | courier (key)    | status (key)    | items (key)    |
|-----------------|-------------------|------------------------|-------------------|-------------|------------|-----------|
| 1               | John              | Unit 2, 12 Main Street, London, WH1 2ER | 0789887334 | 2 | 1 | 1 |
| 1               | John              | Unit 2, 12 Main Street, London, WH1 2ER | 0789887334 | 2 | 1 | 3 |
| 1               | John              | Unit 2, 12 Main Street, London, WH1 2ER | 0789887334 | 2 | 1 | 4 |
| 2               | Jing Yuan   | The Seat of Divine Foresight | 0758583478 | 1 | 2 | 0 |
| 2               | Jing Yuan   | The Seat of Divine Foresight | 0758583478 | 1 | 2 | 5 |
| 2               | Jing Yuan   | The Seat of Divine Foresight | 0758583478 | 1 | 2 | 3 |

| order_status_id (KEY) | order_status |
|-----------------------|--------------|
| 1                     | preparing    |
| 2                     | out for delivery |
| 3                     | delivered        |

### 2NF

| order_id (KEY)  | customer_id (KEY)     | courier (key)    | status (key)    | items (key)    |
|-----------------|-----------------|------------------|-----------------|----------------|
| 1               | 1               | 2                | 1               | 1              |
| 1               | 1               | 2                | 1               | 3              |
| 1               | 1               | 2                | 1               | 4              |
| 2               | 2               | 1                | 2               | 0              |
| 2               | 2               | 1                | 2               | 5              |
| 2               | 2               | 1                | 2               | 3              |

| customer_id (KEY) | customer_name      | customer_address                        | customer_phone |
|-------------------|--------------------|-----------------------------------------|----------------|
| 1                 | John               | Unit 2, 12 Main Street, London, WH1 2ER | 0789887334     |
| 2                 | Jing Yuan          | The Seat of Divine Foresight            | 0758583478     |

| order_status_id (KEY) | order_status     |
|-----------------------|------------------|
| 1                     | preparing        |
| 2                     | out for delivery |
| 3                     | delivered        |

### 3NF

order table
| order_id (FOREIGN KEY) | courier (FOREIGN KEY)    | items (FOREIGN KEY)    |
|---------------------------------|--------------------------|------------------------|
| 1                               | 2                        | 1                      |
| 1                               | 2                        | 3                      |
| 1                               | 2                        | 4                      |
| 2                               | 1                        | 0                      |
| 2                               | 1                        | 5                      |
| 2                               | 1                        | 3                      |

customer table
| customer_id (PRIMARY KEY) | customer_name      | customer_address                        | customer_phone |
|---------------------------|--------------------|-----------------------------------------|----------------|
| 1                         | John               | Unit 2, 12 Main Street, London, WH1 2ER | 0789887334     |
| 2                         | Jing Yuan          | The Seat of Divine Foresight            | 0758583478     |

order status table
| order_status_id (PRIMARY KEY) | order_status     |
|-------------------------------|------------------|
| 1                             | preparing        |
| 2                             | out for delivery |
| 3                             | delivered        |

order id table
| order_id (PRIMARY KEY) | customer_id (FOREIGN KEY)    | status (FOREIGN KEY)  |
|------------------------|------------------------------|-----------------------|
| 1                      | 1                            | 1                     |
| 2                      | 2                            | 2                     |

### SQL Join Query:
SELECT t1.order_id, t1.courier_id, t1.product_id, t2.customer_id, t2.status_id, t3.customer_name, t3.customer_address, t3.customer_phone, t4.order_status, t5.product_name
FROM orders t1
INNER JOIN order_number t2 ON t1.order_id = t2.order_id
INNER JOIN customer t3 ON t2.customer_id = t3.customer_id
INNER JOIN order_status t4 ON t2.status_id = t4.status_id
INNER JOIN product t5 ON t1.product_id = t5.product_id

SELECT t1.order_id, t3.customer_name, t3.customer_address, t3.customer_phone, t4.order_status, t5.product_name
FROM orders t1
INNER JOIN order_number t2 ON t1.order_id = t2.order_id
INNER JOIN customer t3 ON t2.customer_id = t3.customer_id
INNER JOIN order_status t4 ON t2.status_id = t4.status_id
INNER JOIN product t5 ON t1.product_id = t5.product_id