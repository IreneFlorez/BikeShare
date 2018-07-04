# Importing packages and functions
import pandas as pd
import datetime # operations to parse dates
import time
import csv

# supported cities
cities = {'chicago': 'chicago.csv',
          'new york': 'new_york_city.csv',
          'washington': 'washington.csv',}

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

#get user input for city
def get_city_filter():
    '''Asks the user for a city and returns the specified filter.
    Args:
        none.
    Returns:
        (str) City filter for the bikeshare data.
    '''
    while True:
        try:
            city_input = input('Hello! Let\'s explore some US bikeshare data!\nWould you like to see data for Chicago, New York, or Washington?\n')
        except ValueError:
            print('That is not a valid answer. Please try again.')
        if city_input.lower() in cities.keys():
            return city_input.lower()
        else:
            print('That is not a valid answer. Please try again.')

# get time period for filtering
def get_time_period_filter():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (str) Time period filter for the bikeshare data.
    '''
    while True:  
        time_period_filter = input('Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n').lower()
        if time_period_filter == 'month' or time_period_filter == 'm':
            get_month_filter()
            return "month"
        elif time_period_filter == 'day' or time_period_filter == 'd':
            get_day_filter()
            return "day"
        elif time_period_filter == 'none' or time_period_filter == 'n':
            return 'none'
        else:    
            print('That is not a valid answer. Please try again.')

# get month for filtering
def get_month_filter():
    '''Asks the user which month they want to filter for and returns the specified filter
    Args:
        none.
    Returns:
        (str) Month filter for the bikeshare data.
    '''
    while True:
        month_selection = input('Select a month, January - June \n')
        if month_selection.lower() in months:
            return month_selection            
            print('\n')
            print('-------------------------------------')
            print('Great! We\'ll use %s.' % month_selection)
        print('That is not a valid answer. Please try again.')

def get_day_filter():
    '''Asks the user which day they want to filter for and returns the specified filter
    Args:
        none.
    Returns:
        (str) Day filter for the bikeshare data.
    '''
    while True:
        day_selection = input('Which day of the week? \n')
        if day_selection.lower() in days:
            return day_selection
            print('Great! We\'ll use %s.' % day_selection)
        print('That is not a valid answer. Please try again.')
    
def get_data(filename):
    '''Read CSV (comma-separated) file into DataFrame
    Args:
        city filter from get_city_filter()
    Returns:
        DataFrame for the specified city's bikeshare data.
    '''
    return pd.read_csv(filename)

# def month_day_allotment(city_data):
#     period = get_time_period_filter()
#     if (period == 'month'):
#         city_data['Start Time'].dt.month 
#     elif (period == 'day'):
#         city_data['Start Time'].dt.weekday_name
#     elif (period == 'none'):

#     print('Great! We\'ll use %s' % period)

def parse_data(city_data):
    '''convert columns to datetime, extract/concatenate data to create new columns, replace spaces with underscores
    Args:
        city_data
    Returns:
        Parsed DataFrame for the specified city's bikeshare data.
    '''
    # parse datetime 
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    city_data['End Time'] = pd.to_datetime(city_data['End Time']) 
    # extract month and hour from the Start Time column to create month, hour columns
    city_data['Month'] = city_data['Start Time'].dt.month
    city_data['Hour'] = city_data['Start Time'].dt.hour 
    # create 'journey' column that concatenates start_station, end_station 
    city_data['Journey'] = city_data['Start Station'].str.cat(city_data['End Station'], sep=' to ')
    #format column names
    city_data.columns = [x.strip().replace(' ', '_') for x in city_data.columns]
    return city_data

def display_data(city_data, row):
    """
    Asks the user if they would you like to view individual trip data and loads the raw data 
    Args:
        (obj) filtered data
        (str) iloc
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



def statistics(city_data):
    '''Calculates and prints out the descriptive statistics about the city and time period
    specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''    
    """Display statistics on the most frequent times of travel."""
    print('\nTrip Info:')
    # display the most common month
    popular_month = city_data['Month'].mode()[0]
    print(popular_month, 'is the month with the highest ridership')

    # display the most common day of week
    index = int(city_data['Start_Time'].dt.dayofweek.mode())
    popular_day = days[index]
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

def inconsistant_data_handling(city, city_data): 
    '''Calculates and prints out the gender and birth year statistics about Chicago and New York
    Args:
        city
        city_data
    Returns:
        none.
    '''    
    """Display statistics on the most frequent times of travel."""   
    #Display counts of gender
    # Display earliest, most recent, and most common year of birth
    if city == 'chicago' or city == 'new york': 
        gender_count = city_data['Gender'].value_counts()
        print(gender_count)
        earliest = int(city_data['Birth_Year'].min())
        recent = int(city_data['Birth_Year'].max())
        mode = int(city_data['Birth_Year'].mode())
        print('The oldest birth year in the dataset is listed as {}.\nThe most recent birth year in the dataset is {}.'
          '\nThe most common birth year in the dataset is {}.'.format(earliest, recent, mode))
    print('\n')

def restart_program():
    '''asks user if they would like to restart the program
    Args:
        none.
    Returns:
        none.
    '''
    restart = input('Would you like to restart? Type \'yes\' or \'no\n')
    if restart.lower() == 'yes':
        main()
    else:
        quit()

def main():
    """
    Loads analysis and data for the specified city and filters by month and day if applicable.
    """
    # pick a city
    city = get_city_filter()
    # load the file with input from above
    city_data = get_data(cities[city])
    # choose time period
    # month_day_allotment(city_data)
    parse_data(city_data)
    period = get_time_period_filter()
    if (period == 'month'):
        city_data['Start_Time'].dt.month 
    elif (period == 'day'):
        city_data['Start_Time'].dt.weekday_name
    
    statistics(city_data)
    inconsistant_data_handling(city, city_data)
    display_data(city_data, row=76)
    restart_program()

if __name__ == "__main__":
	main()
