# Importing packages and functions
import time
import pandas as pd
import numpy as np
import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.
import matplotlib as mpl # Still required to change the sizes of plots

#get user input for city
def get_city():
    try:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York City, or Washington?\n')
        print('Getting data....')
        # read data and assign to city_data
        city_data = pd.read_csv("%s.csv" % city.lower().replace(' ', '_'))
        city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
        city_data['End Time'] = pd.to_datetime(city_data['End Time'])
        city_data['day_of_week'] = city_data['Start Time'].dt.weekday_name
        city_data['month'] = city_data['Start Time'].dt.strftime('%B')
        city_data['hour'] = city_data['Start Time'].dt.strftime('%H %p')
        print('Done!')
        return city_data
    except:
        print('\nThat is not a valid city, try again\n')
        get_city()

# get time period for filtering
def get_time_period():
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n').lower()
        if time_period == 'month' or time_period == 'm':
            return ['month', get_month()]
        elif time_period == 'day' or time_period == 'd':
            return ['day', get_day()]
        elif time_period == 'none' or time_period == 'n':
            return ['none', 'no filter']
        else:    
            print('That is not a valid answer. Please try again.')
        return get_time_period()

# get user input for month (all, january, february, ... , june)
def get_month(city_data):
    try:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
        return city_data[city_data['Start Time'].dt.month == datetime.strptime(month, '%B').month]
    except:
        print("\nI'm sorry, I'm not sure which month you're trying to filter by. Let's try again.")
        return get_month(city_data) 

# get user input for day of week (all, monday, tuesday, ... sunday)
def get_day(city_data):
    try:
        day_of_week = input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
        return city_data[city_data['day_of_week'] == day]
    except:    
        print("\nI'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")
        return get_day(city_data)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
