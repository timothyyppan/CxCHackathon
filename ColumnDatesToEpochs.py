import pandas as pd

def dates_to_epochs(datetime_element):
    
    datetime_element = pd.to_datetime(datetime_element)
    epoch = pd.Timestamp('1970-01-01')
    epoch_time = (datetime_element - epoch) // pd.Timedelta('1s')
    
    return epoch_time

def column_dates_to_epochs(df):
    df['fire_start_date'] = df['fire_start_date'].apply(dates_to_epochs)
    df['discovered_date'] = df['discovered_date'].apply(dates_to_epochs)
    df['reported_date'] = df['reported_date'].apply(dates_to_epochs)
    df['dispatch_date'] = df['dispatch_date'].apply(dates_to_epochs)
    df['start_for_fire_date'] = df['start_for_fire_date'].apply(dates_to_epochs)
    df['assessment_datetime'] = df['assessment_datetime'].apply(dates_to_epochs)
    df['ia_arrival_at_fire_date'] = df['ia_arrival_at_fire_date'].apply(dates_to_epochs)
    df['fire_fighting_start_date'] = df['fire_fighting_start_date'].apply(dates_to_epochs)
    df['first_bucket_drop_date'] = df['first_bucket_drop_date'].apply(dates_to_epochs)
    df['bh_fs_date'] = df['bh_fs_date'].apply(dates_to_epochs)
    df['uc_fs_date'] = df['uc_fs_date'].apply(dates_to_epochs)
    df['to_fs_date'] = df['to_fs_date'].apply(dates_to_epochs)
    df['ex_fs_date'] = df['ex_fs_date'].apply(dates_to_epochs)