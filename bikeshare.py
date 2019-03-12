# Importing packages and functions
import pandas as pd
import datetime # operations to parse dates

import calendar
import csv

# supported cities, months, days
city_data = {'chicago': 'chicago.csv',
          'new york': 'new_york_city.csv',
          'washington': 'washington.csv'}
months = {v.lower(): k for k, v in enumerate(calendar.month_name)}
#months = ('january', 'february', 'march', 'april', 'may', 'june')
days = {v.lower(): k for k, v in enumerate(calendar.day_name)}
#days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')

#get user input for city
def get_city():
    '''Asks the user for a city and returns the specified filter.
    Args:
        none.
    Returns:
        (str) City filter for the bikeshare data.
    '''
    while True:
        try:
            city = input('Hello! Let\'s explore some US bikeshare data!\nWould you like to see data for Chicago, New York, or Washington?\n')
        except ValueError:
            print('That is not a valid answer. Please try again.')
        if city.lower() in city_data.keys():
            return city.lower()
        else:
            print('That is not a valid answer. Please try again.')

# 1) pick a city   
city = get_city()
print('Great! We\'ll use %s.' % city)

def get_raw_city_data(city):
    '''Read CSV (comma-separated) file into DataFrame
    Args:
        city filter from get_city()
    Returns:
        raw_city_data df for the specified city's bikeshare data.
    '''
    raw_city_data = pd.read_csv(city_data[city])
    return raw_city_data
  
  # 3) load data
raw_city_data = get_raw_city_data(city)

def clean_data(raw_city_data):
    '''Read CSV (comma-separated) file into DataFrame
    Args:
        (obj) raw_city_data from get_raw_city_data(city)
    Returns:
        (obj) parsed raw_city_data   
    '''

    raw_city_data['Journey'] = raw_city_data['Start Station'].str.cat(raw_city_data['End Station'], sep=' to ')
    
    #format column names
    raw_city_data.columns = [x.strip().replace(' ', '_') for x in raw_city_data.columns]
    #make all headers lowercase
    raw_city_data.columns=map(str.lower, raw_city_data.columns)
    
    return raw_city_data

def parse_data(raw_city_data):
'''Read CSV (comma-separated) file into DataFrame
Args:
    (obj) raw_city_data from get_raw_city_data(city)
Returns:
    (obj) parsed raw_city_data   
''' 
# parse datetime 
raw_city_data['start_time'] = pd.to_datetime(raw_city_data['start_time'])
raw_city_data['end_time'] = pd.to_datetime(raw_city_data['end_time'])

# extract month and hour from the Start Time column to create month, hour columns
raw_city_data['month'] = raw_city_data['start_time'].dt.month
raw_city_data['day_of_week'] = raw_city_data['start_time'].dt.weekday_name
raw_city_data['hour'] = raw_city_data['start_time'].dt.hour 

return raw_city_data

def filter_data(raw_city_data):
    '''Asks the user for a time period and filter the basic processed data according 
        to the specified filter and returns the filtered data and the filter name.
    Args:
        (obj) basic processed data
    Returns:
        (obj) filtered data
    '''

    # loop for handling invalid entries
    while True: 
        time_period = input('Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n').lower()
        print('Great! Time period selected: %s' % time_period)
        if time_period in ('month', 'day', 'none'):
            break
        print('Enter a valid input provided in the options')

    if time_period =='month':
    #ask for the month of choice
        while True:
            month_selection = input('Select a month, January - June \n')
            if month_selection.lower() in months:
                print('Great! We\'ll use %s.' % month_selection)
                month_selection = months.get(month_selection)
                filtered_city_data = raw_city_data[raw_city_data['start_time'].dt.month==month_selection]
                
                break

            print('That is not a valid answer. Please try again.')
            
    elif time_period =='day':
        while True:
            day_selection = input('Which day of the week? \n')
            if day_selection.lower() in days:
                print('Great! We\'ll use %s.' % day_selection)
                day_selection = days.get(day_selection)
                filtered_city_data = raw_city_data[raw_city_data['start_time'].dt.dayofweek==day_selection]
                break

            print('That is not a valid answer. Please try again.')
                
    else:
        filtered_city_data = raw_city_data # for none option

    return filtered_city_data

 def display_statistics(filtered_city_data):
    '''Displays city data statistics (trip, user) on the specified filters
    Args:
        (ob) filtered_city_data
    Returns:
        statistics
    '''
    #Print heading that specifies selected city, filters
    print('\n')
    print('-------------------------------------')    


    """Display statistics on the most popular stations and trip."""
    print('\nStation Info:')
    # display most commonly used start station & end station
    popular_start_station = filtered_city_data['start_station'].mode().to_string(index = False)
    popular_end_station = filtered_city_data['end_station'].mode().to_string(index = False)
    print('Popular Start Station: ', popular_start_station)
    print('Popular End Station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_journey = filtered_city_data['journey'].mode().to_string(index = False)
    print('Popular Journey: ', popular_journey)

    """Displays statistics on the total and average trip duration."""
    print('\nOther Ridership Data:')
    # display total travel time
    total_travel_time = filtered_city_data['trip_duration'].sum()
    print('Total Time Travel:', total_travel_time)
    # display mean travel time
    mean_travel_time = filtered_city_data['trip_duration'].mean()
    print('Mean Time Travel:', mean_travel_time)

    """Displays statistics on bikeshare users."""
    print('\nUser Info:')
    #Display counts of user types
    user_types=filtered_city_data['user_type'].value_counts()
    print(user_types)
    print('\n')
    
    if city == 'chicago' or city == 'new york': 
        user_statistics(filtered_city_data)

def display_month_day_hour_statistics(filtered_city_data):
    '''Displays city data statistics (month, day, hour) on the specified filters.
       Example: Finds and prints the most popular day of week (Monday, Tuesday, etc.) for start time.
    Args:
        (ob) filtered_city_data
    Returns:
        statistics
    '''
    #Print heading that specifies selected city, filters
    print('\n')
    print('-------------------------------------')
    # display total number of trips for this city and filter
    #print('Total trips: ', (filtered_city_data['Start_Time'].count()))
    
    """Display statistics on the most frequent times of travel."""
    print('\nTrip Info:')
    # display the most common month
    popular_month = filtered_city_data['month'].mode()[0]
    print(popular_month, 'is the month with the highest ridership')

    # display the most common day of week
    popular_day = filtered_city_data['day_of_week'].mode()[0]
    print(popular_day, 'is the day of the week with the highest ridership')
        
    # display the most common hour (from 0 to 23)
    popular_hour = filtered_city_data['hour'].mode()[0]
    print(popular_hour, 'is the most common trip start hour')

def user_statistics(filtered_city_data):
    '''Displays city data statistics on the specified filters, for specified cities
    Args:
        (obj) filtered_city_data
    Returns:
        user statistics for chicago and nyc data only 
    '''
    #Display counts of gender
    #Display earliest, most recent, and most common year of birth
    #gender_count = city_data.groupby('Gender')['Gender'].count()
    gender_count = filtered_city_data['gender'].value_counts()
    print(gender_count)
    earliest = int(filtered_city_data['birth_year'].min(skipna=True))
    recent = int(filtered_city_data['birth_year'].max(skipna=True))
    mode = int(filtered_city_data['birth_year'].mode())
    print('The oldest birth year in the dataset is listed as {}.\nThe most recent birth year in the dataset is {}.'
          '\nThe most common birth year in the dataset is {}.'.format(earliest, recent, mode))
    print('\n')
 

def display_data(filtered_city_data, row):
    """
    Asks the user if they would you like to view individual trip data and loads the raw data 
    Args:
        (obj) filtered city_data
        ilocs
    Returns:
        data in detail
    """
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n').lower()
    if display == 'yes' or display == 'y':
        print(filtered_city_data.iloc[row:row+5])
        row += 5
        return display_data(filtered_city_data, row)
    if display == 'no' or display == 'n':
        return
    else:
        print('That is not a valid answer. Please try again.')
        return display_data(filtered_city_data, row)


      
def main():
    """
    Loads analysis and data for the specified city and filters.
    """
    # 1) pick a city   
    city = get_city()
    print('Great! We\'ll use %s.' % city)
    
    # 2) load data
    raw_city_data = get_raw_city_data(city)
    
    #3) clean data
    clean_data(raw_city_data)
 
    #4) parse data
    parse_data(raw_city_data)
    
    #5) filter data
    filtered_city_data = filter_data(raw_city_data)
    
    #6) display statistics
    display_statistics(filtered_city_data)
    
    #7) display statistics on most popular month and day overall
    display_month_day_hour_statistics(filtered_city_data)
    
    #8) see data details
    see_data = display_data(filtered_city_data, row=76)

    #9) restart if you wish
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes' or restart.lower() == 'y':
        main()
    elif restart.lower() == 'no' or restart.lower() == 'n':
        return
    else:
        print("\nThat is not a valid answer. Please try again.")
        return restart()

if __name__ == "__main__":
	main()