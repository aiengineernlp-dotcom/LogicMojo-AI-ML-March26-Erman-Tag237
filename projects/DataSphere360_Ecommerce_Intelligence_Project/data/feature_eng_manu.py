#total_order_per_value -> df.groupby("order_id") -> sum(price + freigth_value)
# from data.feature_eng_auto import r_c_f_feature_engineering

df = pass # mon dataframe

#======Total order value (aggregated from order_items or payments) ============
order_feature = df.groupby("order_id").agg(
    total_price = ("price", "sum"),
    total_freight = ("freight_value", "sum"),
)

order_feature["total_order_per_value"] =  order_feature['total_price'] + order_feature['total_freight']
df = df.join(order_feature[["total_order_per_value"]], on="order_id")

print(df.head())


#======Delivery time (order purchase to delivery date) ============
# deja calculer par la fonction automatique

#======Number of items per order ============
nio = df.groupby("order_id")["order_item_id"].count().rename("nomber_of_items_per_order")
df = df.join(nio, on="order_id")

#======Customer purchase frequency  =======================
cpf = df.groupby("customer_unique_id")["order_id"].nunique().rename("Customer_purchase_frequency")

df = df.join(cpf, on="customer_unique_id")

#======Customer lifetime value (basic approximation) ============
clv = df.groupby("customer_unique_id")["payment_value"].sum().rename("Customer_lifetime_value")
df = df.join(clv, on="customer_unique_id")
#======Average order value per customer ============
aoc = df.groupby("customer_unique_id")['payment_value'].mean().rename("Average_order_value_per_customer")
df = df.join(aoc, on="customer_unique_id")






