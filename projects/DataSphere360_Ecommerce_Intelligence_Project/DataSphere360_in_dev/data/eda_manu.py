
import plotly.express as px

def f_eda_metier_new_vs_repeat(df):

    customer_frequency = df.groupby("customer_unique_id")["order_id"].nunique() #

    nouveau = (customer_frequency==1).sum()
    repeat = (customer_frequency>1).sum()
    fig = px.pie(
        names=["Nouveau", "Repeat"],
        values=[nouveau, repeat],
        title="Nouveau vs Repeat Customer",
    )
    return fig


def f_eda_metier_high_vs_low_value(df):

    customer_ltv = df.groupby("customer_unique_id")["customer_lifetime_value"].first()

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

    customers_per_state = df.groupby("customer_state")["customer_unique_id"].nunique().sort_values(ascending=False)


    fig = px.bar(
        x=customers_per_state.index,
        y=customers_per_state.values,
        title="Customers per State"
    )
    return fig


def f_eda_metier_monthly_revenue(df):
    metier_monthly_revenue = df.groupby("order_purchase_timestamp_month")["payment_value"].sum()


    fig = px.line(
        x=metier_monthly_revenue.index, # months
        y=metier_monthly_revenue.values, # amount
        title="Trends Monthly Revenue",
        markers=True,
    )
    return fig


def f_eda_metier_order_volume(df):

    order_volume = df.groupby("order_purchase_timestamp_month")["order_id"].nunique().sort_index()
    fig = px.line(
        x=order_volume.index,
        y=order_volume.values,
        title="Order Volume",
        markers=True,
    )
    return fig


def f_eda_metier_peak_sales(df):

    df["year_month"] =df["order_purchase_timestamp_year"].astype(str) + "-" + df["order_purchase_timestamp_month"].astype(str) # ✅ donne "2017-01"


    psm = df.groupby("year_month")["payment_value"].sum().sort_index()
    fig = px.line(
        x=psm.index,
        y=psm.values,
        title="Peak Sales",
        markers=True,
    )
    return fig




def f_eda_metier_top_categories(df):

    top_categories = df.groupby("product_category_name")['order_id'].nunique().sort_values(ascending=False).head(10)

    fig = px.bar(
        x=top_categories.index,
        y=top_categories.values,
        title="Top Categories",
    )

    return fig


def f_eda_metier_revenue_by_category(df):


    revenue_by_category = df.groupby("product_category_name")["payment_value"].sum().sort_values(ascending=False).head(10)

    fig = px.bar( x=revenue_by_category.index,y=revenue_by_category.values,title="Revenue by Category")

    return fig

def f_eda_metier_product_demand(df):
    product_demand = df["product_id"].value_counts()
    # créer un histogram
    fig = px.histogram(
        x=product_demand.values,
        title="Product Demand Distribution",
        labels={"x": "Nombre de commandes par produit"}
    )
    return fig


def f_eda_metier_top_sellers(df):


    top_sellers = df.groupby("seller_id")["order_id"].nunique().sort_values(ascending=False).head(10)

    fig =px.bar(
        x=top_sellers.index,
        y=top_sellers.values,
        title="Top sellers",
    )

    return fig


def f_eda_metier_seller_revenue(df):

    seller_revenue = df.groupby("seller_id")["payment_value"].sum().sort_values(ascending=False).head(10)
    '''
    groupby sur ("seller_id") parce que c'est dans seller_id que on va voir le montant vendu
    sum() sur ["payment_value"] pour sommer le montant du seller
    '''

    fig = px.bar( x=seller_revenue.index,y=seller_revenue.values,title="Seller Revenue") # bar parceque on a plusieurs payment_value mais on a juste choisi d'afficher 10
    return fig


def f_eda_metier_seller_distribution(df):

    seller_distribution = df.groupby("seller_state")["seller_id"].nunique().sort_values(ascending=False).head(10)

    fig = px.bar( x=seller_distribution.index,y=seller_distribution.values,title="Seller Distribution")
    return fig

def f_eda_metier_review_distribution(df):

    review_distribution = df["review_score"]
    fig = px.histogram(
        x=review_distribution,
        title="Review Score Distribution"
    )

    return fig


def f_eda_metier_delivery_vs_rating(df):

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

if __name__ == "__main__":
    # r_c_f_eda_metier_high_vs_low_value = f_eda_metier_high_vs_low_value (f_feature_engineering)
    # print(r_c_f_eda_metier_high_vs_low_value)
    pass



