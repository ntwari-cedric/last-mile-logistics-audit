import pandas as pd

# load data
orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")

# merge
df = orders.merge(customers, on="customer_id")
df = df.merge(reviews, on="order_id")

# dates
df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])

# clean
df = df.dropna(subset=[
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "review_score"
])

# delay
df["delay_days"] = (
    df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
).dt.days

# status
df["delivery_status"] = df["delay_days"].apply(
    lambda x: "On Time" if x <= 0 else ("Late" if x <= 5 else "Super Late")
)

# quick insights
print(df.groupby("customer_state")["delivery_status"].apply(lambda x: (x=="Late").mean()*100).head())
print(df.groupby("delivery_status")["review_score"].mean())

# save
df.to_csv("cleaned_master_data.csv", index=False)

# CANDIDATE'S CHOICE FEATURE

avg_delay = df.groupby("customer_state")["delay_days"].mean()

avg_delay.sort_values(ascending=False).head(10).plot(
    kind="bar",
    color="red"
)

plt.title("Top 10 States with Highest Average Delay")
plt.xlabel("State")
plt.ylabel("Average Delay (Days)")
plt.tight_layout()
plt.show()