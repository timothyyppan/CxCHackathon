def get_all_current_size(df):
    all_current_size = 0.0
    for current_size in df['current_size']:
        all_current_size += current_size
    return all_current_size