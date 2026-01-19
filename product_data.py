echo "# arussell_project1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Amazing100502/arussell_project1.git
git push -u origin main
print(git)

# Mock product catalog
products = [
    {"name": "Laptop", "tags": ["electronics", "portable", "work"]},
    {"name": "Headphones", "tags": ["audio", "music", "electronics"]},
    {"name": "Coffee Maker", "tags": ["kitchen", "appliance", "coffee"]},
    {"name": "Running Shoes", "tags": ["fitness", "outdoors", "clothing"]},
    {"name": "Smartwatch", "tags": ["electronics", "fitness", "wearable"]},
    {"name": "Backpack", "tags": ["travel", "portable", "outdoors"]},
]

# Mock customer preferences (example)
customer_preferences = ["electronics", "fitness", "portable", "music"]

products = [
    {"name": "Laptop", "tags": ["electronics", "portable", "work"]},
    {"name": "Headphones", "tags": ["audio", "music", "electronics"]},
    ...
]
from product_data import products

# Print first few entries
print("Sample product data:")
print(products[:3])
customer_preferences = []

while True:
    pref = input("Enter a product preference (or 'N' to stop): ").strip()
    if pref.upper() == "N":
        break
    customer_preferences.append(pref)
customer_preferences = set(customer_preferences)
print("Customer preferences (unique):", customer_preferences)
products_with_sets = []

for product in products:
    new_product = product.copy()
    new_product["tags"] = set(product["tags"])
    products_with_sets.append(new_product)
def count_matches(product_tags, customer_prefs):
    return len(product_tags.intersection(customer_prefs))
def recommend_products(products, customer_preferences):
    recommendations = []

    for product in products:
        score = count_matches(product["tags"], customer_preferences)
        recommendations.append({
            "name": product["name"],
            "match_score": score
        })

    return recommendations
results = recommend_products(products_with_sets, customer_preferences)

print("\nRecommended Products:")
for item in results:
    print(f"{item['name']} — Match Score: {item['match_score']}")
    git add .
git commit -m "Debugged final output issues"
git push



"""
DESIGN MEMO

This program recommends products to a customer based on how many of their stated preferences match each product’s tags. The core operations used in this project include list iteration, set conversion, and set intersection. Lists are used initially because they preserve order and allow the user to enter preferences freely, including duplicates. Once the preferences are collected, they are converted into a set to remove duplicates and to enable faster membership checks. This is important because sets provide average O(1) lookup time, which becomes increasingly valuable as the dataset grows.

Another key operation is converting each product’s list of tags into a set. This allows the program to use set intersection to compare customer preferences with product attributes. Intersection is an efficient and expressive way to determine how many tags overlap, and it simplifies the logic needed to compute match scores. Loops are used throughout the program to iterate through products, transform data structures, and generate recommendation results.

If this system were scaled to 1,000 or more products, several optimizations might be considered. Storing products in a database or using indexing structures could improve retrieval speed. Sorting recommendations by match score would also become more important for usability. Additionally, caching or precomputing tag sets could reduce repeated work. Overall, the current design is simple, readable, and efficient for small to medium datasets, while still being flexible enough to scale with thoughtful adjustments.
"""
