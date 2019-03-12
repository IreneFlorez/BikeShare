# Importing packages and functions
import pandas as pd
import datetime # operations to parse dates
import time
import calendar
import csv

# supported cities, months, days
city_data = {'chicago': 'chicago.csv',
          'new york': 'new_york_city.csv',
          'washington': 'washington.csv',}
cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
months = {v.lower(): k for k, v in enumerate(calendar.month_name)}
days = {v.lower(): k for k, v in enumerate(calendar.day_name)}

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
            city_selection = input('Hello! Let\'s explore some US bikeshare data!\nWould you like to see data for Chicago, New York, or Washington?\n')
        except ValueError:
            print('That is not a valid answer. Please try again.')
        if city_selection.lower() in city_data.keys():
            return city_selection.lower()
        else:
            print('That is not a valid answer. Please try again.')

# get time period for filtering
def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (str) Time period filter for the bikeshare data.
    '''
    while True: 
        time_period = input('Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n').lower()
        print('Great! Time period selected: %s' % time_period)
        if time_period == 'month' or time_period == 'm':
            month = get_month()
            return 'month'
        elif time_period == 'day' or time_period == 'd':
            day = get_day()
            return 'day'
        elif time_period == 'none' or time_period == 'n':
            print('Great! You selected none')
            return 'none'
        else: print('That is not a valid answer. Please try again.')
      
# get month for filtering
def get_month():
    '''Asks the user which month they want to filter for and returns the specified filter
    Args:
        none.
    Returns:
        (str) Month filter for the bikeshare data.
    '''
    while True:
        month_selection = input('Select a month, January - June \n')
        if month_selection.lower() in months:
            print('Great! We\'ll use %s.' % month_selection)
            return month_selection  
        print('That is not a valid answer. Please try again.')

# get day of week for filtering
def get_day():
    '''Asks the user which day they want to filter for and returns the specified filter
    Args:
        none.
    Returns:
        (str) Day filter for the bikeshare data.
    '''
    while True:
        day_selection = input('Which day of the week? \n')
        if day_selection.lower() in days:
            print('Great! We\'ll use %s.' % day_selection)
            return day_selection
        print('That is not a valid answer. Please try again.')

def load_data(city_selection, month_selection, day_selection, time_period):
    '''Read CSV (comma-separated) file into DataFrame
    Args:
        (str) city - name of the city to analyze - city filter from get_city()
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        DataFrame for the specified city's bikeshare data-containing city data filtered by month and day.   
    '''
    city_data = pd.read_csv(city_data[city_selection])

    # parse datetime 
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    city_data['End Time'] = pd.to_datetime(city_data['End Time']) 
    # extract month and hour from the Start Time column to create month, hour columns
    city_data['Month'] = city_data['Start Time'].dt.month
    city_data['day_of_week'] = city_data['Start Time'].dt.weekday_name
    city_data['Hour'] = city_data['Start Time'].dt.hour 
    # create 'journey' column that concatenates start_station, end_station 
    city_data['Journey'] = city_data['Start Station'].str.cat(city_data['End Station'], sep=' to ')
    #format column names
    city_data.columns = [x.strip().replace(' ', '_') for x in city_data.columns]

    # filter by month if applicable
    if month_selection != 'all':
        month_selection =  months.index(month_selection) + 1
        city_data = city_data[city_data['month'] == month_selection]
    # filter by day of week if applicable
    if day_selection != 'all':
        # filter by day of week to create the new dataframe
        city_data = city_data[ city_data['day_of_week'] == day_selection.title()]
    if time_period == 'none':
        Start_Time = time.time()

    return city_data

def display_statistics(city_data):
    '''Displays city data statistics on the specified filters
    Args:
        city_data
    Returns:
        statistics
    '''
    #Print heading that specifies selected city, filters
    print('\n')
    print('-------------------------------------')
    # display total number of trips for this city and filter
    #print('Total trips: ', (city_data['Start_Time'].count()))
    
    """Display statistics on the most frequent times of travel."""
    print('\nTrip Info:')
    # display the most common month
    popular_month = city_data['Month'].mode()[0]
    print(popular_month, 'is the month with the highest ridership')

    # display the most common day of week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(city_data['Start_Time'].dt.dayofweek.mode())
    popular_day = days_of_week[index]
    print(popular_day, 'is the day of the week with the highest ridership')

    # display the most common hour (from 0 to 23)
    popular_hour = city_data['Hour'].mode()[0]
    print(popular_hour, 'is the most common trip start hour')

    """Display statistics on the most popular stations and trip."""
    print('\nStation Info:')
    # display most commonly used start station & end station
    popular_start_station = city_data['Start_Station'].mode().to_string(index = False)
    popular_end_station = city_data['End_Station'].mode().to_string(index = False)
    print('Popular Start Station: ', popular_start_station)
    print('Popular End Station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_journey = city_data['Journey'].mode().to_string(index = False)
    print('Popular Journey: ', popular_journey)

    """Displays statistics on the total and average trip duration."""
    print('\nOther Ridership Data:')
    # display total travel time
    total_travel_time = city_data['Trip_Duration'].sum()
    print('Total Time Travel:', total_travel_time)
    # display mean travel time
    mean_travel_time = city_data['Trip_Duration'].mean()
    print('Mean Time Travel:', mean_travel_time)

    """Displays statistics on bikeshare users."""
    print('\nUser Info:')
    #Display counts of user types
    user_types=city_data['User_Type'].value_counts()
    print(user_types)
    print('\n')
    
    if city_data == 'chicago' or city_data == 'new york': 
        user_statistics(city_data)

def user_statistics(city_data):
    '''Displays city data statistics on the specified filters, for specified cities
    Args:
        city_data
    Returns:
        statistics
    '''
    #Display counts of gender
    # Display earliest, most recent, and most common year of birth
    #gender_count = city_data.groupby('Gender')['Gender'].count()
    gender_count = city_data['Gender'].value_counts()
    print(gender_count)
    earliest = int(city_data['Birth_Year'].min())
    recent = int(city_data['Birth_Year'].max())
    mode = int(city_data['Birth_Year'].mode())
    print('The oldest birth year in the dataset is listed as {}.\nThe most recent birth year in the dataset is {}.'
          '\nThe most common birth year in the dataset is {}.'.format(earliest, recent, mode))
    print('\n')

def display_data(city_data, row):
    """
    Asks the user if they would you like to view individual trip data and loads the raw data 
    Args:
        city_data
        ilocs
    Returns:
        raw data
    """
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n').lower()
    if display == 'yes' or display == 'y':
        print(city_data.iloc[row:row+5])
        row += 5
        return display_data(city_data, row)
    if display == 'no' or display == 'n':
        return
    else:
        print('That is not a valid answer. Please try again.')
        return display_data(city_data, row)
#https://stackoverflow.com/questions/43772362/how-to-print-a-specific-row-of-a-pandas-dataframe
#https://pandas.pydata.org/pandas-docs/stable/indexing.html


def main():
    """
    Loads analysis and data for the specified city and filters by month and day if applicable.
    """
    # pick a city   
    city = get_city()
    print('Great! We\'ll use %s.' % city)
    # choose time period
    time_period = get_time_period()
    city_selection = []
    # load the file with input from above
    # Filter by time period (month, day, none)
    load_data
    #city_data = load_data(city_data[city], month_selection, day_selection)
    display_statistics (city_data)
    see_data = display_data(city_data, row=76)

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

