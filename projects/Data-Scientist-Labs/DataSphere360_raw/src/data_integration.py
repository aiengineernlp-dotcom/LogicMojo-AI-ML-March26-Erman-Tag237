from sqlalchemy import create_engine
import pandas as pd
from initial_exploration import  f_indentify_p_f_key ,understanding_relation_between_tables
from cleaning_prepro import standardize_col_name, data_clean_final

engine_erman_connexion_to__dataspere360 = create_engine(
    'postgresql://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce')


def fecth_data_from_sql(engine_erman_connexion_to__) -> dict:
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' "  # my query: I need to know what i want to collect, in this case the table names
    tables = pd.read_sql(query, con=engine_erman_connexion_to__)[
        "table_name"].tolist()  # I put them look like a list of tables
    all_data_fetch_from_sql = {}

    for table in tables:
        all_data_fetch_from_sql[table] = pd.read_sql(f'SELECT * FROM "{table}"', con=engine_erman_connexion_to__)
    return all_data_fetch_from_sql
data_fecht_from_sql = fecth_data_from_sql(engine_erman_connexion_to__dataspere360)























def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    from initial_exploration import f_indentify_p_f_key, understanding_relation_between_tables
    from cleaning_prepro import standardize_col_name, data_clean_final
    print(f"--- FUSION UNIVERSELLE INTELLIGENTE ---")
    keys = f_indentify_p_f_key(data_clean_from_sql)

    # LOGIQUE AMÉLIORÉE :
    # Au lieu de la plus longue, on cherche la table qui a le plus de clés "FK"
    # car c'est elle qui centralise les données (La Fact Table).
    fk_counts = {}
    for key_full_name, tipo in keys.items():
        if "FK" in tipo:
            table = key_full_name.split('.')[0]
            fk_counts[table] = fk_counts.get(table, 0) + 1

    # Si on ne trouve pas de FK, on prend la plus longue (plan B)
    if fk_counts:
        main_table_name = max(fk_counts, key=fk_counts.get)
    else:
        main_table_name = max(data_clean_from_sql, key=lambda x: len(data_clean_from_sql[x]))

    main_df = data_clean_from_sql[main_table_name].copy()
    tables_fusionnees = [main_table_name]

    # 3. Boucle de fusion intelligente
    for key_full_name, tipo in keys.items():
        table_name, col_name = key_full_name.split('.')

        # On fusionne si ce n'est pas la table mère et qu'on ne l'a pas déjà fait
        if table_name not in tables_fusionnees:
            # On vérifie si la colonne existe dans notre main_df pour faire le pont
            if col_name in main_df.columns:
                print(f"✅ Maillage trouvé : {main_table_name} + {table_name} sur '{col_name}'")

                df_to_add = data_clean_from_sql[table_name]

                # Sécurité pour éviter les colonnes en double (ton excellente logique)
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]

                main_df = pd.merge(
                    main_df,
                    df_to_add[cols_to_keep],
                    on=col_name,
                    how='left'
                )

                tables_fusionnees.append(table_name)

    return main_df

r_data_integration = data_integration(data_clean_final)
print(f"\nSUCCESS ! Nombre de colonnes : {len(r_data_integration.columns)}")
# print(r_data_integration.columns)

print(data_clean_final['order_item'].head())
# print(r_data_intagration.isnull().sum().sort_values(ascending=False)) # Last verification to see if null values has been created after the fusion

