
def region_main_causes(region, df, cause_category, cause_activity, true_cause):

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

   

    # Isolating wildfires of that certain region 
    df_region = df[df['fire_number'] == region]
    
    # Calling the fire cause industry/category data
    region_cause_category = cause_category[df['fire_number'] == region]

    # Determining main industry/category responsible for wildfire in a certain 
   # region_cause_category = df_region['general_cause_desc']

   

    return region_cause_category