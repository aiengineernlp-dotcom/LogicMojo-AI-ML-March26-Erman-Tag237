from DataSphere360_in_prod.config.settings import *
import plotly.express as px


def f_eda_section1(df_final: pd.DataFrame) -> dict:

    return {
        "shape": df_final.shape,
        "dtypes": df_final.dtypes,
        "head": df_final.head(5),
    }


def f_eda_section2(df_final: pd.DataFrame) -> dict:
    missing_count = df_final.isnull().sum()[df_final.isnull().sum() > 0]
    missing_percent = (df_final.isnull().sum() / len(df_final) * 100)[df_final.isnull().sum() > 0]
    return {
        "missing_count": missing_count,
        "missing_percent": missing_percent.round(2),
    }


def f_eda_section3(df_final: pd.DataFrame) -> dict:

    return {
        "numeric_stats": df_final.select_dtypes(include='number').describe().round(2),
        "categorical_stats": df_final.select_dtypes(include='object').describe(),
    }



def f_eda_section4(df_final: pd.DataFrame) -> list:

    figures = []
    for col in df_final.select_dtypes(include='number').columns:
        fig = px.histogram(df_final, x=col, title=f"Distribution de {col}")
        figures.append(fig)
    return figures



def f_eda_section5(df_final: pd.DataFrame) -> list:

    figures = []
    for col in df_final.select_dtypes(include='number').columns:
        fig = px.box(df_final, y=col, title=f"Outliers - {col}")
        figures.append(fig)
    return figures



def f_eda_section6(df_final: pd.DataFrame) -> list:

    figures = []
    corr = df_final.select_dtypes(include='number').corr()
    fig = px.imshow(corr, title="Matrice de corrélation")
    figures.append(fig)

    return figures

def f_eda_section7(df_final: pd.DataFrame) -> dict:

    value_counts = {}
    figures = []

    for col in df_final.select_dtypes(include='object').columns:
        value_counts_col = df_final[col].value_counts()
        value_counts[col] = value_counts_col
        fig = px.bar(x=value_counts_col.index, y=value_counts_col.values, title=f"Distribution - {col}")
        figures.append(fig)

    return {
        "value_counts": value_counts,
        "figures": figures
    }

def f_generate_eda_report(df_final: pd.DataFrame, output_path: str = "eda_report.html") -> None:


    section1 = f_eda_section1(df_final)
    section2 = f_eda_section2(df_final)
    section3 = f_eda_section3(df_final)
    section4 = f_eda_section4(df_final)
    section5 = f_eda_section5(df_final)
    section6 = f_eda_section6(df_final)
    section7 = f_eda_section7(df_final)

    # construire le HTML
    html = ""

    #section 1
    html += "<h1> Section 1 - Vue générale </h1>"
    html += f"<p>Shape:  {section1['shape']}</p>"
    html += f"<p>Dtypes:  {section1['dtypes'].to_frame().to_html()}</p>"
    html += f"<p>Head:  {section1['head'].to_html()}</p>"

    # Section 2
    html += "<h1>Section 2 - Valeurs manquantes</h1>"
    html += f"{section2['missing_count'].to_frame().to_html()}"

    # Section 3
    html += "<h1>Section 3 - Statistiques descriptives</h1>"
    html += f"{section3['numeric_stats'].to_html()}"
    html += f"{section3['categorical_stats'].to_html()}"

    # Sections 4, 5, 6 → graphiques plotly
    html += f"<h1> Section 4 - Distributions </h1>"
    for fig in section4:
        html += fig.to_html(full_html=False, include_plotlyjs='cdn')

    html += "<h1>Section 5 - Outliers</h1>"
    for fig in section5:
        html += fig.to_html(full_html=False, include_plotlyjs=False)

    html += "<h1>Section 6 - Corrélations</h1>"
    for fig in section6:
        html += fig.to_html(full_html=False, include_plotlyjs=False)

    # Section 7
    html += "<h1>Section 7 - Catégorielles</h1>"
    for fig in section7['figures']:
        html += fig.to_html(full_html=False, include_plotlyjs=False)

    # écrire le fichier
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"<html><body>{html}</body></html>")


    print(f"Rapport EDA généré : {output_path}")
