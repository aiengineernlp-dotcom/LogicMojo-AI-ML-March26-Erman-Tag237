
from DataSphere360_in_prod.config.settings import *

# data_overview
def data_overview(my_df_init: pd.DataFrame) -> dict:
    if not my_df_init:
        raise ValueError("Erman Not data availble")
    else:
        try:
            for table_name, df in my_df_init.items():
                print(f"---✅Traitement de la table: {table_name}---")
                print(df.columns)
                Shape = (f"{df.shape}"f"\n")
                print(Shape)

                # print(Shape)
                Columns = (f"{list(df.columns)}\n")
                print(Columns)
                Total_oders = (f"{len(df):,}")
                print(Total_oders)

                dtypes = (f"{df.dtypes}")
                print(dtypes)
                print("--- Aperçu (3 premières lignes) ---")
                print(f"{df.head(3).to_string()}\n")
                tree_3_first_rows = (f"{df.head(3).to_string()}")
                print(tree_3_first_rows)

                missing_value = (df.isnull().sum()[df.isnull().sum() > 0])
                print(missing_value)
                missing_value = df.isnull().sum()[df.isnull().sum() > 0]
                print("--- Valeurs manquantes détectées ---")
                print(f"{missing_value.to_string() if not missing_value.empty else 'Aucune'}\n")

                Date_Range = (f"{df['date'].min().date()}" f"  -> {df['date'].max().date()}\n")
                print(Date_Range)
                date_cols = df.select_dtypes(include=['datetime64', 'datetime']).columns.to_list()
                if not date_cols:
                    date_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
                    if date_cols:
                        print("--- Périodes temporelles détectées ---")
                        for col in date_cols:
                            try:
                                temp_series = pd.to_datetime(df[col])
                                print(f"  •{col} : {temp_series.min().date()} -> {temp_series.max().date()}")
                            except Exception as e:
                                pass
                        # print()

                numeric_stats = df[["quantity","unit_price","total_aed","rating"]].describe().round(2)
                print(numeric_stats)

                numeric_df = df.select_dtypes(include='number')

                if not numeric_df.empty:
                    print("--- Statistiques numériques automatiques ---")
                    print(f"{numeric_df.describe().round(2)}\n")
                    print()
        except Exception as e:
            print(f"Erman The error : ->  {e}")
    return my_df_init




def f_identify_fk_pk(data_fetch_from_sql:dict)->dict:
    '''
    --->>Quelles colonnes ressemblent à des clés ?
    '''
    all_data = {}
    all_key_pot_save = {}
    unique_key ={}
    # look_keys_pattern = re.compile(r'.*(id|pk|code|fk|pk).*', re.IGNORECASE)
    look_keys_pattern= re.compile(r'.*(id|_id|code|pk|fk|zip_code).*', re.IGNORECASE)
    for data_table in data_fetch_from_sql:
        df = data_fetch_from_sql[data_table] # on recupere un seul dataframe
        all_data[data_table] = df

    for data_table, df in all_data.items():
        potential_cols = [col for col in df.columns if  look_keys_pattern.match(col)]
        all_key_pot_save[data_table] = potential_cols

        for col in potential_cols:
            is_unique = df[col].nunique() == len(df)
            key = f"{data_table}.{col}"
            type_key = "PK (Primary Key)" if is_unique else "FK (Foreing Key)"
            unique_key[key] = type_key
            # print(f"Table [{data_table}] -> Key DEtected : {col} --- Type: ({type_key})\n {'-' * 50} ")
    # return unique_key, all_key_pot_save  # ou choisis ce dont tu as besoin
    return unique_key  # ou choisis ce dont tu as besoin


def understanding_relation_between_tables(data_fetch_from_sql: dict) -> dict | str:
    # look_keys_pattern = re.compile(r'.*(id|pk|code|fk|pk).*', re.IGNORECASE)
    look_keys_pattern = re.compile(r'(id|_id|code|pk|fk|zip_code)', re.IGNORECASE)
    relation_dict = {}
    if not data_fetch_from_sql:
        raise ValueError("❌ Donnees pas trouvees")
    else:
        try:
            for data_table, df in data_fetch_from_sql.items():
                potential_cols = [col for col in df.columns if look_keys_pattern.search(col)]

                for col in potential_cols:
                    is_unique = df[col].nunique() == len(df)
                    key = f"{data_table}.{col}"
                    type_key = "PK (Primary Key)" if is_unique else "FK (Foreing Key)"
                    relation_dict[key] = type_key

        except Exception as e:
            print("❌ Erreur est exactement: -> ", e)

    return relation_dict


if __name__ == "__main__":
    pass