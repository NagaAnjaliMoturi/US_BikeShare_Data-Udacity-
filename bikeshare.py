import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter the city you want to analyze (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose from 'chicago', 'new york city', or 'washington'")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to filter by month? Please enter a month (january, february, march, april, may, june) or 'all' to apply no month filter: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid input. Please enter a valid month or 'none'")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to filter by day? Please enter a day (monday, tuesday, wednesday, thursday, friday, saturday, sunday) or 'all' to apply no day filter: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid input. Please enter a valid day or 'none' ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of Week'].str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('The Most Frequent Times of Travel...\n')

    # TO DO: display the most common month
    mc_month = df['Month'].mode()[0]
    print(f"The most common month is: {mc_month}")

    # TO DO: display the most common day of week
    mc_day = df['Day of Week'].mode()[0]
    print(f"The most common day of the week is: {mc_day}")

    # TO DO: display the most common start hour
    mc_hour = df['Hour'].mode()[0]
    print(f"The most common start hour is: {mc_hour}")

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nThe Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station
    mc_start_station = df['Start Station'].mode()[0]
    print(f"The most common start station is: {mc_start_station}")

    # TO DO: display most commonly used end station
    mc_end_station = df['End Station'].mode()[0]
    print(f"The most common end station is: {mc_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    mc_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent trip is from {mc_trip[0]} to {mc_trip[1]}")

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time is: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time is: {mean_travel_time} seconds")

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser Stats...\n')

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types:\n")
    for user_type,count in user_types.items():
        print(f"{user_type}: {count}")
    print()
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        for gender,count in gender_counts.items():
            print(f"{gender}: {count}")
    else:
        print("Gender data is not available for this city.")
    print()
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_by = int(df['Birth Year'].min())
        most_recent_by = int(df['Birth Year'].max())
        most_common_by = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_by}")
        print(f"Most recent year of birth: {most_recent_by}")
        print(f"Most common year of birth: {most_common_by}")
    else:
        print("Birth year data is not available for this city.")

    print('-'*40)

def Hourly_Usage(df):
    """Displays the average of bikes usage by hour of day"""
    hourly_usage = df.groupby(['Day of Week', 'Hour']).size()
    avg_hourly_usage = hourly_usage.mean()
    print("\nHourly Usage...\n")
    print("   Day     Hour    Usage") 
    for (day, hour), usage in hourly_usage.items():
        print(f"{day:<12} {hour:<4} {usage}")
    print(f"\nAverage Hourly Usage : {avg_hourly_usage}")
    
    
def display_raw_data(df):
    "User can view the raw data in chuncks of 5 rows"
    i = 0
    while True:
        show_data = input("Would you like to view 5 lins of raw data? Enter 'Yes' or 'No': ").lower()
        if show_data == 'yes':
            print(df.iloc[i:i+5])
            i+=5
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        if i >= len(df):
            print("No more data to display")
            break
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Hourly_Usage(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


    
if __name__ == "__main__":
    main()
