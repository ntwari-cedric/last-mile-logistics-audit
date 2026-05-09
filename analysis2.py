import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_master_data.csv")

# recreate delay if missing safety check
if "delivery_status" not in df.columns:
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
    df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])

    df["delay_days"] = (
        df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
    ).dt.days

    df["delivery_status"] = df["delay_days"].apply(
        lambda x: "On Time" if x <= 0 else ("Late" if x <= 5 else "Super Late")
    )

# CHART 1
df["delivery_status"].value_counts().plot(kind="bar")
plt.title("Delivery Status Distribution")
plt.show()

# CHART 2
df.groupby("delivery_status")["review_score"].mean().plot(kind="bar")

plt.title("Average Review Score by Delivery Status")
plt.xlabel("Delivery Status")
plt.ylabel("Average Review Score")
plt.show()

# Chart 3

state_late = df.groupby("customer_state")["delivery_status"].apply(
    lambda x: (x == "Late").mean() * 100
)

state_late.sort_values(ascending=False).head(10).plot(kind="bar")

plt.title("Top 10 States with Late Deliveries (%)")
plt.xlabel("State")
plt.ylabel("% Late Orders")
plt.show()

