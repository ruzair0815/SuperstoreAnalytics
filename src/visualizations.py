import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

data_path = '/Users/rehmauzair/SuperstoreAnalytics/data/SampleSuperstore.csv'
data = pd.read_csv(data_path)

# make sure charts folder exists
charts_folder = Path('/Users/rehmauzair/SuperstoreAnalytics/outputs/charts')
charts_folder.mkdir(parents=True, exist_ok=True)

# Sales by Region
region_summary = data.groupby('Region')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=region_summary.index, y=region_summary.values)
plt.title('Total Sales by Region')
plt.ylabel('Total Sales')
plt.savefig(charts_folder / 'sales_by_region.png')
plt.close()

# Discount vs Profit
discount_profit = data.groupby('Discount')['Profit'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.lineplot(data=discount_profit, x='Discount', y='Profit', marker='o')
plt.title('Average Profit vs Discount')
plt.savefig(charts_folder / 'discount_vs_profit.png')
plt.close()

# Profit Margin by Sub-Category
data['Profit_Margin'] = data['Profit'] / data['Sales']
subcat_margin = data.groupby('Sub-Category')['Profit_Margin'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=subcat_margin.index, y=subcat_margin.values)
plt.xticks(rotation=45)
plt.title('Profit Margin by Sub-Category')
plt.savefig(charts_folder / 'profit_margin_subcat.png')
plt.close()
