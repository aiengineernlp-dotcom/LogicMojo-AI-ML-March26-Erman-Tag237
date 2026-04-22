import pandas as pd
from sqlalchemy import create_engine
from load_data_version_2 import push_data_file_to_sql, customers

engine = create_engine('postgresql://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce')
print(customers)
