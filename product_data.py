echo "# arussell_project1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Amazing100502/arussell_project1.git
git push -u origin main
print(git)

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
