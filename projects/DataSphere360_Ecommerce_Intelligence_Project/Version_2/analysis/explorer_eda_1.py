
from Version_2.config.settings import *

# print("=" * 60)
# print(f"{'UAE RETAIL EDA - ERMAN':^60}")
# print(f"{'LogicMojo Batch Mars 2026':^60}")
# print("=" * 60)

# data_overview
def data_overview(my_df_init: pd.DataFrame) -> dict:
    if not my_df_init:
        raise ValueError("Erman Not data availble")
    else:
        try:
            for table_name, df in my_df_init.items():
                print(f"---✅Traitement de la table: {table_name}---")

                # 1 - Analyse structurelle automatique
                # print(df.columns)  # Affiche les colonnes de chaque table
                Shape = (f"{df.shape}"f"\n")
                # print(Shape)
                Columns = (f"{list(df.columns)}\n")
                # print(Columns)
                Total_oders = (f"{len(df):,}")
                #print(Total_oders)

                # 2 - Types de données et premier aperçu
                dtypes = (f"{df.dtypes}")
                # print(dtypes)
                # print("--- Aperçu (3 premières lignes) ---")
                # print(f"{df.head(3).to_string()}\n")
                tree_3_first_rows = (f"{df.head(3).to_string()}")
                # print(tree_3_first_rows)

                # 3- Détection dynamique des valeurs manquantes
                missing_value = (df.isnull().sum()[df.isnull().sum() > 0])
                # print(missing_value)
                missing_value = df.isnull().sum()[df.isnull().sum() > 0]
                # print("--- Valeurs manquantes détectées ---")
                # print(f"{missing_value.to_string() if not missing_value.empty else 'Aucune'}\n")

                # 4. SÉCURISATION DYNAMIQUE DES DATES
                # avant pour gerer les dates j'avais juste
                # Date_Range = (f"{df['date'].min().date()}" f"  -> {df['date'].max().date()}\n")
                # print(Date_Range)
                # APRES j'ai ceci en bas
                # Pandas cherche automatiquement toutes les colonnes de type datetime ou objet-date
                date_cols = df.select_dtypes(include=['datetime64', 'datetime']).columns.to_list()
                # Si aucune n'est typée datetime, on cherche les colonnes contenant "date" ou "time" dans leur nom
                if not date_cols:
                    date_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
                    if date_cols:
                        # print("--- Périodes temporelles détectées ---")
                        for col in date_cols:
                            try:
                                temp_series = pd.to_datetime(df[col])
                                # print(f"  •{col} : {temp_series.min().date()} -> {temp_series.max().date()}")
                            except Exception as e:
                                pass
                        # print()

                # 5. SÉCURISATION DYNAMIQUE DES STATISTIQUES NUMÉRIQUES
                # avant pour gerer les numerimeriques j'avais juste
                # numeric_stats = df[["quantity","unit_price","total_aed","rating"]].describe().round(2)
                # print(numeric_stats)

                # apres j'ai ceci en bas :
                # .select_dtypes(include='number') isole automatiquement TOUTES les colonnes numériques existantes
                numeric_df = df.select_dtypes(include='number')

                if not numeric_df.empty:
                    # print("--- Statistiques numériques automatiques ---")
                    # print(f"{numeric_df.describe().round(2)}\n")
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





# ❌ je ne vois pas l'erreur ici mais il en a. Je dois corriger et valider ce code et non celui du bas (pense a le deposer dans le groupe)
# for key_a, val_a in r_c_understanding_relation_between_tables.items():
#     table_name_a, col_name_a = key_a.split(".")

#     for key_b, val_b in r_c_understanding_relation_between_tables.items():
#         table_name_b, col_name_b = key_b.split(".")

#         if table_name_a != table_name_b and col_name_a == col_name_b:  # donc ici on a deux table differentes  et on compare les noms(key) et (val)
#             relation_type = "1:N" if val_a != val_b else "1:1"
#     print(f"[{table_name_a} <----------{'Connected via'} {col_name_a} to {table_name_b}]")
#     print(f" The relation is:  {relation_type}")


#❌✅❌✅❌✅❌✅❌✅❌✅❌✅❌✅  ICI DOIT ETTRE BIEN GERER STP CAR IL FAUT L"INTEGRER ❌✅❌✅❌✅❌✅❌✅❌✅❌✅❌✅❌✅❌✅❌✅
# for table_colonne_a, type_a in .items():
#     table_name_a, col_name_a = table_colonne_a.split(".")
#
#     for table_colonne_b, type_b in .items():
#         table_name_b, col_name_b = table_colonne_b.split(".")
#
#         if table_name_a != table_name_b and col_name_a == col_name_b:
#             print(f"[{table_name_a} <----------{'Connection via'}: {col_name_a}----------> {table_name_b}]")
#

# NOTE CL0DE T"AS DONNER UN TRUC POUR REFLECHIR SUR LA CFONCTION
###❌✅


if __name__ == "__main__":
    pass