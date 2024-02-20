
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
    
    fire_number = df['fire_number']

    # Isolating wildfires of that certain region by acquiring indices of rows containing fire code
    
    region_indices = []
    for i in range(len(fire_number)):
        if fire_number[i] == region:
            region_indices.append(i)

    #for i, string in enumerate(fire_number):
    #    if fire_code in string:
    #        region_indices.append(i)

    print(region_indices)
    for i in region_indices:
        region_fire_causes = df_filtered_causes[region_indices, :]

    print(type(region_fire_causes))
    return region_fire_causes