import pandas as pd

# tdfbody = pd.read_csv('filtered_downsampled_training_data_features.csv', encoding='latin-1', dtype=str)
# vdfbody = pd.read_csv('filtered_validation_data_features.csv', encoding='latin-1',dtype=str)
#
# tdfbody = tdfbody.replace("FALSE", "0")
# tdfbody = tdfbody.replace("TRUE", "1")
# vdfbody = vdfbody.replace("FALSE", "0")
# vdfbody = vdfbody.replace("TRUE", "1")
#
# tdfbody.to_csv('Modified_downsampled_training_data_features.csv')
# vdfbody.to_csv('Modified_validation_data_features.csv')

tdfbody = pd.read_csv('filtered_downsampled_training_data_features_attempt_2.csv', encoding='latin-1', dtype=str)
tdfbody = tdfbody.replace("FALSE", "0")
tdfbody = tdfbody.replace("TRUE", "1")
tdfbody.to_csv('Modified_downsampled_training_data_features_attempt_2.csv')