# Superstore Analytics Project

This project analyzes the SampleSuperstore.csv dataset to calculate KPIs, generate visualizations, and create a summary CSV.

## Folder Structure
- data/ → store SampleSuperstore.csv
- src/ → Python scripts
- outputs/ → charts and summary CSV

## Steps to Run
1. Run `load_data.py` to check your CSV
2. Run `kpi_calculations.py` for KPIs
3. Run `visualizations.py` for charts
4. Run `save_summary.py` to save a summary CSV

## Technologies Used
Python – Core programming language
Pandas – Data cleaning, manipulation, and aggregation
Matplotlib & Seaborn – Data visualization libraries

## Insights Gained from the Data
Regional Performance
- The West and East regions generate the highest sales.
- The South shows weaker profitability despite steady sales.

Category-Level Trends
- Technology products contribute the highest profit margins.
- Furniture tends to have lower profits due to high discounting and shipping costs.

Sub-Category Analysis
- Office Supplies sell in high volume but have thin profit margins.
- Tables in the Furniture category consistently show negative profit, suggesting over-discounting or supply chain inefficiencies.

Customer Segments
- Corporate customers drive higher sales, but Home Office customers are more profitable proportionally.

