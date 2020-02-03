		
def make():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\n    Would you like to restart? (y or n):  ')
        if restart.lower() != 'y':
            break




