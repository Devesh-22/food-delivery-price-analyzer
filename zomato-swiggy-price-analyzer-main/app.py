import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Zomato vs Swiggy Price Analyzer",
    page_icon="🍔",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("🍔 Zomato vs Swiggy Price Analyzer")
st.write("Compare food prices across platforms and find the best deal instantly.")

# -------------------------------
# Load data
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/food_prices.csv")

df = load_data()

# -------------------------------
# Select food item
# -------------------------------
food_items = sorted(df["item"].unique())
selected_item = st.selectbox("🍽 Select a food item", food_items)

filtered_df = df[df["item"] == selected_item]

# -------------------------------
# Show data table
# -------------------------------
st.subheader(f"📋 Prices for {selected_item}")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# -------------------------------
# Minimum price comparison
# -------------------------------
zomato_price = filtered_df[filtered_df["platform"] == "Zomato"]["price"].min()
swiggy_price = filtered_df[filtered_df["platform"] == "Swiggy"]["price"].min()

st.subheader("💰 Best Price Comparison")

col1, col2 = st.columns(2)
with col1:
    st.metric("Zomato", f"₹{zomato_price}")
with col2:
    st.metric("Swiggy", f"₹{swiggy_price}")

price_diff = abs(zomato_price - swiggy_price)

if zomato_price < swiggy_price:
    st.success(f"🏆 Zomato is cheaper by ₹{price_diff}")
elif swiggy_price < zomato_price:
    st.success(f"🏆 Swiggy is cheaper by ₹{price_diff}")
else:
    st.info("🤝 Both platforms have the same price")

# -------------------------------
# BEAUTIFUL PLATFORM COMPARISON CHART
# -------------------------------
st.subheader("📊 Price Comparison Chart")

platforms = ["Zomato", "Swiggy"]
prices = [zomato_price, swiggy_price]
colors = ["#E23744", "#FC8019"]  # Brand colors

fig1, ax1 = plt.subplots(figsize=(6, 4))
bars1 = ax1.bar(platforms, prices, color=colors, width=0.45)

ax1.set_ylabel("Price (₹)", fontsize=11)
ax1.set_title(f"{selected_item} Price Comparison", fontsize=13, pad=10)
ax1.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars1:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        f"₹{int(height)}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

st.pyplot(fig1)

# -------------------------------
# RESTAURANT-WISE COMPARISON
# -------------------------------
st.subheader("🏬 Restaurant-wise Average Price")

restaurant_prices = (
    filtered_df.groupby("restaurant")["price"]
    .mean()
    .sort_values()
)

fig2, ax2 = plt.subplots(figsize=(7, 4))
restaurant_prices.plot(kind="bar", ax=ax2, color="#4C72B0")

ax2.set_ylabel("Average Price (₹)")
ax2.set_title(f"{selected_item} – Restaurant-wise Comparison")
ax2.grid(axis="y", linestyle="--", alpha=0.4)

for i, value in enumerate(restaurant_prices):
    ax2.text(
        i,
        value + 5,
        f"₹{int(value)}",
        ha="center",
        va="bottom",
        fontsize=9
    )

st.pyplot(fig2)

# -------------------------------
# AVERAGE PRICE & INSIGHTS
# -------------------------------
st.subheader("📈 Average Price & Insights")

avg_price = round(filtered_df["price"].mean(), 2)
st.metric("Average Price", f"₹{avg_price}")

if avg_price > min(zomato_price, swiggy_price) + 40:
    st.warning(
        "⚠️ The average price is much higher than the cheapest option. "
        "Choosing the cheapest platform can save money."
    )
else:
    st.info(
        "✅ Prices are fairly consistent across platforms for this item."
    )

st.info("💡 Prices may vary due to platform fees, offers, or surge demand.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built by Sona John | Python • Pandas • Streamlit")
