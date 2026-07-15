from pexpect.pxssh import pxssh

from config.settings import *
from data.feature_eng_auto import f_feature_engineering
def f_eda_metier_new_vs_repeat(df):
    # calculer la fréquence par client
    # classifier nouveau vs repeat
    # compter chaque catégorie
    # créer un graphique plotly (pie chart ou barplot)
    # retourner figure
    customer_frequency = df.groupby("customer_unique_id")["order_id"].nunique() #
    '''
    groupby("customer_unique_id":  parce que on veut s'assurer de prendre un seul unique client
    # nunique() sur order_id : car un même order_id peut apparaitre
    # plusieurs fois (plusieurs items par commande)
    # nunique() compte chaque commande une seule fois     
    '''
    nouveau = (customer_frequency==1).sum() # on additionne les clients dont la frequence est egale a 1
    repeat = (customer_frequency>1).sum() # on additionne les clients dont la frequence est superieur a 1
    fig = px.pie( # car on a deux categories que on veut representer leur proportion et comparer
        names=["Nouveau", "Repeat"], # les noms des deux categories
        values=[nouveau, repeat], # les valeurs des deux categories
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
    customer_ltv = df.groupby("customer_unique_id")["customer_lifetime_value"].first()
    '''
    groupby () sur ("customer_unique_id") parceque on veut etre sur de travailler avec un client unique 
    first()  sur ["customer_lifetime_value"] fonctionne un peu comme nunique() sauf que ici on ne compte pas. on regarde 
    ou les valeurs sont identiques pour un meme client et on garde la premiere valeur
    '''
    median =customer_ltv.median() # c'est le centre de la colonne customer_ltv qui sert de reference pour faire le calcul
    high_value = (customer_ltv >= median).sum() # peut etre considerer comme a droite du centre ou de la mediane donc (+)
    low_value = (customer_ltv < median).sum() # peut etre considerer comme a gauche du centre ou de la mediane donc (-)
    fig =px.pie( # ici on a les deux categorie meme en lisant de la la question on comprend que on va faire un pie. pour reprenter deux categories
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
    '''
    groupby sur ("customer_state") parce que c'est dans customer_state que on cherche ["customer_unique_id"] -> regle generale des 'groupby' je crois je crois
    nunique() sur ["customer_unique_id"]: parce que nunique() compte les clients uniques et identiques sans les additionner car c'est par exemple 3 entrees du meme client dont c'est egale a 1 pas 3
    .sort_values(ascending=False)  veut dire que on part du plus grand nombre au plus petit
    '''

    fig = px.bar( # car on a plusieurs categories. On a pas juste 2 ou 3 states mais plusieurs.
        x=customers_per_state.index,
        y=customers_per_state.values,
        title="Customers per State"
    )
    return fig


def f_eda_metier_monthly_revenue(df):
    metier_monthly_revenue = df.groupby("order_purchase_timestamp_month")["payment_value"].sum()
    '''
    groupby sur ("order_purchase_timestamp_month") parce que c'est dans "order_purchase_timestamp_month" que on cherche "payment_value"
    .sum() sur ["payment_value"] parce que on veut additionner la somme pour chaque mois
    
    '''

    fig = px.line( # ici on parle d'une tandance dans le temps evolution dans le temps on veut voir comment une ligne se deplace dans le temps. On aurait pu utiliser bar "qui gere plusieurs categories" mais le fait que ici on a un indice temporel, on utilise line.
        x=metier_monthly_revenue.index, # months
        y=metier_monthly_revenue.values, # amount
        title="Trends Monthly Revenue",
        markers=True,
    )
    return fig


def f_eda_metier_order_volume(df):
    # groupby order_purchase_timestamp_month
    # compter les commandes uniques par mois
    # créer un lineplot
    # retourner figure
    order_volume = df.groupby("order_purchase_timestamp_month")["order_id"].nunique().sort_index()
    fig = px.line(
        x=order_volume.index,
        y=order_volume.values,
        title="Order Volume",
        markers=True,
    )
    return fig


def f_eda_metier_peak_sales(df):
    # créer year_month
    # groupby year_month
    # sum(payment_value)
    # lineplot



    # combiner année et mois pour avoir # ✅ "2017-01"
    df["year_month"] =df["order_purchase_timestamp_year"].astype(str) + "-" + df["order_purchase_timestamp_month"].astype(str) # ✅ donne "2017-01"
    """
    on combine deux features avant de faire le groupby parceque ....
    """

    psm = df.groupby("year_month")["payment_value"].sum().sort_index()
    fig = px.line(
        x=psm.index,
        y=psm.values,
        title="Peak Sales",
        markers=True,
    )
    return fig




'''
2-3 catégories + proportion  → pie chart
Beaucoup de catégories       → bar
Tendance dans le temps       → line
Distribution d'une variable  → histogram
Outliers                     → boxplot
Corrélation entre variables  → scatter ou heatmap
'''
if __name__ == "__main__":
    # r_c_f_eda_metier_high_vs_low_value = f_eda_metier_high_vs_low_value (f_feature_engineering)
    # print(r_c_f_eda_metier_high_vs_low_value)
    pass



