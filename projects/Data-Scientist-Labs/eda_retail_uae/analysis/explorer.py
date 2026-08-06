# ════════════════════════════════════════════════════
# STEP 2 — LOAD & FIRST LOOK
# ════════════════════════════════════════════════════
import pandas as pd

from config.settings import *
from data.cleaner import f_fecth_data_from_sql
from dataset.synthetic_data_generate import my_df_init

print("=" * 60)
print(f"{'UAE RETAIL EDA - ERMAN':^60}")
print(f"{'LogicMojo Batch Mars 2026':^60}")
print("=" * 60)


def data_overview(my_df_init: pd.DataFrame) -> pd.DataFrame:
    print(f"\n📦 DATA OVERVIEW")

    # 1. Vérification dynamique si le DataFrame est vide
    if my_df_init.empty:
        raise ValueError("Erman No data available")

    try:
        # 2. Informations structurelles globales
        print(f"Dimensions (Lignes, Colonnes) : {my_df_init.shape}\n")
        print(f"Liste des colonnes : {list(my_df_init.columns)}\n")
        print(f"Nombre total de lignes : {len(my_df_init):,}\n")

        # 3. Types et aperçu
        print("--- Types des colonnes ---")
        print(f"{my_df_init.dtypes}\n")
        print("--- Aperçu (3 premières lignes) ---")
        print(f"{my_df_init.head(3).to_string()}\n")

        # 4. Valeurs manquantes automatiques
        missing_value = my_df_init.isnull().sum()[my_df_init.isnull().sum() > 0]
        print("--- Valeurs manquantes détectées ---")
        print(f"{missing_value.to_string() if not missing_value.empty else 'Aucune'}\n")

        # 5. Détection et analyse dynamique des dates
        date_cols = my_df_init.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()
        if not date_cols:
            date_cols = [col for col in my_df_init.columns if 'date' in col.lower() or 'time' in col.lower()]

        if date_cols:
            print("--- Périodes temporelles détectées ---")
            for col in date_cols:
                try:
                    temp_series = pd.to_datetime(my_df_init[col])
                    print(f"  • {col} : {temp_series.min().date()} -> {temp_series.max().date()}")
                except Exception:
                    pass
            print()

        # 6. Statistiques numériques automatiques sur TOUTES les colonnes chiffrées
        numeric_df = my_df_init.select_dtypes(include='number')
        if not numeric_df.empty:
            print("--- Statistiques numériques automatiques ---")
            print(f"{numeric_df.describe().round(2)}\n")

    except Exception as e:
        print(f"Erman The error globale : ->  {e}")

    return my_df_init


# Votre code d'exécution
r_c_data_overview = data_overview(my_df_init)

print(r_c_data_overview)



def inspect_data_structure_in_360():
    pass


def f_identify_fk_pk():
    pass

def understanding_relation_between_tables():
    pass