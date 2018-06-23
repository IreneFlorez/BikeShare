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
  #print('Accessing %s' % filename)
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
      #return get_month(city_data)

# get day of week for filtering
def get_day():
    try:
        return input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
    except:    
        print('That is not a valid answer. Please try again.')
        #return get_day(city_data)
      
def main():
    # pick a city
    city = get_city()
    #print('Great! We\'ll use %s.' % city)
    
    # load the file with input from above
    city_data = get_city_data(cities[city])
    # parse datetime and column names
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    city_data['End Time'] = pd.to_datetime(city_data['End Time'])  
    city_data.columns = [x.strip().replace(' ', '_') for x in city_data.columns]

    # choose time period
    period = get_time_period()
    #print('Filtering on time period: %s' % period)

    if (period == 'month'):
      month = get_month()
      city_data['Start_Time'].dt.month 
      #print('Month selected: %s.' % month)
    elif (period == 'day'):
      day = get_day()
      city_data['Start_Time'].dt.dayofweek  
      #print('Day selected: %s.' % day)

#Print heading that specifies selected city, filters
    print('\n')
    print('-------------------------------------')
    print('Great! We\'ll use %s.' % city)
    print('Time period selected: %s' % period)
    if (period == 'month'):
      print(month)
    elif (period == 'day'):
      print(day)

    #For context, print total number of trips for this city and filter
    print("total trips" (city_data['Start Time'].count() )
    #print('Month selected: %s.' % month)
    #print('Day selected: %s.' % day)

    # TO DO: display the most common month

    # TO DO: display the most common day of week

    # TO DO: display the most common start hour

    # TO DO: display most commonly used start station

    # TO DO: display most commonly used end station

    # TO DO: display most frequent combination of start station and end station trip

    # TO DO: display total travel time

    # TO DO: display mean travel time

    # TO DO: Display counts of user types

    # TO DO: Display counts of gender

    # TO DO: Display earliest, most recent, and most common year of birth

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes' or restart.lower() == 'y':
        main()
    elif restart.lower() == 'no' or restart.lower() == 'n':
        return
    else:
        print("\nI'm not sure if you wanted to restart or not. Let's try again.")
        return restart()

if __name__ == "__main__":
	main()
