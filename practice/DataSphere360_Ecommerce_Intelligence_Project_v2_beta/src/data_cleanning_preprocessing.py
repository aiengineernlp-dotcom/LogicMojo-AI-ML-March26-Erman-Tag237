import pandas as pd
from sqlalchemy import create_engine
from fetch_data_from_sql import r_c_fect_data_from_sql

#databse connexion
engine_erman_ds_version_2 = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce_v2')

if engine_erman_ds_version_2:
    print('Successfully connected to PostgreSQL database')
else:
    print('Failed to connect to PostgreSQL database')

def handle_missing_value(data_from_sql: dict) -> dict | pd.DataFrame:

    return

r_c_handle_missing_value = handle_missing_value(r_c_fect_data_from_sql)

