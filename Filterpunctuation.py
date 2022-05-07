import pandas as pd

trainingdata = pd.read_csv('downsampled_training_data.csv')
validationdata = pd.read_csv('validationdata.csv')

trainingdata.replace(r'[\W]', ' ', regex=True, inplace=True)
validationdata.replace(r'[\W]', ' ', regex=True, inplace=True)

trainingdata.to_csv('filtered_downsampled_training_data.csv')
validationdata.to_csv('filtered_validation_data.csv')

