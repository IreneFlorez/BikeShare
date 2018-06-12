# BikeShare

# Python Script to Explore US Bikeshare Data
This Python script is written to explore data related to bike share systems for Chicago, New York City, and Washington. It imports data from csv files and computes descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

## How to run the script
You can run the script using a Python integrated development environment (IDE) such as Spyder. To install Spyder, you will need to [download the Anaconda installer](https://www.anaconda.com/download/). This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.

## Datasets
The datasets used for this script contain bike share data for the first six months of 2017.  You can access the original data files here [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data). Some data wrangling, to reduce columns and reformat, has been performed to condense these files to the core six columns used in this project. This makes the analysis and the evaluation in this project more straightforward.

The data is provided by [Motivate](https://www.motivateco.com/), which is a bike share system provider for many cities in the United States. The data files for all three cities contain the same six columns:
* Start Time
* End Time
* Trip Duration (in seconds)
* Start Station
* End Station
* User Type (Subscriber or Customer)

The Chicago and New York City files also contain the following two columns:
* Gender
* Birth Year

## Questions explored
The script answers the following questions about the bike share data:

Business Analysis
* How many bikes should each bikeshare have available?
* What is the optimal driving time between stations?

Popular times of travel
* What is the most popular month for start time?
* What is the most popular day of week (Monday, Tuesday, etc.) for start time?
* What is the most popular hour of day for start time?

Popular stations and trip
* What is the most popular start station and most popular end station?
* What is the most popular trip?

Trip duration
* What is the total trip duration and average trip duration?

User information
* What are the counts of each user type?
* What are the counts of gender?  (only available for NYC and Chicago)
* What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?

## Resources
https://pandas.pydata.org/pandas-docs/stable/api.html#datetimelike-properties
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html
