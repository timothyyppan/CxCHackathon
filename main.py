import pandas as pd
import math
import joblib
import ImpactScore as imsc
import ColumnDatesToEpochs as cde
import FilterFireCause as ffc
import ModelTrainer as mt
import ModelUse as mu
import DataCleaner as dc

#Store file path of the dataset
excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

#Opens the dataset as a pandas dataframe
df = pd.read_excel(excel_file, engine='openpyxl')

#Removes rows where dates that have a typo
df.drop(index=1291, inplace=True)
df.drop(index=14316, inplace=True)

#Converts size_class from letters to numbers
size_class_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
df['size_class_num'] = df['size_class'].map(size_class_mapping)

#Calculates the magnitude of the current_size column
magnitude_all_current_sizes= math.sqrt((df['current_size']**2).sum())

#Creates a column and fills it with the normalized current_size
df['normalized_current_size'] = df['current_size'] / magnitude_all_current_sizes

#Converts all date/time to epoch
cde.column_dates_to_epochs(df)

#Creates a column and fills it with the calculated impact score
df['impact_score'] = df.apply(imsc.get_impact_score, axis=1)

#Removes any rows that have NaNs
columns_with_nans = ['bh_hectares', 'uc_hectares', 
                     'assessment_hectares', 
                     'fire_spread_rate', 'temperature', 
                     'relative_humidity', 'wind_speed', 
                     'impact_score'
                     ]
df = dc.clean_data(df, columns_with_nans)

#Trains the model **Need to optimize the model**
regression_model = mt.train_regression_model(df)
#Tensor model not used due to overfitting
#tensor_model = mt.train_tensor_model(df)

#Interface for using the prediction models
stop_input = ""
while(True):
    if stop_input == 'Yes':
        break

    #Gets features from the user
    bh_hectares = input("bh_hectares: ")
    uc_hectares = input("uc_hectares: ")
    assessment_hectares = input("assessment_hectares: ")
    fire_spread_rate = input("fire_spread_rate: ")
    temperature = input("temperature: ")
    relative_humidity = input("relative_humidity: ")
    wind_speed = input("wind_speed: ")

    #Stores new features
    new_features = pd.DataFrame({
        'bh_hectares': [bh_hectares],
        'uc_hectares': [uc_hectares],
        'assessment_hectares': [assessment_hectares],
        'fire_spread_rate': [fire_spread_rate],
        'temperature': [temperature],
        'relative_humidity': [relative_humidity],
        'wind_speed': [wind_speed]
        })
    
    #Loads scalers for the models
    regression_scaler = joblib.load('regression_scaler.save')
    #Tensor scaler not needed
    #tensor_scaler = joblib.load('tensor_scaler.save')

    #Models make a prediction of the final burn size and the impact score
    regression_prediction = mu.use_regression_model(regression_model, new_features, regression_scaler)
    #Tensor model not used
    #tensor_prediction = mu.use_tensor_model(tensor_model, new_features, tensor_scaler)

    #Prints the results of the model
    print(regression_prediction)
    #Tensor model not used
    #print(tensor_prediction)
    
    stop_input = input("Stop? ")
    
#df['fire_cause'] = df.apply(ffc.filter_fire_causes, axis=1)
#df_filtered_causes = ffc.filter_fire_causes(df)
#print(df_filtered_causes.iloc[12])