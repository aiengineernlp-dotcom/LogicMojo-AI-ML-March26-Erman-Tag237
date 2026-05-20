import pandas as pd
from sqlalchemy import create_engine
import os
import datetime
current_time = datetime.datetime.now()
pd.set_option('display.expand_frame_repr',False)

# connexion to the database
engine_erman_ds_version_2 = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5551/datasphere360_customer_ecommerce_v2')


def fect_data_from_sql(connexion_to_db) -> dict:
    print(f"{'▇' * 30} fect_data_from_sql{'▇' * 70}")
    """
    Use Case :

    param:
        -
    Args:
        -
    """
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    tables = pd.read_sql(query, con=connexion_to_db)['table_name'].tolist()
    all_raw_tables = {}

    for table in tables:
        if not table:
            raise ValueError("The table doest not exsit")
        else:
            print(f"Recuperation de la table: {table}")
            try:
                query_table = f'SELECT * FROM {table}'
                all_raw_tables[table] = pd.read_sql(query_table, con=connexion_to_db)
            except Exception as e:
                print(f'The error is {e}')

    return all_raw_tables


r_c_fect_data_from_sql = fect_data_from_sql(engine_erman_ds_version_2)
