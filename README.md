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
