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
    all_data= {}
    colonnes_numeriques = []
    colonnes_texte = []
    for table_name, df in raw_data_from_.items():
        if df.empty:
            print("ok")
            raise ValueError("Erman The data is not avaible")
        else:
            print("ok_1")
            try:
                raw_data_from_clean = df.copy()
                all_data[table_name] = raw_data_from_clean
                print(all_data)

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
            except Exception as e:
                print(f"Erman The error is {e}")

        return all_data


r_c_cleaning = cleaning(r_c_fech_data_from_psql)
missing_before = sum(df.isnull().sum().sum() for df in r_c_fech_data_from_psql.values())
# missing_after = sum(df.isnull().sum().sum() for df in r_c_cleaning())

print(f"\nMissing Before: {missing_before}")
# print(f"\n✅ Missing After: {r_c_cleaning.isnull().sum().sum()}")

"""
README:
j'ai fait une petite gymastie ici: dans cette fonction tout par du fait que j'ai un dictionnaire qui vient du fichier
precedent (loader), et je sais que, je peux avoir le dataframe de ce dictionnaire, appliquer mes operation pandas dessus

"""





def handle_missing_values():
    pass


def remove_duplicated_record():
    pass

def convert_date_col_to_date_time_format():
    pass


def validate_data_type_and_range():
    pass

def standardize_col_name():
    pass




