
def region_main_causes(df, df_filtered_causes, region):
    # accounting for different input variations using title mapping
    region = region.upper() # this alone accounts for inputs such as 'c'
    title_mapping = { 
        # meanwhile, title mapping will also account for full name inputs.
        # this paired with the upper() function will account for any capitalization
        # variation.
        'CALGARY' : 'C',
        'EDSON' : 'E',
        'HIGH LEVEL' : 'H',
        'GRANDE PRAIRIE' : 'G',
        'LAC LA BICHE' : 'L',
        'FORT MCMURRAY' : 'M',
        'PEACE RIVER' : 'P',
        'ROCKY' : 'R',
        'SLAVE LAKE' : 'S',
        'WHITECOURT' : 'W'
    }

    if region in title_mapping:
        region = title_mapping[region]
    
    #print(df_filtered_causes['fire_number'])
    fire_number = df['fire_number']

    # Isolating wildfires of that certain region by acquiring indices of rows containing fire code
    
    region_indices = []
    for i in range(len(fire_number)):
        if fire_number[i] == region:
            region_indices.append(i)

    #for i, string in enumerate(fire_number):
    #    if fire_code in string:
    #        region_indices.append(i)

    #Is erroring because region_indices is empty, if condition is not executing so when we call a return statement, it is empty
    #This is because we need to chop off the last three numbers of fire_number
    #Also I noticed that there is only one item in fire_code, I think there needs to be a for loop
    print(region_indices)
    for i in region_indices:
        region_fire_causes = df_filtered_causes[region_indices, :]

    print(type(region_fire_causes))
    return region_fire_causes