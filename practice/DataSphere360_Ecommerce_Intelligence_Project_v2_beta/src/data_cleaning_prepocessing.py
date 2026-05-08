import pandas as pd
from sqlalchemy import create_engine
import os
import datetime
current_time = datetime.datetime.now()
pd.set_option('display.expand_frame_repr',False)


# connexion a ma base de donnees
engine_erman_ds_version_2 = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce_v2')


def fecht_data_from_sql(connexion_to____) -> dict:

    """
    :useCase
    :param connexion_to____:
    :return: dict

    """

    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    tables = pd.read_sql(query, con=connexion_to____)['table_name'].tolist()
    all_raw_data_from_sql = {}
    # print(tables)

    for table_name in tables:
        # requette pour la base de donnees
        sql_query = f'SELECT * FROM "{table_name}"'

        # recuperation des donnees de la base de donnees
        df = pd.read_sql(sql_query, con=connexion_to____)
        # chargement dans le dictionnaire
        all_raw_data_from_sql[table_name] = df

    return all_raw_data_from_sql


r_fecht_data_from_sql = fecht_data_from_sql(engine_erman_ds_version_2)
print(r_fecht_data_from_sql)