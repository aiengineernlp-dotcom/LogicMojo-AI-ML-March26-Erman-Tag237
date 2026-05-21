import pandas as pd
from sqlalchemy import create_engine
import os
import datetime
current_time = datetime.datetime.now()
pd.set_option('display.expand_frame_repr',False)


# connexion a ma base de donnees
engine_erman_ds_version_2 = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce_v2')
if engine_erman_ds_version_2:
    print('Successfully connected to PostgreSQL database')
else:
    print('Failed to connect to PostgreSQL database')


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
# print(r_fecht_data_from_sql)


pd.set_option('display.expand_frame_repr', False)


def handle_missing_values(data_from_sql: dict) -> dict:
    treshold = 0.3
    list_more_than_30 =[]
    for table_name, df in data_from_sql.items():
        for col_name in df.columns:
            col_value = df[col_name]

            # Transformations
            is_nulls = col_value.isnull().sum()

            # more than 30% missing values
            more_than_30 = is_nulls > (treshold * len(df))
            if more_than_30:
                print(f" ❌ ❌{col_name} has  ->  {is_nulls}  missing values and it's more than 30% from the df. need to be drop off.")
                list_more_than_30.append(col_name)

                ###❌ ❌❌ ❌❌ ❌❌ ❌❌ ❌ drop the values...

            else:
                if is_nulls > 0:
                    if pd.api.types.is_numeric_dtype(col_value):
                        # -2- valueur numeriques null doivent etre remplcer par la mediane
                        col_value_to_median = col_value.median()
                        df[col_name] = col_value.fillna(col_value_to_median)
                        print(f"{col_name} has  ->  {is_nulls}  missing numerical values  has been transform to median and added to df.")

                    elif pd.api.types.is_categorical_dtype(col_value):
                        # -3- valueur categoriel null doivent etre remplcer par le mode
                        col_value_to_mode = col_value.mode()[0] # Le Mode : df.mode() retourne une Série, pas une valeur unique. Il faut utiliser .mode()[0] pour obtenir la valeur la plus fréquente.
                        df[col_name] = col_value.fillna(col_value_to_mode)
                        print(f"{col_name} has  ->  {is_nulls}  missing categorial values  has been transfomr to mode and added to df.")
                    # else:
                    #     print(f"{col_name} does not have enough values to transform to median and added to df")
                else:
                    print(f"🟢 {col_name} :  All fine for this table.")

    return data_from_sql

r_handle_missing_values = handle_missing_values(r_fecht_data_from_sql)
print(r_handle_missing_values)