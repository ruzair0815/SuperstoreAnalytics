import pandas as pd

data_path = '/Users/rehmauzair/SuperstoreAnalytics/data/SampleSuperstore.csv'
data = pd.read_csv(data_path)

# KPIs
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100
avg_sales_per_item = (data['Sales'] / data['Quantity']).mean()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Profit Margin (%):", profit_margin)
print("Average Sales per Item:", avg_sales_per_item)
