import pandas as pd
from sqlalchemy import create_engine
import time
import re

current_time = time.time()
# # 1. stop the automatic back to the ligne when display datasets
pd.set_option('display.expand_frame_repr', False)
# 2. display all columns
# pd.set_option('display.max_columns', None)


# -0- connection to the data base PostgreSql that i choose to use
engine_erman_connexion_to__dataspere360 = create_engine('postgresql://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce')


def fetch_data_from_psql(
        engine_erman_connexion_to___) -> dict:  # I'm using this long name just beacause i want to personalize .
    """
    USE CASE: this fuction is for fetching data from the database sql. He can be use with other database.
    Returns :
        - Dict: a dictionnary with my data inside

    """
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' "  # this is like a prompt who follows the path location of my data in postgreSQL. Im just saying that i want to SELECT all table table.schema.
    tables = pd.read_sql(query, con=engine_erman_connexion_to___)[
        'table_name'].tolist()  # After selection, I put them in the list, so i can loop in front and back
    all_data_fetch_from_sql = {}
    for table in tables:
        print(f"Recuparation of the table :{table}  -> in :{round((current_time))}s")
        # I load each table in the dictionnary with is name like a key and his value is the query sql
        all_data_fetch_from_sql[table] = pd.read_sql(f'SELECT * FROM "{table}"', con=engine_erman_connexion_to___)
        # print(all_data_fetch)
    return all_data_fetch_from_sql


fetch_dataSet = fetch_data_from_psql(engine_erman_connexion_to__dataspere360)
print(fetch_dataSet['customers'].describe())

print('\n')

def inspect_data_structure_in_360(data_from_sql: dict) -> pd.DataFrame:
    ''''
    Use case: This fuction is for inspecting data structure in 360
    it can be use to retrieve a specific data structure but in that case one additional param like 'data_table_name:str'
    need to be add to inspect_data_structure_in_360. OTHERWISE, use the curent fonction is fol all data table at once.

    :arg:
        - data_from_sql : dict
        - data_table : str
    :returns :
        - pd.DataFrame
    :errors:
        - ValueError
    '''
    for data_table in data_from_sql:
        df = data_from_sql[
            data_table]  # i collect the key of my dictiannary who will come from fetch_data_from_psql function
        print(f"{'█' * 70} ANALYSE TABLE {data_table} {'█' * 55}")
        print(df.head())
        print(df.describe())
        print(df.info())
    return df.head(), df.info(), df.describe()  # can use


my_sql_dataset = fetch_dataSet  # la capture du dictionnaire all_data_fetch_from_sql qui est ejectee dans l'espace se fait via l'appel de sa fonction
head, info, describe = inspect_data_structure_in_360(my_sql_dataset)

# DROP TABLE SECUTITY
from sqlalchemy import text

with engine_erman_connexion_to__dataspere360.connect() as conn:
    try:
        conn.execute(text(
            'DROP TABLE "../python_project_aiml_logicmojo_dataset/customers.csv" '))  # this explain more more the use of:  table_name = os.path.splitext(os.path.basename(filepath))[0]
        conn.commit()
        print(fr' ✅  Table droped')
    except Exception as e:
        print(fr"❌ Error Bro  look at {e}")

print('\n')


def identify_fk_pk(data_from_sql: dict) -> dict:
    all_data = {}
    all_key_pot_save = {}
    unique={}
    look_keys_pattern = re.compile(r'.*(id|pk|code|fk|pk).*', re.IGNORECASE)
    for data_table in data_from_sql:
        df = data_from_sql[data_table]
        all_data[data_table] = df
    # print(all_data.items())

    for data_table, df in all_data.items():  # I loop in my dictionnary
        potential_cols = [col for col in df.columns if look_keys_pattern.match(col)]  # I collect those who are fiiting my Regex pattern
        all_key_pot_save[data_table] =potential_cols

        for col in potential_cols:  # remenber that it contains for all data_table Regex match, So need to create the dictionnary or list to capture them

            is_unique = df[col].nunique() == len(df)  # since each element in the col is unique for entrie, it shoulbe egual to len(df). in that case -> I have a PK

            key = f"{data_table}.{col}"
            type_key = "PK (Primary Key)" if is_unique else "FK (Foreing Key)"
            unique[key] = type_key
            print(f"Table [{data_table}] -> Key DEtected at : {col} ({type_key})\n {'-' * 50} ")
            # all_key_pot_save[data_table] = type_key

    return unique


r = identify_fk_pk(fetch_dataSet)
print(r)


def understanding_relation_between_tables(data_set_from_sql: dict) -> dict:
    all_data = {}
    result = {}
    unique = {}
    look_keys_pattern = re.compile(r'.*(id|pk|code|fk|key|cle).*', re.IGNORECASE)

    for data_table in data_set_from_sql:
        df = data_set_from_sql[data_table]
        all_data[data_table] = df

        for data_table, df in all_data.items():
            potential_cols = [col for col in df.columns if look_keys_pattern.match(col)]
            result[data_table] = potential_cols

            for col in potential_cols:
                is_unique = df[col].nunique() == len(df)
                done = "PK" if is_unique else "FK"
                key = f"{data_table}.{col}"  # this line help to avoid loosing somme key because of collision. , also helo for the notation. if: data_table = "orders"  and col = "customer_id"  i will have -> key = "orders.customer_id"
                unique[key] = done

    return unique


c = understanding_relation_between_tables(
    fetch_dataSet)  # note que ces donnees de mon dict sont deja de type "pandas" car j'ai utiliser "pandas.read_sql" pour la recuperation lors du fetch.

print(f"❌❌❌TU EST ICI {c}")




for table_colonne_a, type_a in c.items():
    table_name_a, col_name_a = table_colonne_a.split(".")

    for table_colonne_b, type_b in c.items():
        table_name_b, col_name_b = table_colonne_b.split(".")

        if table_name_a != table_name_b and col_name_a == col_name_b:
            relation_type = "1:N" if type_a != type_b else "1:1"

            print(f"[{table_name_a}   <----------{'Connection via'}: {col_name_a}---------->   {table_name_b}]")




