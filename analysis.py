import pandas as pd

# Load datasets
orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")

# Merge datasets
df = orders.merge(customers, on="customer_id", how="left")
df = df.merge(reviews, on="order_id", how="left")

# Convert dates
df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])

# Clean missing values
df = df.dropna(subset=[
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "review_score"
])

# Create delay column
df["delay_days"] = (
    df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
).dt.days

# Delivery status
def status(x):
    if x <= 0:
        return "On Time"
    elif x <= 5:
        return "Late"
    else:
        return "Super Late"

df["delivery_status"] = df["delay_days"].apply(status)

# Save final dataset
df.to_csv("cleaned_master_data.csv", index=False)

# Quick check
print(df.shape)
print(df.columns)