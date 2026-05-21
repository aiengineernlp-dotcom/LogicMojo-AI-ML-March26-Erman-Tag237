from fetch_data_from_sql import r_c_fect_data_from_sql
# initial exploration 
import io
def inspect_data_structure(raw_data_from_sql:dict)->dict:
    
    """

    :param raw_data_from_sql:
    :return:
    """

    structure_table_name = {}
    for table_name, df in raw_data_from_sql.items():
        if not table_name:
            raise ValueError ("Table doest not exsit ")
        else:
            try:
                #Capture de df.info() car son affichage est tres sauvage ici
                buffer = io.StringIO()
                df.info(buf = buffer ) #redirrige l'affichage vers un buffer invisible
                info_str = buffer.getvalue() # Contient le texte de info
                
                
                describe = df.describe()
                head = df.head()
                structure_table_name[table_name] = [info_str,head, describe,]
            except Exception as e:
                print(f"🚨The error is {e}")
                
    return structure_table_name

r_c_inspect_data_structure = inspect_data_structure(r_c_fect_data_from_sql)    

for table, element in r_c_inspect_data_structure.items():
    info_str,head, describe = element # logiquement les elements du dictionnaire sont [info_str,head, describe]
    print(f"DETAILS about the table : {table.upper()}\n ")
    print(info_str)
    print(head)
    print(describe)



import re
def identify_primary_foreing_key(data_fetch_from_psql: dict) -> dict | str:
    """

    :param data_fetch_from_psql:
    :return:
    """
    print(f"{'▇' * 30} identify_primary_foreing_key {'▇' * 70}")
    # patter_for_all_cols = re.compile(r'.*(id|_id|code|pk|fk|zip_code).*', re.IGNORECASE)
    # patter_for_all_cols = re.compile(r'.*(|id|_id|code|pk|fk)',re.IGNORECASE)
    # patter_for_all_cols = re.compile(r'.*(id|_id|code|pk|fk).*', re.IGNORECASE)
    patter_for_all_cols = re.compile(r'.*(_id|_code|_pk|_fk)$|^id$|zip_code|^code$', re.IGNORECASE)

    all_potentials_cols = {}
    unique_key = {}

    for table_name, df in data_fetch_from_psql.items():
        potentials_cols = [cols for cols in df.columns if patter_for_all_cols.match(cols)]
        all_potentials_cols[table_name] = potentials_cols

        for col in potentials_cols:
            is_unique = df[col].nunique() == len(
                df)  # chaque colonne est unique donc la somme des lignes est == la somme des colonnes
            key = f"{table_name}.{col}"

            type_key = "PK" if is_unique else "FK"
            unique_key[key] = type_key
            print(f" {col}  is {type_key} via {key} in {table_name.upper()} Table\n")

    return unique_key


r_c_identify_primary_foreing_key = identify_primary_foreing_key(r_c_fect_data_from_sql)
print(r_c_identify_primary_foreing_key)

import re
def understand_relationbetweentable(data_from_sql: dict) -> dict | str:
    print(f"{'▇' * 30} understand_relationbetween tables {'▇' * 70}")
    """"""
    pattern_keys = re.compile(r'.*(id|_id|code|zip_code|pk|fk)$|^id$|zip_code|^code$', re.IGNORECASE)
    dict_all_keys = {}
    for table_name, df in data_from_sql.items():
        if not table_name:
            raise ValueError("The table doest not exist ...")
        else:
            try:
                potentials_cols = [col for col in df.columns if pattern_keys.match(col)]
                for col in potentials_cols:
                    is_nunique = df[col].nunique() == len(df)  # total de ligne unique doit etre egal a la taille du df

                    key_relation = f'{table_name}.{col}' # juste pour l'affichage. on veut voir quelle colonne "cle" est liee a quelle table

                    type_key = "PK" if is_nunique else "FK" # type de la clee

                    dict_all_keys[key_relation] = type_key

                    print(f"{table_name} is a {type_key} via the relation {key_relation}")

            except Exception as e:
                # print ("🚨✅🚩❌⚠️🔍⏳▇")
                print("❌ Il ya une erreur ici c'est : ", e)

    return dict_all_keys


r_c_understand_relationbetweentable = understand_relationbetweentable(r_c_fect_data_from_sql)
print(r_c_understand_relationbetweentable)

"""
> IN THE FONCTION "understand_relationbetweentable"  CODE  WE HAVE 3 FALSES POSITIVES
1- orders is a PK via the relation orders.customer_id : SUPPOSE TO BE FK
2- reviews is a FK via the relation reviews.review_id : SUPPOSE TO BE PK 
3- order_item is a FK via the relation order_item.order_item_id : SUPPOSE TO BE PK 

nevertheless It doest not affect the pipeline because this function is separeted from the other and he is independent.
also his output is not yet used. When I will use it i will consider the false Positives observed 
"""
    
    