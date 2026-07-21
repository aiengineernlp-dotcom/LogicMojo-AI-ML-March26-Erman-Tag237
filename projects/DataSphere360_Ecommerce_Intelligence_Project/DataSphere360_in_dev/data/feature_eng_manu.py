def f_feature_eng_manu(df):

    #======Total order value ============
    order_feature = df.groupby("order_id").agg(
        total_price   = ("price", "sum"),
        total_freight = ("freight_value", "sum"),
    )
    order_feature["total_order_per_value"] = order_feature['total_price'] + order_feature['total_freight']
    df = df.join(order_feature[["total_order_per_value"]], on="order_id")

    #======Delivery time ============
    # deja calculer par la fonction automatique

    #======Number of items per order ============
    nio = df.groupby("order_id")["order_item_id"].count().rename("number_of_items_per_order")
    df = df.join(nio, on="order_id")

    #======Customer purchase frequency ============
    cpf = df.groupby("customer_unique_id")["order_id"].nunique().rename("customer_purchase_frequency")
    df = df.join(cpf, on="customer_unique_id")

    #======Customer lifetime value ============
    clv = df.groupby("customer_unique_id")["payment_value"].sum().rename("customer_lifetime_value")
    df = df.join(clv, on="customer_unique_id")

    #======Average order value per customer ============
    aoc = df.groupby("customer_unique_id")["payment_value"].mean().rename("average_order_value_per_customer")
    df = df.join(aoc, on="customer_unique_id")

    return df