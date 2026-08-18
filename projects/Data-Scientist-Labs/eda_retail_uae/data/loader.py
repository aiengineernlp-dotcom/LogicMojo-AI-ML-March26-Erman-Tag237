from config.imports import *

# les donnees brutes viennent de analysis, on envoie a psql et on reupere pour une meilleur utilisation automatique
engine_erman_connexion_to__dataspere360 = create_engine('postgresql://postgres:postgres@localhost:5555/datasphere360_customer_ecommerce')



def fetch_data_from_psql ():
    pass