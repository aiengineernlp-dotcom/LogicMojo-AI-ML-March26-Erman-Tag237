# ════════════════════════════════════════════════════
# STEP 3 — CLEAN
# ════════════════════════════════════════════════════
from data.loader import r_c_fech_data_from_psql
from config.settings import *




# print(f"\n🧹 CLEANING")
# my_df_init_clean = my_df_init.copy()

# # Rating -> madiane par categorie
# my_df_init_clean["rating"] = my_df_init_clean.groupby("category")["rating"].transform(lambda x : x.fillna(x.median()))

# #Payement -> mode global
# my_df_init_clean ["payment_method"] = (my_df_init_clean["payment_method"]).fillna(my_df_init_clean["payment_method"].mode()[0])

# print(f"\nMissing Before: {my_df_init.isnull().sum().sum()}")
# print(f"\n✅ Missing After: {my_df_init_clean.isnull().sum().sum()}")


# methode by fucntion

def cleaning(raw_data_from_:dict):
    print(f"\n🧹 CLEANING")

    colonnes_numeriques = []
    colonnes_texte = []
    cleaned_data={}
    for table_name, df in raw_data_from_.items():
        if df.empty:
            print("ok")
            raise ValueError("Erman The data is not avaible")
        else:
            print("ok_1")
            try:
                raw_data_from_clean = df.copy()
                for col in raw_data_from_clean.columns:
                    print("ok_4")
                    # colonnes numériques
                    if raw_data_from_clean[col].dtype in ["int64", "float64"] or pd.api.types.is_numeric_dtype(
                            raw_data_from_clean[col]):  ## C"EST CA QUE JE VAIS FUSIONNER L"INGINE FINALE
                        raw_data_from_clean[col] = raw_data_from_clean[col].fillna(raw_data_from_clean[col].median())
                        colonnes_numeriques.append(col)
                        print(colonnes_numeriques)

                    # colonnes texte
                    if raw_data_from_clean[col].dtype == "object" or pd.api.types.is_object_dtype(
                            raw_data_from_clean[col]) or pd.api.types.is_categorical_dtype(
                            raw_data_from_clean[col]):  ## C"EST CA QUE JE VAIS FUSIONNER L"INGINE FINALE
                        raw_data_from_clean[col] = raw_data_from_clean[col].fillna(raw_data_from_clean[col].mode()[0])
                        colonnes_texte.append(col)
                        print(colonnes_texte)
                    # more than 30% missing values  a coder
                    # if raw_data_from_clean[col].isnull():
                cleaned_data[table_name] = raw_data_from_clean
            except Exception as e:
                print(f"Erman The error is {e}")

        return cleaned_data


r_c_cleaning = cleaning(r_c_fech_data_from_psql)
missing_before = sum(df.isnull().sum().sum() for df in r_c_fech_data_from_psql.values()) # cette ecriture car r_c_fech_data_from_psql est un dictionnaire
missing_after = sum(df.isnull().sum().sum() for df in r_c_cleaning.values()) # cette ecriture car r_c_cleaning est un dictionnaire

print(f"\nMissing Before: {missing_before}")
print(f"\n✅Missing Before: {missing_after}")
# print(f"\n✅ Missing After: {r_c_cleaning.isnull().sum().sum()}") # cas si r_c_cleaning est un dataFrame

"""
README:
note que selon que ce soit un dataframe ou un dictionnaire la difference est tres minime. mais fait attention au faux positifs silencieux
"""


def handle_missing_values(raw_data_from_:dict)->dict:
    all_is_missing={}
    treshold = 0.3
    missing_values_great_30={}

    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Donnees introuvables")
        else:
            try:
                df_clone = df.copy()
                for col_name in df_clone.columns:
                    col_value = df[col_name]
                    # -1- Missing Values
                    is_missing = col_value.isnull().sum()
                    if is_missing > 0:
                        all_is_missing[table_name] = is_missing
                    # -2- more than 30% missing values
                    more_than_30 = is_missing > (treshold * len(df_clone))
                    if more_than_30:
                        missing_values_great_30[col_name] = is_missing
                    else:
                        if is_missing > 0:
                            # -3- base on type of variable, I will transform missing values to :
                            # - 3.1 - Median for numerical  variables,
                            if pd.api.types.is_numeric_dtype(col_value):
                                # compute the median
                                median_col_value = col_value.median()
                                # Replace by the median
                                df_clone[col_name] = col_value.fillna(median_col_value)
                                print(f"Numerical:{col_name} - Median is : {median_col_value}")

                            #- 3.2 Mode for categorial variables
                            elif pd.api.types.is_object_dtype(col_value) or pd.api.types.is_categorical_dtype(col_value):
                                # compute the mode
                                mode_col_value = col_value.mode()[0] #  [0] because .mode() always return a list. and i can not put a list in a dataframe (exel file) so i just take the first value
                                # Replace by the mode (la valeur la plus frequente)
                                df_clone[col_name] = col_value.fillna(mode_col_value)
                                print(f"categorial:{col_name} - mode is: {mode_col_value}\n")
                        else:
                            # print(f"🟢 {col_name} : all is fine")
                            print()
            except Exception as e:
                print("STOP l'erreur est : ->", e)

    return  raw_data_from_

# r_c_handle_missing_values = handle_missing_values(r_c_fech_data_from_psql) # no problem here.
imputation = handle_missing_values(r_c_fech_data_from_psql)
print(imputation)


def remove_duplicated_record(raw_data_from_: dict):
    duplicated_records = {}

    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Donnnees non trouvees")
        else:
            try:
                df_clone = df.copy()
                for col_name in df_clone.columns:  # id , name , sexe , city
                    # 🚩col_value = df[col_name]
                    # 🚩if col_value.duplicated().any(): # BAS: col_value est une Series (une colonne) or on veux une ligne qui correspond a un record.  Donc col_value.duplicated() vérifie si des valeurs de cette colonne sont répétées. C'est pas ce que on veux. On veut savoir et voir les LIGNES (record) Dupliquees
                    pass
                duplicates = df_clone[df_clone.duplicated()]

                if not duplicates.empty:
                    duplicated_records[table_name] = duplicates
            except Exception as e:
                print("The error is ", e)

    return duplicated_records


r_c_remove_duplicated_record = remove_duplicated_record(r_c_fech_data_from_psql)
print(r_c_remove_duplicated_record)



def convert_date_col_to_date_time_format():
    pass


def validate_data_type_and_range():
    pass

def standardize_col_name():
    pass




