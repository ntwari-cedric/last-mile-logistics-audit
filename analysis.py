import pandas as pd

orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")

# STEP 1: Merge orders + customers
df = orders.merge(customers, on="customer_id", how="left")

# STEP 2: Merge with reviews
df = df.merge(reviews, on="order_id", how="left")

print(df.head())

print(df.shape)
print(df.columns)

df.to_csv("cleaned_master_data.csv", index=False)