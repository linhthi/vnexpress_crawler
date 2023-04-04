import pandas as pd

file_path = './dataset_vnexpress_csv/khoa-hoc.csv'

data = pd.read_csv(file_path)

print(data.head)