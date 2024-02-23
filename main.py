#Main File, Click run
import pandas as pd
import math
import joblib
import ImpactScore as imsc
import ColumnDatesToEpochs as cde
import FilterFireCause as ffc
import ModelTrainer as mt
import ModelUse as mu
import DataCleaner as dc
import FireNumberTrimmer as fnt
import RegionMainCauses as rmc
import GetVulnerableRegions as gvr
import LetterToRegion as ltr
import TopBurnArea  as tba
import TopImpact as ti
import WildFireMainCause as wfmc
import GetIndigenousVulnerability as giv
import GetPopulationVulnerability as gpv

#Accurate when current size is above 1 hectare under 10% error
#When below 1 hectare, error increases drastically, however
#it doesn't matter because the area is so small anyways

#Store file path of the dataset
excel_file = 'fp-historical-wildfire-data-2006-2021.xlsx'

#Opens the dataset as a pandas dataframe
df = pd.read_excel(excel_file, engine='openpyxl')

#Removes rows where dates that have a typo
df.drop(index=1291, inplace=True)
df.drop(index=14316, inplace=True)

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
                     'impact_score', 'general_cause_desc'
                     ]
df = dc.clean_data(df, columns_with_nans)

# Extracting filtered cause information
fire_causes = ffc.filter_fire_causes(df)
#df = fire_causes[0]
cause_category = fire_causes[1]
cause_activity = fire_causes[2]
true_cause = fire_causes[3]

# Trimming the fire number to just the region code
df['fire_number'] = fnt.trim_fire_number(df['fire_number'])

#Finds the top three most vulnerable regions
df_vulnerable_regions = gvr.get_vulnerable_regions(df)
print(df_vulnerable_regions)
df_vulnerable_region_names = []
for region in df_vulnerable_regions:
    df_vulnerable_region_names.append(ltr.get_region_from_letter(region))

#Finds the main causes for the three most vulnerable regions
df_region_main_causes = []
for main_cause in df_vulnerable_regions:
    df_region_main_causes.append(rmc.region_main_causes(main_cause, df, cause_category, cause_activity, true_cause))

#Finds the main industries, activities, and true causes in the top three most vulnerable regions
counter = 0
for region in df_vulnerable_region_names:
    print(region + ":")
    for info in df_region_main_causes:
        if counter == 0:
            print("Main Industries/Categories Causing Wildfires:")
            print(info[counter])
            counter += 1
        elif counter == 1:
            print("Main Activities Causing Wildfires:")
            print(info[counter])
            counter += 1
        else:
            print("Main True Causes Causing Wildfires")
            print(info[counter])
            counter = 0
    print()

#Within each of the top three most vulnerable regions, it finds
counter = 0
for region in df_vulnerable_region_names:
    print("Top 5 wildfires in " + region + " with largest burn area with its causes:")
    for i in range(5):
        print("#", (i + 1),  ": ", tba.get_top_burn_area(df, df_vulnerable_regions[counter])[i],  " hectares")
        print("Main reason for #",  (i + 1),  ": ",  wfmc.get_cause_of_wf_burn(df, tba.get_top_burn_area(df, df_vulnerable_regions[counter])[i]))
    print()
    print("Top 5 wildfires in " + region + " with largest impact score with its causes:")
    for i in range(5):
        print("#",  (i + 1),  ": ",  ti.get_top_impact(df, df_vulnerable_regions[counter])[i])
        print("Main reason for #",  (i + 1),  ": ",  wfmc.get_cause_of_wf_impact(df, ti.get_top_impact(df, df_vulnerable_regions[counter])[i]))
    print()
    print()
    counter += 1

for region in df_vulnerable_regions:
    print("Population Vulnerability in " + ltr.get_region_from_letter(region) + ": ", gpv.get_population_vulnerability(df, region), "%")
    print("Indigenous Vulnerability in " + ltr.get_region_from_letter(region) + ": ", giv.get_indigenous_vulnerability(df, region), "%")

#Trains the model 
regression_model = mt.train_regression_model(df)
#Tensor model not used due to overfitting
#tensor_model = mt.train_tensor_model(df)

print(df['impact_score'])

#Interface for using the prediction models
stop_input = ""
while(True):
    if stop_input == 'Yes':
        break

    #Inputs features from the user
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
    
    #Models make a pre0diction of the final burn size and the impact score
    regression_prediction = mu.use_regression_model(regression_model, new_features, regression_scaler)
    #Tensor model not used
    #tensor_prediction = mu.use_tensor_model(tensor_model, new_features, tensor_scaler)

    #Prints the results of the model
    print(regression_prediction)
    #Tensor model not used
    #print(tensor_prediction)
    
    stop_input = input("Stop? ")