#Calculates the percentage of the land that will be burnt for the average wildfire
def get_exposure(df, region):
    df_filtered = df[df['fire_number'] == region]
    AREAS = [25.34, 6.63, 2.67]

    if region == "Peace River":
        area = AREAS[0]
    elif region == "Slave Lake":
        area = AREAS[1]
    else:
        area = AREAS[2]

    exposure = ((df_filtered['current_size'] / area).sum()) / df_filtered.shape[0]

    return exposure
