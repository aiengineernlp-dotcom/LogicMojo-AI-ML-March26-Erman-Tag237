# engineer.py
from Version_2.config.settings import *
from itertools import combinations

def f_detect_column_types(df_ingrated: pd.DataFrame, max_categories: int = 30) -> dict:
    """
    Classe les colonnes en : datetime, categorial, numerical, id_like (à ignorer)
    """
    types = {"datetime": [], "categorial": [], "numerical": [], "id_like": []}

    for col in df_ingrated.columns:
        if pd.api.types.is_datetime64_any_dtype(df_ingrated[col]):
            types["datetime"].append(col)
            continue

        if df_ingrated[col].dtype == "object":
            try:
                parsed = pd.to_datetime(df_ingrated[col], errors="coerce")
                if parsed.notna().mean() > 0.9:
                    types["datetime"].append(col)
                    continue
            except Exception:
                pass

        if "id" in col.lower() and df_ingrated[col].nunique() > 0.9 * len(df_ingrated):
            types["id_like"].append(col)
            continue

        # Catégorielle SEULEMENT si c'est réellement du texte (object/category)
        if df_ingrated[col].dtype == "object" or df_ingrated[col].dtype.name == "category":
            types["categorial"].append(col)
            continue

        # Sinon, si numérique -> reste numérique, même à faible cardinalité
        # (ex: payment_installments, review_score, product_photos_qty)
        if pd.api.types.is_numeric_dtype(df_ingrated[col]):
            types["numerical"].append(col)
            continue

    return types


def f_extract_datetime_features(df_ingrated: pd.DataFrame, datetime_cols: list) -> pd.DataFrame:
    df_clone = df_ingrated.copy()
    for col in datetime_cols:
        df_clone[col] = pd.to_datetime(df_clone[col], errors="coerce")
        df_clone[f"{col}_year"] = df_clone[col].dt.year
        df_clone[f"{col}_month"] = df_clone[col].dt.month
        df_clone[f"{col}_weekday"] = df_clone[col].dt.weekday
        df_clone[f"{col}_is_weekend"] = df_clone[col].dt.weekday >= 5
        print(f"🕒 Features temporelles extraites pour '{col}'")
    return df_clone


def f_generate_date_deltas(df_ingrated: pd.DataFrame, datetime_cols: list) -> pd.DataFrame:
    """
    Calcule le delta (en jours) entre chaque paire de colonnes dates.
    Ex : delivery_date - purchase_date = délai de livraison réel
    """
    df_clone = df_ingrated.copy()
    for col_a, col_b in combinations(datetime_cols, 2):
        delta_name = f"delta_{col_b}_minus_{col_a}_days"
        df_clone[delta_name] = (df_clone[col_b] - df_clone[col_a]).dt.total_seconds() / 86400
        print(f"⏱️ Delta calculé : '{delta_name}'")
    return df_clone


def f_encode_categorical(df_ingrated: pd.DataFrame, categorical_cols: list, max_onehot: int = 10) -> pd.DataFrame:
    df_clone = df_ingrated.copy()
    for col in categorical_cols:
        n_unique = df_clone[col].nunique()
        if n_unique <= max_onehot:
            dummies = pd.get_dummies(df_clone[col], prefix=col, dummy_na=True)
            df_clone = pd.concat([df_clone.drop(columns=[col]), dummies], axis=1)
            print(f"🔤 One-hot encodé : '{col}' ({n_unique} catégories)")
        else:
            print(f"⚠️ '{col}' a {n_unique} catégories : laissé tel quel (target encoding à faire manuellement)")
    return df_clone


def f_drop_raw_datetime_columns(df_ingrated: pd.DataFrame, datetime_cols: list) -> pd.DataFrame:
    """
    TODO : supprimer les colonnes datetime brutes une fois les features
    (year/month/weekday/deltas) extraites, pour ne pas polluer le modèle final.
    Pour l'instant : ne fait rien (les colonnes restent).
    """
    return df_ingrated


def f_handle_missing_numeric(df_ingrated: pd.DataFrame, numeric_cols: list) -> pd.DataFrame:
    """
    TODO : gérer les NaN dans les colonnes numériques
    (ex: fillna médiane + colonne indicatrice '{col}_was_missing').
    Pour l'instant : ne fait rien (les NaN restent).
    """
    return df_ingrated


def f_isolate_id_columns(df_ingrated: pd.DataFrame, id_cols: list) -> tuple:
    """
    TODO : isoler les colonnes id_like pour faciliter leur exclusion
    au moment de la modélisation (ex: retourner (df, liste_id_cols)
    au lieu de les mélanger avec les vraies features).
    Pour l'instant : ne fait rien, retourne le df tel quel + la liste reçue.
    """
    return df_ingrated, id_cols


def f_filter_relevant_deltas(df_ingrated: pd.DataFrame, delta_cols: list) -> pd.DataFrame:
    """
    TODO : filtrer/valider les deltas de dates qui ont un sens métier
    (éviter les deltas systématiquement négatifs ou non interprétables).
    Pour l'instant : ne fait rien (tous les deltas restent).
    """
    return df_ingrated

def f_feature_engineering(df_ingrated: pd.DataFrame) -> pd.DataFrame:
    print("--- FEATURE ENGINEERING AUTOMATIQUE ---")
    types = f_detect_column_types(df_ingrated)

    df_ingrated = f_extract_datetime_features(df_ingrated, types["datetime"])
    df_ingrated = f_generate_date_deltas(df_ingrated, types["datetime"])
    df_ingrated = f_filter_relevant_deltas(df_ingrated, [])          # stub
    df_ingrated = f_drop_raw_datetime_columns(df_ingrated, types["datetime"])  # stub
    df_ingrated = f_handle_missing_numeric(df_ingrated, types["numerical"])    # stub
    df_ingrated, id_cols = f_isolate_id_columns(df_ingrated, types["id_like"]) # stub
    df_ingrated = f_encode_categorical(df_ingrated, types["categorial"])

    print(f"✅ Colonnes finales : {len(df_ingrated.columns)}")
    return df_ingrated


# claude tkh : # Erreur AttributeError sur keys.items() et ermanwilliant@gmail.com

