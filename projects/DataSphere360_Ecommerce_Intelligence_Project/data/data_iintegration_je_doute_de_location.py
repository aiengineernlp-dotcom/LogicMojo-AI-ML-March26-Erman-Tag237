from data.loader import r_c_fech_data_from_psql
from config.settings import *
from data.cleaner import r_c_cleaning
from analysis.explorer import f_identify_fk_pk ,understanding_relation_between_tables


def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    """
    Fully automatic data integration.
    1. Detects keys
    2. Auto-detects central table (most keys = hub)
    3. Merges all tables in 2 passes (cascade effect)
    """
    print("--- ANALYSE DE LA STRUCTURE RELATIONNELLE ---")
    print(f"📋 Tables reçues : {list(data_clean_from_sql.keys())}")
    print(r_c_cleaning.keys())

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

    # Step 5 : double pass for cascade merging
    # Pass 1 : tables directement liées à la table centrale
    # Pass 2 : tables indirectement liées (via une table déjà fusionnée)
    for passage in range(2):
        print(f"\n📌 Passage n°{passage + 1}...")
        for key_full_name, tipo in keys.items():
            table_name, col_name = key_full_name.split('.')
            if table_name not in tables_fusionnees and col_name in main_df.columns:
                print(f"✅ Fusion : {main_table_name} + {table_name} sur '{col_name}'")
                df_to_add = data_clean_from_sql[table_name]
                # Securite anti-doublons : on ne garde que les colonnes inedites
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                main_df = pd.merge(
                    main_df,
                    df_to_add[cols_to_keep],
                    on=col_name,
                    how='left'
                )
                tables_fusionnees.append(table_name)

    print(f"\n✅ SUCCESS ! Tables fusionnées : {tables_fusionnees}")
    print(f"📊 Dimensions finales : {main_df.shape}")

    return main_df


r_data_integration = data_integration(r_c_cleaning)
print(r_data_integration.isnull().sum().sort_values(ascending=False))
