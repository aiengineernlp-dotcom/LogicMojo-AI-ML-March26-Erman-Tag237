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


     
    
    
    