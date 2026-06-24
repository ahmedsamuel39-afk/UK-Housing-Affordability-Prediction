import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression
import os 

# =========================
# CONFIG
# =========================
DATA_PATH = "Data"


# =========================
# LOAD DATA
# =========================
def load_data():
    income = pd.read_excel(os.path.join(DATA_PATH, "income.xls"))
    house_prices = pd.read_csv(os.path.join(DATA_PATH, "house_prices.csv"))
    return income, house_prices


# =========================
# CLEAN INCOME DATA
# =========================
def clean_income(income):
    income.columns = ["Year", "NonRetired", "Retired"]
    df = income[["Year", "NonRetired"]].copy()

    df["Year"] = df["Year"].astype(str).str.extract(r'(\d{4})')
    df = df.dropna(subset=["Year", "NonRetired"])

    df["Year"] = df["Year"].astype(int)

    df["NonRetired"] = df["NonRetired"].astype(str).str.strip()
    df["NonRetired"] = pd.to_numeric(df["NonRetired"], errors="coerce")

    df = df.dropna(subset=["NonRetired"])

    return df


# =========================
# CLEAN HOUSE PRICE DATA
# =========================
def clean_house_prices(house_prices):
    df = house_prices[
        house_prices["Region_Name"] == "United Kingdom"
    ]

    df = df[["Date", "Average_Price"]]
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year

    yearly = (
        df.groupby("Year")["Average_Price"]
        .mean()
        .reset_index()
    )

    yearly.columns = ["Year", "HousePrice"]
    return yearly


# =========================
# MERGE + FEATURE ENGINEERING
# =========================
def merge_data(income, house_prices):
    merged = pd.merge(income, house_prices, on="Year", how="inner")
    merged = merged.sort_values("Year")

    merged["Affordability"] = (
        merged["HousePrice"] / merged["NonRetired"]
    )

    return merged


# =========================
# PLOTTING
# =========================
def plot_affordability(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Year"], df["Affordability"])

    plt.xlabel("Year")
    plt.ylabel("House Price / Income")
    plt.title("UK Housing Affordability Over Time")

    plt.grid()
    plt.savefig("affordability.png")  # Save for GitHub
    plt.show()


def plot_comparison(df):
    recent = df[df["Year"] >= 2015]
    past = df[df["Year"] < 2015]

    plt.figure(figsize=(10, 5))

    plt.plot(past["Year"], past["Affordability"], label="Before 2015")
    plt.plot(recent["Year"], recent["Affordability"], label="2015 onwards")

    plt.legend()
    plt.title("Affordability Comparison")

    plt.grid()
    plt.savefig("comparison.png")  
    plt.show()


def predict_affordability(df):
    X = df[["Year"]]
    y = df["Affordability"]

    model = LinearRegression()
    model.fit(X,y)

    future_years = np.arange(2025, 2036).reshape(-1, 1)
    predictions = model.predict(future_years)

    future_df = pd.DataFrame({
        "Year": future_years.flatten(),
        "Predicted_Affordability": predictions
    })

    return future_df

def plot_prediction(actual_df,future_df):
    plt.figure(figsize=(10,5))

    plt.plot(actual_df['Year'],actual_df["Affordability"], label = 'Actual')

    plt.plot(
        future_df['Year'],
        future_df['Predicted_Affordability'],
        linestyle = '--',
        label = "Predicted"

    )

    plt.xlabel('Year')
    plt.ylabel('House Price / Income')
    plt.title("UK Housing Affordability: Actual vs Predicted")

    plt.legend()
    plt.grid()
    plt.savefig("prediction.png")
    plt.show()
    

    
# =========================
# MAIN
# =========================
def main():
    income, house_prices = load_data()

    income_clean = clean_income(income)
    house_clean = clean_house_prices(house_prices)

    merged = merge_data(income_clean, house_clean)

    future_df = predict_affordability(merged)
    plot_prediction(merged, future_df)


if __name__ == "__main__":
    main()




