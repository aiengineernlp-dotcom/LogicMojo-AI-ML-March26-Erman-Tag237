products = ["Laptop", "Phone", "Tablet", "Monitor", "Headphones", "Mouse"]
amazon_prices = [75000, 45000, 30000, 20000, 5000, 440]
flipkart_prices = [72000, 47000, 31000, 19500, 4800, 440]

"""Combines the product names and their prices into a single data structure representing a table."""
# option with zip
# data = [{"produit":p , "amazon_prices": a , "flipkart_prices": f}  for p,a,f in zip (products,amazon_prices,flipkart_prices)]
# print(data)

# option with for loop  But here the condition is that the liste has to be the same len()
table = []
for i in range(len(products)):
    ligne = {
        "product": products[i],
        "amazon_price": amazon_prices[i],
        "flipkart_prices": flipkart_prices[i],
    }
    table.append(ligne)
print(table)

"""Compares the price of each product across both platforms."""
"""AND"""
"""Calculates the difference between the two prices."""

"""Displays the product name, cheaper platform, and price difference."""

print("\n")

for i in range(len(products)):
    price_comp = {
        "product": products[i],
        "amazon_prices": amazon_prices[i],
        "flipkart_prices": flipkart_prices[i]
    }

    if price_comp["amazon_prices"] > price_comp["flipkart_prices"]:  # note that it's
        print(
            f"\n The price of {price_comp["product"]} is MOOST expensive on Amazon: {price_comp["amazon_prices"]} than flipkart {price_comp["flipkart_prices"]} , with a difference of {price_comp["amazon_prices"] - price_comp["flipkart_prices"]}")
    elif price_comp["amazon_prices"] < price_comp["flipkart_prices"]:
        print(
            f"\n The price of {price_comp["product"]} is LESS expensive on Amazon: {price_comp["amazon_prices"]} than flipkart {price_comp["flipkart_prices"]} , with a difference of {price_comp["flipkart_prices"] - price_comp["amazon_prices"]}")
    else:
        print(
            f"The prices on Amazon and Flipkart  are same Amazon: {price_comp["amazon_prices"]}; flipkart: {price_comp["amazon_prices"]}")

    """Determines which platform offers the lower price."""
    print("\n")
if (sum(amazon_prices)) > sum(flipkart_prices):
    print("\n The flipkart platform offers the LOWER prices")
else:
    print("\n The Amazon platform offers the Expensive prices")
