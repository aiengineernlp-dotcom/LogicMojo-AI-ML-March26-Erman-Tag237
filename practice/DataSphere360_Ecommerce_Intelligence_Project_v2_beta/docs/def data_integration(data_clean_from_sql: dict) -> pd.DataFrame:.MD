## def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:

## UNIVERSAL 100/100 

# def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
#     print(f"--- FUSION UNIVERSELLE INTELLIGENTE ---")
#     keys = f_indentify_p_f_key(data_clean_from_sql)
    
#     # LOGIQUE AMÉLIORÉE : 
#     # Au lieu de la plus longue, on cherche la table qui a le plus de clés "FK" 
#     # car c'est elle qui centralise les données (La Fact Table).
#     fk_counts = {}
#     for key_full_name, tipo in keys.items():
#         if "FK" in tipo:
#             table = key_full_name.split('.')[0]
#             fk_counts[table] = fk_counts.get(table, 0) + 1
    
#     # Si on ne trouve pas de FK, on prend la plus longue (plan B)
#     if fk_counts:
#         main_table_name = max(fk_counts, key=fk_counts.get)
#     else:
#         main_table_name = max(data_clean_from_sql, key=lambda x: len(data_clean_from_sql[x]))
        
#     main_df = data_clean_from_sql[main_table_name].copy()
#     tables_fusionnees = [main_table_name]

#     # 3. Boucle de fusion intelligente
#     for key_full_name, tipo in keys.items():
#         table_name, col_name = key_full_name.split('.')
        
#         # On fusionne si ce n'est pas la table mère et qu'on ne l'a pas déjà fait
#         if table_name not in tables_fusionnees:
#             # On vérifie si la colonne existe dans notre main_df pour faire le pont
#             if col_name in main_df.columns:
#                 print(f"✅ Maillage trouvé : {main_table_name} + {table_name} sur '{col_name}'")
                
#                 df_to_add = data_clean_from_sql[table_name]
                
#                 # Sécurité pour éviter les colonnes en double (ton excellente logique)
#                 cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                
#                 main_df = pd.merge(
#                     main_df, 
#                     df_to_add[cols_to_keep], 
#                     on=col_name, 
#                     how='left'
#                 )
                
#                 tables_fusionnees.append(table_name)
            
#     return main_df

# r_data_integration = data_integration(data_clean_final)
# print(f"\nSUCCESS ! Nombre de colonnes : {len(r_data_integration.columns)}")
# # print(r_data_integration.columns)

# print(data_clean_final['order_item'].head())
# print(r_data_intagration.isnull().sum().sort_values(ascending=False)) # Last verification to see if null values has been created after the fusion



------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------- CODE 2 WITH NO COMMENTS-----------------------------------------------------------------------------------------------------------

## UNIVERSAL 100/100  et  100/100

def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    print(f"--- ANALYSE DE LA STRUCTURE ---")
    keys = f_indentify_p_f_key(data_clean_from_sql)
    
    # --- LOGIQUE DE DÉCISION AUTOMATIQUE ---
    # On compte combien de clés différentes chaque table possède
    connexions_par_table = {}
    for key_full_name in keys.keys():
        table_name = key_full_name.split('.')[0]
        connexions_par_table[table_name] = connexions_par_table.get(table_name, 0) + 1
    
    # On choisit la table qui a le plus de "portes d'entrée/sortie" (le Hub)
    # Dans ton cas, ce sera 'orders' ou 'order_item'
    main_table_name = max(connexions_par_table, key=connexions_par_table.get)
    
    print(f"📍 Table principale détectée automatiquement : '{main_table_name}'")
    # ----------------------------------------

    main_df = data_clean_from_sql[main_table_name].copy()
    tables_fusionnees = [main_table_name]

    # Double passage pour l'effet domino (pour arriver aux 39 colonnes)
    for _ in range(2):
        for key_full_name, tipo in keys.items():
            table_name, col_name = key_full_name.split('.')
            if table_name not in tables_fusionnees and col_name in main_df.columns:
                print(f"✅ Fusion : {table_name} via '{col_name}'")
                df_to_add = data_clean_from_sql[table_name]
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                main_df = pd.merge(main_df, df_to_add[cols_to_keep], on=col_name, how='left')
                tables_fusionnees.append(table_name)
            
    return main_df

r_data_integration = data_integration(data_clean_final)
print(f"\nSUCCESS ! Nombre de colonnes : {len(r_data_integration.columns)}")
# print(r_data_integration.columns)

print(data_clean_final['order_item'].head())
print(r_data_intagration.isnull().sum().sort_values(ascending=False)) # Last verification to see if null values has been created after the fusion

------------------------------------------------------------- CODE 2 WITH COMMENTS-----------------------------------------------------------------------------------------------------------
def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    """
    Intègre dynamiquement toutes les tables d'un dictionnaire en un DataFrame unique.
    
    Logique :
    1. Identifie les relations (clés) entre les tables.
    2. Détecte la table 'Hub' (celle qui a le plus de connexions) comme table mère.
    3. Fusionne les tables satellites en deux passages pour gérer les relations indirectes.
    """
    print(f"--- ANALYSE DE LA STRUCTURE RELATIONNELLE ---")
    
    # Récupération du dictionnaire des clés (PK/FK) via l'analyseur universel
    keys = f_indentify_p_f_key(data_clean_from_sql)
    
    # --- DÉCISION AUTOMATIQUE DE LA TABLE SOURCE ---
    # On calcule la centralité de chaque table (nombre de clés ID qu'elle possède)
    connexions_par_table = {}
    for key_full_name in keys.keys():
        table_name = key_full_name.split('.')[0]
        connexions_par_table[table_name] = connexions_par_table.get(table_name, 0) + 1
    
    # La table principale est celle qui sert de point de ralliement (le plus d'IDs)
    main_table_name = max(connexions_par_table, key=connexions_par_table.get)
    print(f"📍 Point d'ancrage détecté : '{main_table_name}'")

    # Initialisation du DataFrame final avec une copie de la table mère
    main_df = data_clean_from_sql[main_table_name].copy()
    tables_fusionnees = [main_table_name]

    # --- MOTEUR DE FUSION EN CASCADE (2 PASSAGES) ---
    # Le double passage permet de lier des tables qui n'ont pas de lien direct 
    # avec la table mère, mais qui sont liées à une table déjà fusionnée.
    for passage in range(2):
        print(f"Passage n°{passage + 1}...")
        for key_full_name, tipo in keys.items():
            table_name, col_name = key_full_name.split('.')
            
            # Si la table n'est pas encore fusionnée ET qu'un pont (col_name) existe dans le main_df
            if table_name not in tables_fusionnees and col_name in main_df.columns:
                print(f"✅ Fusion de {table_name} via le pont '{col_name}'")
                
                df_to_add = data_clean_from_sql[table_name]
                
                # SÉCURITÉ ANTI-DOUBLONS : On ne prend que les colonnes inédites
                # Cela évite les suffixes _x et _y qui polluent le DataFrame
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                
                main_df = pd.merge(
                    main_df, 
                    df_to_add[cols_to_keep], 
                    on=col_name, 
                    how='left'
                )
                
                # On marque la table comme intégrée pour ne pas la traiter deux fois
                tables_fusionnees.append(table_name)
            
    return main_df

# --- EXÉCUTION DU PIPELINE ---
r_data_integration = data_integration(data_clean_final)

print(f"\n🚀 INTÉGRATION RÉUSSIE ! Total colonnes : {len(r_data_integration.columns)}")

# Vérification finale des valeurs manquantes générées par les jointures (Join Quality)
print(r_data_integration.isnull().sum().sort_values(ascending=False))

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------









## UNIVERSEL MAIS BASER sur la TABLE FUSION  ici orders   CODE 1

def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    print(f"--- FUSION BASÉE SUR TES CLÉS (SÉCURISÉE) ---")
    keys = f_indentify_p_f_key(data_clean_from_sql)
    
    main_df = data_clean_from_sql["orders"].copy() 
    tables_fusionnees = []

    for key_full_name, tipo in keys.items():
        table_name, col_name = key_full_name.split('.')
        
        if table_name != "orders" and table_name not in tables_fusionnees:
            if col_name in main_df.columns:
                print(f"✅ Fusion unique : orders + {table_name} sur la colonne {col_name}")
                
                # --- LOGIQUE DE NETTOYAGE ---
                # On ne garde de la nouvelle table que la clé et les colonnes qu'on n'a pas encore
                df_to_add = data_clean_from_sql[table_name]
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                
                main_df = pd.merge(
                    main_df, 
                    df_to_add[cols_to_keep], # On ne fusionne que le nécessaire
                    on=col_name, 
                    how='left'
                )
                
                tables_fusionnees.append(table_name)
            
         
    return main_df



r_data_integration = data_integration(data_clean_final)
print(f"\nSUCCESS ! Nombre de colonnes : {len(r_data_integration.columns)}")
# print(r_data_integration.columns)

-----------------------------------------------------------------------------------------------------------------------

## SEMI UNIVERSEL MAIS BASER sur la TABLE FUSION  ici orders -1- WITH COMMENTS   CODE 1
print(data_clean_final['order_item'].head())
print(r_data_intagration.isnull().sum().sort_values(ascending=False)) # Last verification to see if null values has been created after the fusion

def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    """
    Consolide les tables SQL nettoyées en un DataFrame unique pour le Feature Engineering.
    
    Args:
        data_clean_from_sql (dict): Dictionnaire contenant les DataFrames par nom de table.
        
    Returns:
        pd.DataFrame: Une table de faits enrichie de toutes ses dimensions.
    """
    print(f"--- LANCEMENT DE L'INTÉGRATION RELATIONNELLE ---")
    
    # 1. Analyse des relations : Récupération du plan de marquage (PK/FK)
    keys = f_indentify_p_f_key(data_clean_from_sql) 
    
    # 2. Initialisation : On définit 'orders' comme table pivot (Fact Table)
    # On utilise .copy() pour ne pas modifier les données sources par erreur
    main_df = data_clean_from_sql["orders"].copy()  
    tables_fusionnees = ["orders"] # On initialise avec la table mère déjà traitée

    # 3. Boucle d'enrichissement dynamique
    for key_full_name, tipo in keys.items():
        # Extraction du nom de la table et de la colonne de liaison (le pont)
        table_name, col_name = key_full_name.split('.')
        
        # SÉCURITÉ : On ne fusionne que les nouvelles tables ayant un lien direct avec main_df
        if table_name not in tables_fusionnees:
            if col_name in main_df.columns:
                print(f"✅ Maillage validé : [orders] + [{table_name}] via '{col_name}'")
                
                df_to_add = data_clean_from_sql[table_name]
                
                # LOGIQUE ANTI-DOUBLONS :
                # On filtre les colonnes pour ne pas importer des infos déjà présentes (ex: city, state)
                # Cela évite la création de colonnes polluantes comme 'customer_city_x' ou '_y'
                cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                
                # Fusion à gauche (Left Join) pour conserver l'intégralité des commandes
                main_df = pd.merge(
                    main_df, 
                    df_to_add[cols_to_keep], 
                    on=col_name, 
                    how='left'
                )
                
                # On enregistre la table pour éviter de la traiter plusieurs fois (optimisation)
                tables_fusionnees.append(table_name)
            
    return main_df

# --- MISE EN SERVICE ---
# r_data_integration devient notre dataset "Master" prêt pour l'analyse
r_data_integration = data_integration(data_clean_final)

print(f"\n🚀 INTÉGRATION TERMINÉE : {len(r_data_integration.columns)} colonnes consolidées.")

# Audit post-fusion : Vérification de la présence de valeurs nulles induites par les jointures
print(r_data_integration.isnull().sum().sort_values(ascending=False))












## SEMI UNIVERSEL MAIS BASER sur la TABLE FUSION  ici orders -2-     CODE 1


def data_integration(data_clean_from_sql: dict) -> pd.DataFrame:
    print(f"--- FUSION UNIVERSELLE TOTALE (CIBLE 39 COLONNES) ---")
    keys = f_indentify_p_f_key(data_clean_from_sql)
    
    # On force 'orders' comme point de départ pour ce dataset, 
    # ou on utilise la détection FK pour le rendre universel.
    main_table_name = "orders" 
    main_df = data_clean_from_sql[main_table_name].copy()
    
    tables_fusionnees = [main_table_name]

    # On fait 2 passages pour être sûr de rattraper les tables liées indirectement
    for passage in range(2):
        print(f"Passage n°{passage + 1}...")
        for key_full_name, tipo in keys.items():
            table_name, col_name = key_full_name.split('.')
            
            if table_name not in tables_fusionnees:
                if col_name in main_df.columns:
                    print(f"✅ Fusion : {table_name} via '{col_name}'")
                    
                    df_to_add = data_clean_from_sql[table_name]
                    cols_to_keep = [col for col in df_to_add.columns if col not in main_df.columns or col == col_name]
                    
                    main_df = pd.merge(main_df, df_to_add[cols_to_keep], on=col_name, how='left')
                    tables_fusionnees.append(table_name)
            
    return main_df




r_data_integration = data_integration(data_clean_final)
print(f"\nSUCCESS ! Nombre de colonnes : {len(r_data_integration.columns)}")
# print(r_data_integration.columns)

print(data_clean_final['order_item'].head())
print(r_data_intagration.isnull().sum().sort_values(ascending=False)) # Last verification to see if null values has been created after the fusion




