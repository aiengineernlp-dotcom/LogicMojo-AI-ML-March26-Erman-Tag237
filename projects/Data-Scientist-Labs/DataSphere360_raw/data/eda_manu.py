
import plotly.express as px

"""
2-3 catégories + proportion       → pie chart
Beaucoup de catégories            → bar
Tendance dans le temps            → line
Distribution d'une variable       → histogram
Relation entre deux variables     → scatter
Corrélation globale               → heatmap
"""
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
    on combine deux features pour avoir plus de lisibiliter dans le rapport.
    """

    psm = df.groupby("year_month")["payment_value"].sum().sort_index()
    fig = px.line( # vue que c'est une representation temporelle, on utilise px.line()
        x=psm.index,
        y=psm.values,
        title="Peak Sales",
        markers=True,
    )
    return fig




def f_eda_metier_top_categories(df):
    # groupby product_category_name
    # compter les commandes uniques
    # garder le top 10
    # barplot
    # retourner figure
    top_categories = df.groupby("product_category_name")['order_id'].nunique().sort_values(ascending=False).head(10)

    fig = px.bar(
        x=top_categories.index,
        y=top_categories.values,
        title="Top Categories",
    )

    return fig


def f_eda_metier_revenue_by_category(df):
    # groupby product_category_name
    # sum(payment_value)
    # top 10
    # barplot
    # retourner figure

    revenue_by_category = df.groupby("product_category_name")["payment_value"].sum().sort_values(ascending=False).head(10)

    fig = px.bar( x=revenue_by_category.index,y=revenue_by_category.values,title="Revenue by Category")

    return fig

def f_eda_metier_product_demand(df):
    # compter combien de fois chaque produit est commandé
    product_demand = df["product_id"].value_counts()
    # créer un histogram
    fig = px.histogram(
        x=product_demand.values,
        title="Product Demand Distribution",
        labels={"x": "Nombre de commandes par produit"}
    )
    # retourner figure
    return fig


def f_eda_metier_top_sellers(df):
    # groupby seller_id
    # compter les commandes uniques
    # top 10
    # barplot
    # retourner figure

    top_sellers = df.groupby("seller_id")["order_id"].nunique().sort_values(ascending=False).head(10)

    fig =px.bar(
        x=top_sellers.index,
        y=top_sellers.values,
        title="Top sellers",
    )

    return fig


def f_eda_metier_seller_revenue(df):
    # groupby seller_id
    # sum(payment_value)
    # top 10
    # barplot
    # retourner figure
    seller_revenue = df.groupby("seller_id")["payment_value"].sum().sort_values(ascending=False).head(10)
    '''
    groupby sur ("seller_id") parce que c'est dans seller_id que on va voir le montant vendu
    sum() sur ["payment_value"] pour sommer le montant du seller
    '''

    fig = px.bar( x=seller_revenue.index,y=seller_revenue.values,title="Seller Revenue") # bar parceque on a plusieurs payment_value mais on a juste choisi d'afficher 10
    return fig


def f_eda_metier_seller_distribution(df):
    # compter le nombre de vendeurs par état
    # barplot
    # retourner figure
    seller_distribution = df.groupby("seller_state")["seller_id"].nunique().sort_values(ascending=False).head(10)

    fig = px.bar( x=seller_distribution.index,y=seller_distribution.values,title="Seller Distribution")
    return fig

def f_eda_metier_review_distribution(df):
    # histogram de review_score
    # retourner figure
    review_distribution = df["review_score"]
    fig = px.histogram(
        x=review_distribution,
        title="Review Score Distribution"
    )

    return fig


def f_eda_metier_delivery_vs_rating(df):
    # scatter plot
    # x = delta_order_estimated_delivery_date_minus_order_purchase_timestamp_days
    # y = review_score
    # retourner figure

    # ✅ on accède à la colonne via df
    x = df["delta_order_estimated_delivery_date_minus_order_purchase_timestamp_days"]
    y = df["review_score"]
    fig = px.scatter(
        df,
        x=x,
        y=y,
        title="Delivery Time vs Review Score",
    )
    return fig


def f_eda_metier_dissatisfaction_patterns(df):
    # filtrer review_score <= 2
    # groupby product_category_name
    # compter les commandes
    # top 10
    # barplot
    # retourner figure
    insatisfaits = df[df["review_score"] <= 2]
    order = insatisfaits.groupby("product_category_name")["order_id"].nunique().sort_values(ascending=False).head(10)

    fig = px.bar(
        x=order.index,
        y=order.values,
        title="Dissatisfaction Patterns - Top 10 Categories"
    )
    return fig


def f_generate_eda_metier_report(df, output_path="eda_metier_report.html"):

    # ======= Customer Analysis =======
    fig1 = f_eda_metier_new_vs_repeat(df)           # New vs Repeat Customers
    fig2 = f_eda_metier_high_vs_low_value(df)        # High vs Low Value Customers
    fig3 = f_eda_metier_geographic_distribution(df)  # Geographic Distribution

    # ======= Revenue and Order Analysis =======
    fig4 = f_eda_metier_monthly_revenue(df)          # Monthly Revenue Trends
    fig5 = f_eda_metier_order_volume(df)             # Order Volume Trends
    fig6 = f_eda_metier_peak_sales(df)               # Peak Sales Periods

    # ======= Product Analysis =======
    fig7 = f_eda_metier_top_categories(df)           # Top Selling Categories
    fig8 = f_eda_metier_revenue_by_category(df)      # Revenue by Category
    fig9 = f_eda_metier_product_demand(df)           # Product Demand Distribution

    # ======= Seller Analysis =======
    fig10 = f_eda_metier_top_sellers(df)             # Top Sellers
    fig11 = f_eda_metier_seller_revenue(df)          # Seller Revenue
    fig12 = f_eda_metier_seller_distribution(df)     # Seller Distribution

    # ======= Review and Satisfaction Analysis =======
    fig13 = f_eda_metier_review_distribution(df)         # Review Score Distribution
    fig14 = f_eda_metier_delivery_vs_rating(df)          # Delivery Time vs Rating
    fig15 = f_eda_metier_dissatisfaction_patterns(df)    # Dissatisfaction Patterns

    # ======= Assembler en HTML =======
    html = "<html><body>"
    html += "<h1>EDA Métier Report</h1>"

    # Customer Analysis
    html += "<h2>Customer Analysis</h2>"
    html += fig1.to_html(full_html=False, include_plotlyjs='cdn')  # charge plotly une seule fois
    html += fig2.to_html(full_html=False, include_plotlyjs=False)  # réutilise plotly déjà chargé
    html += fig3.to_html(full_html=False, include_plotlyjs=False)

    # Revenue and Order Analysis
    html += "<h2>Revenue and Order Analysis</h2>"
    html += fig4.to_html(full_html=False, include_plotlyjs=False)
    html += fig5.to_html(full_html=False, include_plotlyjs=False)
    html += fig6.to_html(full_html=False, include_plotlyjs=False)

    # Product Analysis
    html += "<h2>Product Analysis</h2>"
    html += fig7.to_html(full_html=False, include_plotlyjs=False)
    html += fig8.to_html(full_html=False, include_plotlyjs=False)
    html += fig9.to_html(full_html=False, include_plotlyjs=False)

    # Seller Analysis
    html += "<h2>Seller Analysis</h2>"
    html += fig10.to_html(full_html=False, include_plotlyjs=False)
    html += fig11.to_html(full_html=False, include_plotlyjs=False)
    html += fig12.to_html(full_html=False, include_plotlyjs=False)

    # Review and Satisfaction Analysis
    html += "<h2>Review and Satisfaction Analysis</h2>"
    html += fig13.to_html(full_html=False, include_plotlyjs=False)
    html += fig14.to_html(full_html=False, include_plotlyjs=False)
    html += fig15.to_html(full_html=False, include_plotlyjs=False)

    html += "</body></html>"

    # ======= Écrire le fichier HTML =======
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Rapport EDA Métier généré : {output_path}")

'''
2-3 catégories + proportion  → pie chart
Beaucoup de catégories       → bar
Tendance dans le temps       → line
Distribution d'une variable  → histogram
Outliers                     → boxplot
Corrélation entre variables  → scatter ou heatmap
scatter plot                 → montre la relation entre deux variables numériques
                                axe x → délai de livraison
                                axe y → review_score
                                chaque point → une commande
'''
if __name__ == "__main__":
    # r_c_f_eda_metier_high_vs_low_value = f_eda_metier_high_vs_low_value (f_feature_engineering)
    # print(r_c_f_eda_metier_high_vs_low_value)
    pass



