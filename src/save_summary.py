import pandas as pd
import os

data_path = '/Users/rehmauzair/SuperstoreAnalytics/data/SampleSuperstore.csv'
data = pd.read_csv(data_path)

summary = data.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
}).reset_index()

os.makedirs('/Users/rehmauzair/SuperstoreAnalytics/outputs', exist_ok=True)

summary.to_csv('/Users/rehmauzair/SuperstoreAnalytics/outputs/summary.csv', index=False)
print("Summary saved to outputs/summary.csv")
