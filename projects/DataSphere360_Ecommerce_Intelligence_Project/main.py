from plotly.graph_objs.layout.slider import Step

from config.settings import *
from data.loader import fech_data_from_psql
#r_c_fech_data_from_psql
from analysis.explorer_eda_1 import data_overview , f_identify_fk_pk, understanding_relation_between_tables
#r_c_data_overview, r_c_f_identify_fk_pk,r_c_understanding_relation_between_tables
from data.cleaner import handle_missing_values,remove_duplicated_record,convert_date_col_to_date_time_format,validate_data_type_and_range,standardize_col_name,cleaning
#r_c_cleaning,r_c_handle_missing_values, r_c_remove_duplicated_record,r_c_convert_date_col_to_date_time_format,r_c_validate_data_type_and_range,r_c_standardize_col_name,r_c_cleaning
from data.data_integration import data_integration
#r_data_integration
from data.feature_eng_auto import f_feature_engineering
#r_c_f_feature_engineering
from data.feature_eng_manu import f_feature_eng_manu

from data.eda_auto import f_generate_eda_report

from data.eda_auto import f_generate_eda_report


#Step  du Push



# ###❌✅
# customers = push_data_to_sql('../dataset/E_commerce_datasets/customers.csv', "customers")
# orders = push_data_to_sql('../dataset/E_commerce_datasets/orders.csv', "orders")
# order_item = push_data_to_sql('../dataset/E_commerce_datasets/order_item.csv',"order_item")
# payments = push_data_to_sql('../dataset/E_commerce_datasets/payments.csv',"payments")
# reviews = push_data_to_sql('../dataset/E_commerce_datasets/reviews.csv',"reviews")
# products = push_data_to_sql('../dataset/E_commerce_datasets/products.csv',"products")
# sellers = push_data_to_sql('../dataset/E_commerce_datasets/sellers.csv',"sellers")
# location = push_data_to_sql('../dataset/E_commerce_datasets/location.csv',"location")
# category_translation = push_data_to_sql('../dataset/E_commerce_datasets/category_translation.csv',"category_translation")
#
# print(customers)
# print(orders)
# print(order_item)
# print(payments)
# print(reviews)
# print(products)
# print(sellers)
# print(location)
# print(category_translation)
#
# df_customers  = pd.read_sql('SELECT * FROM customers LIMIT 10',engine)
# # print(df_customers.info())
#



# Step 1 - Fetch data
raw_data = fech_data_from_psql(engine)
#✅print(raw_data)
#==========
#
# #Step xxx du loader
# # r_c_fech_data_from_psql = fech_data_from_psql(engine)
# # print(r_c_fech_data_from_psql.keys())
#
# # Step 2 - EDA 1
r_c_data_overview = data_overview(raw_data)
#✅print(r_c_data_overview)
# #==========
# # r_c_data_overview = data_overview(r_c_fech_data_from_psql)
# # print((r_c_data_overview))
# #
# # r_c_understanding_relation_between_tables = understanding_relation_between_tables(r_c_fech_data_from_psql)
# # print(r_c_understanding_relation_between_tables)
#
# # Step 3 - Cleaning
clean_data = cleaning(raw_data)
missing_before = sum(df.isnull().sum().sum() for df in raw_data.values()) # cette ecriture car r_c_fech_data_from_psql est un dictionnaire
missing_after = sum(df.isnull().sum().sum() for df in clean_data.values()) # cette ecriture car r_c_cleaning est un dictionnaire
# print(f"\nMissing Before: {missing_before}")
# print(f"\n✅Missing Before: {missing_after}")
# #==========
#
#
#
# # r_c_handle_missing_values = handle_missing_values(r_c_fech_data_from_psql) # no problem here.
# # imputation = handle_missing_values(r_c_fech_data_from_psql)
# # print(imputation)
# # r_c_remove_duplicated_record = remove_duplicated_record(r_c_fech_data_from_psql)
# # print(r_c_remove_duplicated_record)
# #
# # r_c_convert_date_col_to_date_time_format = convert_date_col_to_date_time_format(r_c_fech_data_from_psql)
# # print(r_c_convert_date_col_to_date_time_format)
# #
# # r_c_standardize_col_name = standardize_col_name(r_c_fech_data_from_psql)
# # r_c_validate_data_type_and_range = validate_data_type_and_range(r_c_fech_data_from_psql, expected_schema)
# # print(r_c_validate_data_type_and_range)
#

# #==========
# #print(f"\n✅ Missing After: {r_c_cleaning.isnull().sum().sum()}") # cas si r_c_cleaning est un dataFrame
#
# """
# README:
# note que selon que ce soit un dataframe ou un dictionnaire la difference est tres minime. mais fait attention au faux positifs silencieux
# """
#
#
#
#
#
# # Step 4 - Integration
integrated_data = data_integration(clean_data)
print(integrated_data.isnull().sum().sort_values(ascending=False))
print((integrated_data))
print("Lignes après merge :", len(integrated_data))  # Si ce nombre est > à celui d'avant, le merge a dupliqué des lignes (relation 1-to-many mal gérée)
#==========
#
# Step 5 - Feature Engineering Auto
features_auto = f_feature_engineering(integrated_data)
print(features_auto) # [112650 rows x 81 columns]
# #==========
# Step 6 - Feature Engineering Manuel
df_final = f_feature_eng_manu(features_auto)
print(f" les 86 columns:  {df_final.columns}") # [112650 rows x 86 columns]
# #==========

# Step 6 - EDA Auto
# f_generate_eda_report(df_final, "output/eda_auto_report.html")

# Step 7 - EDA Métier
# f_generate_eda_metier_report(df_final, "output/eda_metier_report.html")
# f_generate_eda_metier_report = f_generate_eda_report(features_auto)
# print(f_generate_eda_metier_report)


# chaque fichier    → contient les fonctions
# main.py           → appelle tout dans l'ordre
# le résultat d'une étape → devient l'input de la suivante