def get_top_burn_area(df, region):
    df = df[df['fire_number'] == region]
    df = df['current_size'].sort_values(ascending=False)

    top_current_size = df.head(5).values.tolist()
    
    return top_current_size