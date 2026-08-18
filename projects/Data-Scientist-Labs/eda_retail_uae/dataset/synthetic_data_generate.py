# ════════════════════════════════════════════════════
# STEP 1 — GENERATE DATASET
# ════════════════════════════════════════════════════
from config.imports import *

def generate_retail_dataset(
        n: int = 5000,
        seed: int = 42
) -> pd.DataFrame:
    """
    Generate realistic UAE retail dataset.
    Simulates 5000 orders over 12 months.
    """
    np.random.seed(seed)

    # Dates — 12 mois de données
    start_date = datetime(2025, 1, 1)
    dates = [
        start_date + timedelta(
            days=np.random.randint(0, 365)
        )
        for _ in range(n)
    ]
    dates.sort()

    # Catégories avec prix réalistes UAE
    categories = {
        "Electronics": (200, 3000),
        "Fashion": (50, 500),
        "Home & Garden": (30, 800),
        "Sports": (40, 600),
        "Beauty": (20, 300),
        "Food & Grocery": (10, 200),
        "Books": (15, 100),
        "Toys": (25, 400),
    }

    products = {
        "Electronics": ["iPhone 15", "MacBook Pro",
                        "Samsung TV", "AirPods",
                        "iPad", "Sony Camera"],
        "Fashion": ["Nike Shoes", "Zara Dress",
                    "H&M Jacket", "Adidas Track",
                    "Levi's Jeans"],
        "Home & Garden": ["IKEA Chair", "Philips Lamp",
                          "Garden Set", "Coffee Maker"],
        "Sports": ["Tennis Racket", "Yoga Mat",
                   "Running Shoes", "Dumbbells"],
        "Beauty": ["MAC Foundation", "L'Oreal Set",
                   "Perfume", "Skincare Kit"],
        "Food & Grocery": ["Organic Pack", "Date Box",
                           "Spice Set", "Coffee Beans"],
        "Books": ["Python ML", "Data Science",
                  "Business Strategy", "Novel"],
        "Toys": ["LEGO Set", "RC Car",
                 "Board Game", "Puzzle"],
    }

    cities = {
        "Dubai": 0.45,
        "Abu Dhabi": 0.25,
        "Sharjah": 0.15,
        "Ajman": 0.08,
        "RAK": 0.07,
    }

    payments = {
        "Credit Card": 0.40,
        "Debit Card": 0.25,
        "Cash": 0.15,
        "Apple Pay": 0.12,
        "Bank Transfer": 0.08,
    }

    # Générer les données
    cat_choices = np.random.choice(
        list(categories.keys()),
        n,
        p=[0.25, 0.20, 0.12, 0.10, 0.10,
           0.10, 0.07, 0.06]
    )

    records = []
    for i, (date, cat) in enumerate(
            zip(dates, cat_choices)
    ):
        min_p, max_p = categories[cat]
        unit_price = round(
            np.random.uniform(min_p, max_p), 2
        )
        quantity = int(
            np.random.choice([1, 2, 3, 4, 5],
                             p=[0.6, 0.2, 0.1,
                                0.07, 0.03])
        )
        total = round(unit_price * quantity, 2)

        # Rating — lié au prix et à la catégorie
        base_rating = 4.0 if cat in [
            "Electronics", "Beauty"
        ] else 3.7
        rating = round(
            np.clip(
                np.random.normal(base_rating, 0.5),
                1, 5
            ), 1
        )

        # Retour — plus probable si rating < 3
        return_prob = 0.20 if rating < 3 else \
            0.08 if rating < 4 else 0.03
        returned = int(np.random.random() < return_prob)

        city = np.random.choice(
            list(cities.keys()),
            p=list(cities.values())
        )
        payment = np.random.choice(
            list(payments.keys()),
            p=list(payments.values())
        )
        product = np.random.choice(products[cat])

        records.append({
            "order_id": f"ORD{i + 1:05d}",
            "date": date,
            "month": date.strftime("%B"),
            "month_num": date.month,
            "quarter": f"Q{(date.month - 1) // 3 + 1}",
            "weekday": date.strftime("%A"),
            "category": cat,
            "product": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_aed": total,
            "city": city,
            "payment_method": payment,
            "rating": rating,
            "returned": returned,
        })

    df = pd.DataFrame(records)

    # Ajouter quelques valeurs manquantes réalistes
    missing_idx = np.random.choice(
        df.index, size=int(n * 0.02), replace=False
    )
    df.loc[missing_idx[:len(missing_idx) // 2],
    "rating"] = np.nan
    df.loc[missing_idx[len(missing_idx) // 2:],
    "payment_method"] = np.nan

    return df


my_df_init = generate_retail_dataset(50000, 42)
# df = r_c_generate_retail_dataset

print(list(my_df_init.columns))  # test
