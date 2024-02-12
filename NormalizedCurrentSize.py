import MagnitudeAllCurrentSizes as macs
def get_normalized_current_size(df, current_size):
    return current_size / macs.get_magnitude_all_current_sizes(df)