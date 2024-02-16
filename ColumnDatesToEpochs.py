import pandas as pd

def dates_to_epochs(datetime_column):
    
    datetime_column = pd.to_datetime(datetime_column)
    epoch = pd.Timestamp('1970-01-01')
    datetime_column = (datetime_column - epoch) // pd.Timedelta('1s')
    
    return datetime_column

def column_dates_to_epochs(df):
    df['fire_start_date'] = df['fire_start_date'].apply(dates_to_epochs(df['fire_start_date']))
    df['discovered_date'] = df['discovered_date'].apply(dates_to_epochs(df['discovered_date']))
    df['reported_date'] = df['reported_date'].apply(dates_to_epochs(df['reported_date']))
    df['dispatch_date'] = df['dispatch_date'].apply(dates_to_epochs(df['dispatch_date']))
    df['start_for_fire_date'] = df['start_for_fire_date'].apply(dates_to_epochs(df['start_for_fire_date']))
    df['assessment_datetime'] = df['assessment_datetime'].apply(dates_to_epochs(df['assessment_datetime']))
    df['ia_arrival_at_fire_date'] = df['ia_arrival_at_fire_date'].apply(dates_to_epochs(df['ia_arrival_at_fire_date']))
    df['fire_fighting_start_date'] = df['fire_fighting_start_date'].apply(dates_to_epochs(df['fire_fighting_start_date']))
    df['first_bucket_drop_date'] = df['first_bucket_drop_date'].apply(dates_to_epochs(df['first_bucket_drop_date']))
    df['bh_fs_date'] = df['bh_fs_date'].apply(dates_to_epochs(df['bh_fs_date']))
    df['uc_fs_date'] = df['uc_fs_date'].apply(dates_to_epochs(df['uc_fs_date']))
    df['to_fs_date'] = df['to_fs_date'].apply(dates_to_epochs(df['to_fs_date']))
    df['ex_fs_date'] = df['ex_fs_date'].apply(dates_to_epochs(df['ex_fs_date'])) #call this function in the main file once Helen is done editing