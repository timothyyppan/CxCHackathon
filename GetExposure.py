def get_exposure(df, region):
    df_filtered = df[df['fire_number'] == region]
    current_size_sum = df_filtered['current_size'].sum()

    exposure = current_size_sum / (df['fire_year'].iloc[0] - df['fire_year'].iloc[-1])
    
    return exposure
