import pandas as pd
from sqlalchemy import create_engine
import re
pd.set_option('display.expand_frame_repr',False)
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


r_fetch_data_from_sql = fetch_data_from_sql(engine_erman_ds_version_2)



def inspect_structure_data(raw_data_from_sql)->dict:
    print(f" AFFICHAGES DE LA STRUCTURE DES DONNEES ")
    dict_all_data = {}
    """
    Use Case :
    :param raw_data_from_sql: 
    :return: 
    """

    for table_name, df in raw_data_from_sql.items():

        dict_all_data [table_name] = {
            "HEAD":df.head(),
            "INFO":df.info(),
            "DESCRIBE":df.describe(),
        }

    return dict_all_data

r_inspect_structure_data = inspect_structure_data(r_fetch_data_from_sql)
print(r_inspect_structure_data)



def identify_p_f_keys(raw_data_from_sql: dict) -> dict:
    print(f"{'▇' * 30} identify_p_f_keys {'▇' * 70}")

    """
    Use case : 
    params: 
    argusments:


    """

    pattern_for_keys = re.compile(r'.*(id|_id|code|pk|fk).*', re.IGNORECASE)
    all_patterns_keys = {}
    unique_keys = {}
    for table_name, df in raw_data_from_sql.items():
        # j'utilise la regex pour voir si mon pattern match
        potential_cols = [col for col in df.columns if pattern_for_keys.match(col)]
        #
        all_patterns_keys[table_name] = potential_cols

        for col in potential_cols:
            # Avec .nunique(), le nombre de fois que un element entrer est present sera sommer et la somme devrait etre egale a len(df). ou alors a 1 si on fait le ratio (df[col].nunique()/len(df))
            is_nunique = df[col].nunique() == len(df)

            key = (f"{table_name}.{col}")
            type_key = "PK" if is_nunique else "FK"

            unique_keys[key] = type_key
            print(f"Table: {table_name} -> cle detected: {key}  -> type: {type_key} ")

    return unique_keys


r_identify_p_f_keys = identify_p_f_keys(data_from_sql)
# Note : avec ce code je me dis que que je dois optimiser ma dectetion des cles car je vois dans le resultats pk ou je m'attendais a voir Fk. Est les donnees ou alors mon code? entre temps mon code est bon selon moi
print(f"{'▇' * 30} identify_p_f_keys {'▇' * 70}")
print(r_identify_p_f_keys)
