from config.settings import *
from data.loader import r_c_fech_data_from_psql

print("=" * 60)
print(f"{'UAE RETAIL EDA - ERMAN':^60}")
print(f"{'LogicMojo Batch Mars 2026':^60}")
print("=" * 60)

# data_overview
def data_overview(my_df_init: pd.DataFrame) -> dict:
    if not my_df_init:
        raise ValueError("Erman Not data availble")
    else:
        try:
            for table_name, df in my_df_init.items():
                print(f"---✅Traitement de la table: {table_name}---")

                # 1 - Analyse structurelle automatique
                print(df.columns)  # Affiche les colonnes de chaque table
                Shape = (f"{df.shape}"f"\n")
                print(Shape)
                Columns = (f"{list(df.columns)}\n")
                print(Columns)
                Total_oders = (f"{len(df):,}")
                print(Total_oders)

                # 2 - Types de données et premier aperçu
                dtypes = (f"{df.dtypes}")
                print(dtypes)
                print("--- Aperçu (3 premières lignes) ---")
                print(f"{df.head(3).to_string()}\n")
                tree_3_first_rows = (f"{df.head(3).to_string()}")
                print(tree_3_first_rows)

                # 3- Détection dynamique des valeurs manquantes
                missing_value = (df.isnull().sum()[df.isnull().sum() > 0])
                print(missing_value)
                missing_value = df.isnull().sum()[df.isnull().sum() > 0]
                print("--- Valeurs manquantes détectées ---")
                print(f"{missing_value.to_string() if not missing_value.empty else 'Aucune'}\n")

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
                        print("--- Périodes temporelles détectées ---")
                        for col in date_cols:
                            try:
                                temp_series = pd.to_datetime(df[col])
                                print(f"  • {col} : {temp_series.min().date()} -> {temp_series.max().date()}")
                            except Exception as e:
                                pass
                        print()

                # 5. SÉCURISATION DYNAMIQUE DES STATISTIQUES NUMÉRIQUES
                # avant pour gerer les numerimeriques j'avais juste
                # numeric_stats = df[["quantity","unit_price","total_aed","rating"]].describe().round(2)
                # print(numeric_stats)

                # apres j'ai ceci en bas :
                # .select_dtypes(include='number') isole automatiquement TOUTES les colonnes numériques existantes
                numeric_df = df.select_dtypes(include='number')

                if not numeric_df.empty:
                    print("--- Statistiques numériques automatiques ---")
                    print(f"{numeric_df.describe().round(2)}\n")
        except Exception as e:
            print(f"Erman The error : ->  {e}")
    return my_df_init


r_c_data_overview = data_overview(r_c_fech_data_from_psql)
print((r_c_data_overview))


def inspect_data_structure_in_360():
    pass


def f_identify_fk_pk():
    pass

def understanding_relation_between_tables():
    pass