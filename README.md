# deanna-miniproject

## Project Background

For the mini project I had to code an application that helps a small pop-up cafe keep track of products, couriers and orders and persists the data. As well as, persisting the data, it must allow them to update and delete items.

## Client Requirements

* Wanted a collection of products and couriers
* When a customer makes a new order, it needs to be created on the system
* Wanted to be able to update the status of an order. For example, preparing, out for delivery, delivered
* When the application is exited, all data needs to be persisted
* Need to be sure the app has been tested and proven to work well
* Need regular updates

## How to Run the App

This application uses python 3.12 and Docker. Please make sure that these are installed on your system.

### Basic Set Up
* Fork or clone this repo onto your PC
* Run either python3 -m venv .venv or py -m venv .venv to create a virtual env
* Activate the venv using either .source .venv/bin/activate or .\venv\Scripts\activate
* Install the requirements using either python3 -m pip install -r requirements.txt or py -m pip install -r requirements.txt
* Navigate to week-6 with cd and then to the database folder
* Create a .env file with these variables
    * POSTGRES_HOST
    * POSTGRES_USER
    * POSTGRES_DB
    * POSTGRES_PASSWORD
* Create whatever passwords or host as you like but please use cafe for POSTGRES_DB
* Create a postgresql, adminer container in Docker using docker compose up -d, which will use the .env file
* You will need to log into adminer using the information you made in the .env file and create the database called cafe along with the following tables:
    * product - product_id (PRIMARY KEY, Interger), product_name (VARCHAR), product_price (Real)
    * courier - courier_id (PRIMARY KEY, Interger), courier_name (VARCHAR), courier_phone (VARCHAR)
    * customer - customer_id (PRIMARY KEY, Interger), customer_name (VARCHAR), customer_address (VARCHAR), customer_phone (VARCHAR)
    * order_status - order_status_id (PRIMARY KEY, Interger), order_status (VARCHAR)
    * order_number - order_id (PRIMARY KEY, Interger), customer_id (FOREIGN KEY - cusomter table), status_id (FOREIGN KEY - order_status table)
    * orders - order_id (FOREIGN KEY - order_number), courier_id (FOREIGN KEY - courier), product_id (FOREIGN KEY - product)
* Just from creating these and creating new data should be enough to get it working

### Running the application

* Use cd .. in the powershell to go back to week-6 then use cd src to get to where the application it located
* In the powershell use either python3 app.py or py app.py to run the application. It should run in the powershell/console.

When it runs, you should be able to add data into the tables by navigating the CLI menu along with updating it and deleting the data. It should also catch errors from wrong types to errors checking if a value exists on the table.

## How to run any unit tests

The only unit tests that work are within week 4. You would need to go to week-4, src to run them.

You need to make sure that the unit tests, which are at the bottom of menu_orders and menu_options, are uncommented and the actual fucntions commented out otherwise there will be conflicts with calling the functions. From there, type in either powershell or terminal py -m pytest or python3 -m pytest to see if they work.