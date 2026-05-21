import pandas as pd
from sqlalchemy import create_engine

#databse connexion
engine_erman_ds_version_2 = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce_v2')

if engine_erman_ds_version_2:
    print('Successfully connected to PostgreSQL database')
else:
    print('Failed to connect to PostgreSQL database')

