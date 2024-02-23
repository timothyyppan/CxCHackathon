import pandas as pd

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

     # Isolating industries/categories, activities, and true causes responsible for wildfires in a certain region
    region_cat = cause_category[df['fire_number'] == region]
    region_act = cause_activity[df['fire_number'] == region]
    region_tc = true_cause[df['fire_number'] == region]

    #------------------------------------------------------------------------------------------------------------------------
    # Determining the main INDUSTRIES/CATEGORIES responsible for wildfires in certain region-------------------------------
    # Counting amounts of fire each industry/category is responsible for using a dictionary
    cat_counts = {}

    # Using a for loop that adds newly mentioned categories as it reads 
    # the column, to reduce unnecessary data
    for cat in region_cat:
        # Check if the category is already in the dictionary
        if cat in cat_counts:
            # Increment category's count
            cat_counts[cat] += 1
        else:
            # Add the category to the dictionary with a count of 1
            cat_counts[cat] = 1

    # Sorting the counts in descending order
    sorted_cat_counts = sorted(cat_counts, key=cat_counts.get, reverse=True)

    # Storing the two main industries/categories responsible for wildfires in certain region
    top_cat = [sorted_cat_counts[0], sorted_cat_counts[1]]

     # ----------------------------------------------------------------------------------------------------------------------
    # Determining the main ACTIVITIES responsible for wildfires in certain region-------------------------------
    # Counting amounts of fire each activity is responsible for using a dictionary
    act_counts = {}

    # Using a for loop that adds newly mentioned categories as it reads 
    # the column, to reduce unnecessary data
    for act in region_act:
        # Check if the activity is already in the dictionary
        if act in act_counts:
            # Increment category's count
            act_counts[act] += 1
        else:
            # Add the category to the dictionary with a count of 1
            act_counts[act] = 1

    # Sorting the counts in descending order
    sorted_act_counts = sorted(act_counts, key=act_counts.get, reverse=True)

    # Storing the two main activities responsible for wildfires in certain region
    top_act = [sorted_act_counts[0], sorted_act_counts[1]]

 # -----------------------------------------------------------------------------------------------------------
    # Determining the main TRUE CAUSES responsible for wildfires in certain region-------------------------------
    # Counting amounts of fire each true cause is responsible for using a dictionary
    tc_counts = {}

    # Using a for loop that adds newly mentioned true causes as it reads 
    # the column, to reduce unnecessary data
    for tc in region_tc:
        # Check if the activity is already in the dictionary
        if tc in tc_counts:
            # Increment category's count
            tc_counts[tc] += 1
        else:
            # Add the category to the dictionary with a count of 1
            tc_counts[tc] = 1

    # Sorting the counts in descending order
    sorted_tc_counts = sorted(tc_counts, key=tc_counts.get, reverse=True)

    # Storing the two main industries/categories responsible for wildfires in certain region
    top_tc = [sorted_tc_counts[0], sorted_tc_counts[1]]

    return top_cat, top_act, top_tc







