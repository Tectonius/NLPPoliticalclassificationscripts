import pandas as pd

tdf = pd.read_csv('trainingdata.csv', encoding='latin-1', nrows=201)

tdf.to_csv('downsampled_training_data.csv')