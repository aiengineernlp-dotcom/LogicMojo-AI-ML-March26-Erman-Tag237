
from config.settings import *
from data.feature_eng_auto import f_feature_engineering
def f_eda_metier_new_vs_repeat(df):
    # calculer la fréquence par client
    # classifier nouveau vs repeat
    # compter chaque catégorie
    # créer un graphique plotly (pie chart ou barplot)
    # retourner figure
    customer_frequency = df.groupby("customer_unique_id")["order_id"].nunique()
    nouveau = (customer_frequency==1).sum()
    repeat = (customer_frequency>1).sum()
    fig = px.pie(
        names=["Nouveau", "Repeat"],
        values=[nouveau, repeat],
        title="Nouveau vs Repeat Customer",
    )
    return fig


def f_eda_metier_high_vs_low_value(df):
    # calculer customer_lifetime_value par client
    # calculer la médiane
    # classifier high vs low
    # compter chaque catégorie
    # créer un graphique plotly
    # retourner figure
    customer_ltv = df.groupby("customer_unique_id")["customer_lifetime_value"].first() # first Car la valeur est identique pour toutes les lignes du même client.
    median =customer_ltv.median()
    high_value = (customer_ltv >= median).sum()
    low_value = (customer_ltv < median).sum()
    fig =px.pie(
        names = ["High Value", "Low Value"],
        values=[high_value, low_value],
        title="High Value vs Low Value Customers",
    )

    return fig



def f_eda_metier_geographic_distribution(df):
    # compter le nombre de clients par état
    # créer un barplot plotly
    # retourner figure
    customers_per_state = df.groupby("customer_state")["customer_unique_id"].nunique().sort_values(ascending=False)

    fig = px.bar(
        x=customers_per_state.index,
        y=customers_per_state.values,
        title="Customers per State"
    )
    return fig




if __name__ == "__main__":
    # r_c_f_eda_metier_high_vs_low_value = f_eda_metier_high_vs_low_value (f_feature_engineering)
    # print(r_c_f_eda_metier_high_vs_low_value)
    pass



