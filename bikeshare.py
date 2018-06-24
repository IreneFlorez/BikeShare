# Importing packages and functions
import pandas as pd
import numpy as np
import datetime # operations to parse dates
import time
import csv

# supported cities
cities = {'chicago': 'chicago.csv',
          'new york': 'new_york_city.csv',
          'washington': 'washington.csv',}

#get user input for city
def get_city():
  city_input = input('Hello! Let\'s explore some US bikeshare data!\nWould you like to see data for Chicago, New York, or Washington?\n')
  if city_input.lower() in cities.keys():
    return city_input.lower()
  else:
    print('That is not a valid answer. Please try again.')

def get_city_data(filename):
  return pd.read_csv(filename)

# get time period for filtering
def get_time_period():
  time_period = input('Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n').lower()
  if time_period == 'month' or time_period == 'm':
      return 'month'
  elif time_period == 'day' or time_period == 'd':
      return 'day'
  elif time_period == 'none' or time_period == 'n':
      return 'none'
  else:    
      print('That is not a valid answer. Please try again.')

# get month for filtering
def get_month():
    try:
      return input('January, February, March, April, May, or June?\n').lower()
    except:
      print('That is not a valid answer. Please try again.')

# get day of week for filtering
def get_day():
    try:
        return input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
    except:    
        print('That is not a valid answer. Please try again.')

def display_data(city_data, row):
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
    # pick a city
    city = get_city()
    
    # load the file with input from above
    city_data = get_city_data(cities[city])

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

    # choose time period
    period = get_time_period()
    #print('Filtering on time period: %s' % period)

    if (period == 'month'):
      month = get_month()
      city_data['Start_Time'].dt.month 
    elif (period == 'day'):
      day = get_day()
      city_data['Start_Time'].dt.weekday_name

#Print heading that specifies selected city, filters
    print('\n')
    print('-------------------------------------')
    print('Great! We\'ll use %s.' % city)
    print('Time period selected: %s' % period)

    # display total number of trips for this city and filter
    print('Total trips: ', (city_data['Start_Time'].count()))
    
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

    print('\nStation Info:')
    # display most commonly used start station & end station
    popular_start_station = city_data['Start_Station'].mode().to_string(index = False)
    popular_end_station = city_data['End_Station'].mode().to_string(index = False)
    print('Popular Start Station: ', popular_start_station)
    print('Popular End Station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_journey = city_data['Journey'].mode().to_string(index = False)
    print('Popular Journey: ', popular_journey)

    print('\nOther Ridership Data:')
    # display total travel time
    total_travel_time = city_data['Trip_Duration'].sum()
    print('Total Time Travel:', total_travel_time)
    # display mean travel time
    mean_travel_time = city_data['Trip_Duration'].mean()
    print('Mean Time Travel:', mean_travel_time)

    print('\nUser Info:')
    #Display counts of user types
    user_types=city_data['User_Type'].value_counts()
    print(user_types)

    #Display counts of gender
    gender_count=city_data['Gender'].value_counts()
    print(gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest = int(city_data['Birth_Year'].min())
    recent = int(city_data['Birth_Year'].max())
    mode = int(city_data['Birth_Year'].mode())
    print('The oldest birth year in the dataset is listed as {}.\nThe most recent birth year in the dataset is {}.'
          '\nThe most common birth year in the dataset is {}.'.format(earliest, recent, mode))

    see_data = display_data(city_data, row=76)

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes' or restart.lower() == 'y':
        main()
    elif restart.lower() == 'no' or restart.lower() == 'n':
        return
    else:
        print("\nI'm not sure if you wanted to restart or not. Let's try again.")
        return restart()

    #TO DO:
    print('\nBusiness Analysis:')
    #How many bikes should each bikeshare have available?
    #What is the optimal driving time between stations?

if __name__ == "__main__":
	main()
