# 🍔 Zomato & Swiggy Price Analyzer

A data-driven web application designed to compare food prices across Zomato and Swiggy platforms. This tool helps users and category managers identify the most cost-effective options using interactive visualizations and real-time data logic.

## 🚀 Features
* **Dynamic Comparison:** Select food items via a dropdown to compare minimum prices.
* **Price Gap Identification:** Automatically identifies the cheaper platform and calculates the exact price difference.
* **Restaurant Insights:** Detailed restaurant-wise price comparisons.
* **Aggregated Analytics:** Average price analysis to understand platform-wide pricing strategies.
* **Visual Dashboards:** Interactive bar charts for quick decision-making.

## 🛠 Tech Stack
* **Language:** Python
* **Data Handling:** Pandas
* **Dashboard Framework:** Streamlit
* **Visualization:** Matplotlib

## 📂 Project Structure
```text
food-delivery-price-analyzer/
│
├── app.py              # Main Streamlit application logic
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── data/
    └── food_prices.csv # SKU-level pricing dataset
