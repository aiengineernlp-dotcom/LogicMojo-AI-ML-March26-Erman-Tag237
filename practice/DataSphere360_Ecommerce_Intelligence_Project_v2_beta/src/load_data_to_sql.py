import pandas as pd
from sqlalchemy import create_engine
import os
import datetime
current_time = datetime.datetime.now()

engine_erman_ds_version_2 = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce_v2')

def push_data_to_psql(file_path:str, table_name:str)->str:
    """
    Use case: This fonction will push data from my local computer to psql
    param:
        - file_path: csv_file which is my local pc
        - table_name: the name of my file in the database psql
    """

    if not file_path:
        raise FileNotFoundError (f"File need to be before any operation.")
    else:
        try:
            df = pd.read_csv(file_path) # I load data of the csv file in the Ram of my pc as a dataframe (df) object.
            table_name = os.path.splitext(os.path.basename(file_path))[0] # return only the table name
            df.to_sql(table_name, con = engine_erman_ds_version_2, index = False , if_exists = 'replace')
            what_is_up = (f" ✅ Good news bro {table_name} created at {current_time}")
        except Exception as e:
            what_is_up = (f" ❌ Bad news bro {table_name} failed to create at {current_time}. The error is: {e}")

    return what_is_up


customer = push_data_to_psql('../datasets/customers.csv', 'customers')
location = push_data_to_psql('../datasets/location.csv', 'location')
order_items = push_data_to_psql('../datasets/order_item.csv', 'order_items')
orders = push_data_to_psql('../datasets/orders.csv', 'orders')
payments = push_data_to_psql('../datasets/payments.csv', 'payments')
products = push_data_to_psql('../datasets/products.csv', 'products')
reviews = push_data_to_psql('../datasets/reviews.csv', 'reviews')
sellers = push_data_to_psql('../datasets/sellers.csv', 'sellers')

print(f"{'▇' * 5} LOAD DATA TO POSGRESQL {'▇' * 100}")
print(customer)
print(location)
print(order_items)
print(orders)
print(payments)
print(products)
print(reviews)
print(sellers)

