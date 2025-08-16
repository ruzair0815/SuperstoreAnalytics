import pandas as pd

data_path = '/Users/rehmauzair/SuperstoreAnalytics/data/SampleSuperstore.csv'

data = pd.read_csv(data_path)

print(data.head())
