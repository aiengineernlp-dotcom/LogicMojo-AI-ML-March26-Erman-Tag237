from config.settings import *
from data.feature_eng_manu import df


def f_eda_section1(df: pd.DataFrame) -> dict:
    # shape
    # dtypes
    # head(5)
    return {
        "shape": df.shape,
        "dtypes": df.dtypes,
        "head": df.head(5),
    }


def f_eda_section2(df: pd.DataFrame) -> dict:
    missing_count = df.isnull().sum()[df.isnull().sum() > 0]
    missing_percent = (df.isnull().sum() / len(df) * 100)[df.isnull().sum() > 0]
    return {
        "missing_count": missing_count,
        "missing_percent": missing_percent.round(2),
    }


def f_eda_section3(df: pd.DataFrame) -> dict:
    # statistiques numériques
    # statistiques catégorielles
    return {
        "numeric_stats": df.select_dtypes(include='number').describe().round(2),
        "categorical_stats": df.select_dtypes(include='object').describe(),
    }


import plotly.express as px

def f_eda_section4(df: pd.DataFrame) -> list:
    # récupérer les colonnes numériques
    # pour chaque colonne → créer un histogramme
    # retourner la liste des graphiques
    figures = []
    for col in df.select_dtypes(include='number').columns:
        fig = px.histogram(df, x=col, title=f"Distribution de {col}")
        figures.append(fig)
    return figures



def f_eda_section5(df: pd.DataFrame) -> list:
    # récupérer les colonnes numériques
    # pour chaque colonne → créer un boxplot
    # retourner la liste des graphiques
    figures = []
    for col in df.select_dtypes(include='number').columns:
        fig = px.box(df, y=col, title=f"Outliers - {col}")
        figures.append(fig)
    return figures



def f_eda_section6(df: pd.DataFrame) -> list:
    # matrice de corrélation
    # heatmap plotly
    # retourner le graphique
    figures = []
    corr = df.select_dtypes(include='number').corr()
    fig = px.imshow(corr, title="Matrice de corrélation")
    figures.append(fig)

    return figures

def f_eda_section7(df: pd.DataFrame) -> dict:
    # récupérer les colonnes catégorielles
    # pour chaque colonne → value_counts()
    # pour chaque colonne → barplot plotly
    value_counts = {}
    figures = []

    for col in df.select_dtypes(include='object').columns:
        value_counts_col = df[col].value_counts()
        value_counts[col] = value_counts_col
        fig = px.bar(x=value_counts_col.index, y=value_counts_col.values, title=f"Distribution - {col}")
        figures.append(fig)

    return {
        "value_counts": value_counts,
        "figures": figures
    }
