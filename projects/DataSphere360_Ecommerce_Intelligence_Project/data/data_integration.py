from data.loader import r_c_fech_data_from_psql
from config.settings import *
from data.cleaner import r_c_cleaning
from analysis.explorer_eda_1 import f_identify_fk_pk ,understanding_relation_between_tables


def f_check_merge_cardinality(df_child: pd.DataFrame, key_col: str) -> str:
    """
    Retourne 'one' si la clé est unique dans df_child (merge direct safe),
    ou 'many' si elle est dupliquée (agrégation nécessaire avant merge).
    """
    return "one" if df_child[key_col].is_unique else "many"


def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    """
    Fully automatic data integration.
    1. Detects keys
    2. Auto-detects central table (most keys = hub)
    3. Merges all tables in 2 passes (cascade effect)
    4. Checks cardinality before each merge to avoid row duplication
    """
    print("--- ANALYSE DE LA STRUCTURE RELATIONNELLE ---")
    print(f"📋 Tables reçues : {list(data_clean_from_sql.keys())}")

    # Step 1 : detect keys
    keys = f_identify_fk_pk(data_clean_from_sql)

    # Step 2 : count keys per table to find the hub
    connexions_par_table = {}
    for key_full_name in keys.keys():
        table_name = key_full_name.split('.')[0]
        connexions_par_table[table_name] = connexions_par_table.get(table_name, 0) + 1

    print(f"📊 Clés par table : {connexions_par_table}")

    # Step 3 : central table = most keys
    main_table_name = max(connexions_par_table, key=connexions_par_table.get)
    print(f"🎯 Table centrale détectée : '{main_table_name}'")

    # Step 4 : init main dataframe
    main_df = data_clean_from_sql[main_table_name].copy()
    tables_fusionnees = [main_table_name]

    print("Lignes avant merge (table principale) :", len(main_df))  # Référence pour détecter une duplication

    # Step 5 : double pass for cascade merging
    for passage in range(2):
        print(f"\n📌 Passage n°{passage + 1}...")
        for key_full_name, tipo in keys.items():
            table_name, col_name = key_full_name.split('.')
            if table_name not in tables_fusionnees and col_name in main_df.columns:

                df_to_add = data_clean_from_sql[table_name]

                # --- Vérification de cardinalité avant merge ---
                cardinality = f_check_merge_cardinality(df_to_add, col_name)
                if cardinality == "many":
                    print(f"⚠️ '{table_name}' a plusieurs lignes par '{col_name}' → agrégation avant merge")
                    numeric_cols = df_to_add.select_dtypes(include="number").columns
                    numeric_cols = [c for c in numeric_cols if c != col_name]

                    agg_dict = {c: "sum" for c in numeric_cols}
                    df_to_add = df_to_add.groupby(col_name).agg(agg_dict).reset_index()
                    # On ajoute un compteur (ex: nb d'items par commande), utile en feature engineering
                    df_to_add[f"{table_name}_count"] = data_clean_from_sql[table_name].groupby(col_name)[col_name].transform("count").groupby(data_clean_from_sql[table_name][col_name]).first().values

                print(f"✅ Fusion : {main_table_name} + {table_name} sur '{col_name}'")

                # Securite anti-doublons : on ne garde que les colonnes inedites
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]

                n_before = len(main_df)
                main_df = pd.merge(
                    main_df,
                    df_to_add[cols_to_keep],
                    on=col_name,
                    how='left'
                )
                n_after = len(main_df)
                if n_after != n_before:
                    print(f"⚠️ ATTENTION : le merge sur '{col_name}' a changé le nb de lignes ({n_before} → {n_after})")

                tables_fusionnees.append(table_name)

    print(f"\n✅ SUCCESS ! Tables fusionnées : {tables_fusionnees}")
    print(f"📊 Dimensions finales : {main_df.shape}")
    print("Lignes après merge :", len(main_df))  # Si > au nombre initial, il reste une duplication non traitée

    return main_df


r_data_integration = data_integration(r_c_cleaning)
print(r_data_integration.isnull().sum().sort_values(ascending=False))
print(type(r_data_integration))
print("Lignes après merge :", len(r_data_integration))  # Si ce nombre est > à celui d'avant, le merge a dupliqué des lignes (relation 1-to-many mal gérée)