import pandas as pd
from sqlalchemy import create_engine

# connexion to the database
engine_erman_ds_version_2 = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce_v2')


def fetch_data_from_sql(engine_erman_connexion_to___) -> dict:
    """
    Use Case :

    param:
        -
    Args:
        -
    """

    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    tables = pd.read_sql(query, con=engine_erman_connexion_to___)['table_name'].tolist()
    all_table_from_sql = {}

    for table in tables:
        print(f"Recuperation of the table {table} in ......")
        sql_query = f'SELECT * FROM "{table}"'
        all_table_from_sql[table] = pd.read_sql(sql_query, con=engine_erman_connexion_to___)

    return all_table_from_sql


data_from_sql = fetch_data_from_sql(engine_erman_ds_version_2)


