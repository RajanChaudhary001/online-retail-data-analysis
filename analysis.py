import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_excel("Online Retail.xlsx")

print("Original Dataset Shape:", df.shape)


# ==========================================
# 2. CHECK MISSING VALUES
# ==========================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# ==========================================
# 3. REMOVE DUPLICATE ROWS
# ==========================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)


# ==========================================
# 4. REMOVE ROWS WITH MISSING DESCRIPTION
# ==========================================

df = df.dropna(subset=["Description"])

print("\nShape After Removing Missing Description:", df.shape)


# ==========================================
# 5. CONVERT DATE COLUMN
# ==========================================

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# ==========================================
# 6. REMOVE INVALID QUANTITY
# ==========================================

df = df[df["Quantity"] > 0]

print("\nShape After Removing Invalid Quantity:", df.shape)


# ==========================================
# 7. REMOVE INVALID UNIT PRICE
# ==========================================

df = df[df["UnitPrice"] > 0]

print("Shape After Removing Invalid Prices:", df.shape)


# ==========================================
# 8. CREATE REVENUE COLUMN
# ==========================================

df["Revenue"] = df["Quantity"] * df["UnitPrice"]


# ==========================================
# 9. FINAL DATA CHECK
# ==========================================

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum())


# ==========================================
# 10. SAVE CLEANED DATA
# ==========================================

df.to_csv("cleaned_online_retail.csv", index=False)

print("\nCleaned dataset saved successfully!")








--2

# ==========================================
# 11. BUSINESS KPI ANALYSIS
# ==========================================

print("\n========== BUSINESS KPIs ==========")

# Total Revenue
total_revenue = df["Revenue"].sum()
print("Total Revenue:", round(total_revenue, 2))

# Total Quantity Sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# Total Transactions
total_transactions = df["InvoiceNo"].nunique()
print("Total Transactions:", total_transactions)

# Total Customers
total_customers = df["CustomerID"].nunique()
print("Total Customers:", total_customers)

# Average Order Value
average_order_value = total_revenue / total_transactions
print("Average Order Value:", round(average_order_value, 2))

# Number of Products
total_products = df["StockCode"].nunique()
print("Number of Unique Products:", total_products)

# Number of Countries
total_countries = df["Country"].nunique()
print("Number of Countries:", total_countries)






--3

# ==========================================
# 12. TOP 10 PRODUCTS BY REVENUE
# ==========================================

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_products)






---4


# ==========================================
# 13. TOP 10 COUNTRIES BY REVENUE
# ==========================================

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 COUNTRIES ==========")
print(top_countries)




--5

# ==========================================
# 14. MONTHLY REVENUE
# ==========================================

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_revenue = (
    df.groupby("Month")["Revenue"]
    .sum()
)

print("\n========== MONTHLY REVENUE ==========")
print(monthly_revenue)





--6 
# ============================================================
# 11. DATA VISUALIZATION
# ============================================================

import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 11.1 MONTHLY REVENUE TREND
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 11.2 TOP 10 PRODUCTS BY REVENUE
# ------------------------------------------------------------

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 11.3 TOP 10 COUNTRIES BY REVENUE
# ------------------------------------------------------------

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

top_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Country")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 11.4 QUANTITY SOLD BY TOP 10 COUNTRIES
# ------------------------------------------------------------

top_quantity_countries = (
    df.groupby("Country")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

top_quantity_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Country")

plt.tight_layout()
plt.show()


print("\nAll visualizations created successfully!")







# ==========================================
# 12. FINAL BUSINESS INSIGHTS
# ==========================================

print("\n" + "=" * 50)
print("        FINAL BUSINESS INSIGHTS")
print("=" * 50)


# 1. Total Revenue
total_revenue = df["Revenue"].sum()

print("\n1. TOTAL REVENUE")
print(f"Total Revenue: £{total_revenue:,.2f}")


# 2. Total Quantity Sold
total_quantity = df["Quantity"].sum()

print("\n2. TOTAL QUANTITY SOLD")
print(f"Total Quantity Sold: {total_quantity:,.0f}")


# 3. Total Transactions
total_transactions = df["InvoiceNo"].nunique()

print("\n3. TOTAL TRANSACTIONS")
print(f"Total Transactions: {total_transactions:,}")


# 4. Top Product
top_product = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(1)
)

print("\n4. TOP PRODUCT BY REVENUE")
print(top_product)


# 5. Top Country
top_country = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(1)
)

print("\n5. TOP COUNTRY BY REVENUE")
print(top_country)


# 6. Best Month
monthly_revenue = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["Revenue"]
    .sum()
)

best_month = monthly_revenue.idxmax()
best_month_revenue = monthly_revenue.max()

print("\n6. BEST MONTH")
print(f"Best Month: {best_month}")
print(f"Revenue: £{best_month_revenue:,.2f}")


# 7. Average Order Value
average_order_value = (
    df.groupby("InvoiceNo")["Revenue"]
    .sum()
    .mean()
)

print("\n7. AVERAGE ORDER VALUE")
print(f"Average Order Value: £{average_order_value:,.2f}")


# 8. Number of Products
unique_products = df["Description"].nunique()

print("\n8. UNIQUE PRODUCTS")
print(f"Number of Unique Products: {unique_products:,}")


# 9. Number of Countries
unique_countries = df["Country"].nunique()

print("\n9. COUNTRIES")
print(f"Number of Countries: {unique_countries}")


# 10. Final Summary
print("\n" + "=" * 50)
print("              FINAL SUMMARY")
print("=" * 50)

print(f"""
The dataset contains {len(df):,} cleaned records.

Total revenue generated was £{total_revenue:,.2f}.

A total of {total_quantity:,.0f} items were sold
across {total_transactions:,} transactions.

The business operates across {unique_countries} countries
and has {unique_products:,} unique products.

The highest revenue was generated in {best_month},
with revenue of £{best_month_revenue:,.2f}.

The analysis helps identify:
- Best-performing products
- Best-performing countries
- Monthly revenue trends
- Sales volume
- Customer transactions
- Overall business performance
""")

print("=" * 50)
print("        ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)






customer_revenue = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False)

print("===== TOP 10 CUSTOMERS BY REVENUE =====")
print(customer_revenue.head(10))





