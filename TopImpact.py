#Finds the top five wildfires in a region that had the largest impact score
def get_top_impact(df, region):
    df = df[df['fire_number'] == region]
    df = df['impact_score'].sort_values(ascending=False)

    top_impact_score = df.head(5).values.tolist()

    return top_impact_score