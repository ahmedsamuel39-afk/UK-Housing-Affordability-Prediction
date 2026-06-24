# UK-Housing-Affordability-Prediction (1977 - 2035)
📌 Overview

This project analyses housing affordability in the United Kingdom by comparing house prices to income over time. It extends the analysis by building a predictive model to forecast affordability trends for the next decade.

The goal is to assess whether housing has become less affordable historically and to estimate how this trend may evolve in the future.

📊 Data Sources
UK House Price Index (HM Land Registry)
Household Disposable Income (ONS)
Key Variables
HousePrice: Average UK house price per year
NonRetired: Median income of non-retired households
Affordability: Ratio of house price to income
⚙️ Methodology
Data Processing
Cleaned income dataset (handled inconsistent formatting and extracted year values)
Filtered house price data to UK-level observations
Converted monthly house prices into yearly averages
Merged datasets on the year variable


🤖 Predictive Model

A Linear Regression model was used to estimate the relationship between time (Year) and housing affordability.

Model Specification

( x ) = Year
( y ) = Affordability

The model was trained on historical data (1977–2024) and used to forecast affordability from 2025 to 2035.

📈 Results

The historical analysis shows a clear upward trend in the house price-to-income ratio, indicating that housing has become progressively less affordable over time.

The predictive model suggests that, if current trends continue, affordability will continue to deteriorate over the next decade.

🔍 Key Insight

The number of years of income required to purchase a house has increased significantly over time, highlighting a structural affordability issue in the UK housing market.

⚠️ Limitations
The model assumes a linear relationship between time and affordability
It does not account for:
interest rates
policy changes
housing supply dynamics
Time-series effects such as autocorrelation are not explicitly modelled

As a result, predictions should be interpreted as trend-based projections rather than precise forecasts.

🚀 Future Improvements
Incorporate macroeconomic variables (e.g. interest rates, inflation)
Apply time-series models (e.g. ARIMA)
Perform regional affordability analysis
Explore non-linear models
