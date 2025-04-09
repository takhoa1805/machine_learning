import pandas as pd

depression_path = "../datasets/depression.csv"
depression_data = pd.read_csv(depression_path)

depression_data.describe() 