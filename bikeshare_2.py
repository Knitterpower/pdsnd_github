#Project about bikeshare data

#Import libraries
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    city = ''
    month = ''
    day = ''           
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city == '':
        c_input = input('\nWhat city do you want to analyze? -chicago, new york city, washington \n')
        c = c_input.lower()
        if c == 'chicago' or c == 'new york city' or c == 'washington':
           city = c
        else:
           print('Something went wrong. Try Again')  

    # TO DO: get user input for month (all, january, february, ... , june)
    while month == '':
        m_input = input('\nWhat month do you want to analyze? Type "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" OR "all" for no filter \n')
        m = m_input.title()
        if m == 'Jan' or m == 'Feb' or m == 'Mar' or m == 'Apr' or m == 'May' or m == 'Jun' or m == 'Jul' or m == 'Aug' or m == 'Sep' or m == 'Oct' or m == 'Nov' or m == 'Dec' or m == 'January' or m == 'February' or m == 'March' or m == 'April' or m == 'May' or m == 'June' or m == 'July' or m == 'August' or m == 'September' or m == 'October' or m == 'November' or m == 'December':
            month = m[0:3]
        elif m == 'All':
            month = m
        else:
            print('\nSomething went wrong. Try Again\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day == '':
        d_input = input('\nWhich day? Type "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" or "all" for no filter \n') 
        d = d_input.title()
        if d == 'Monday':
            day = 0
        elif d == 'Tuesday':  
            day = 1
        elif d == 'Wednesday':
            day = 2
        elif d == 'Thursday':
            day = 3
        elif d == 'Friday':
            day = 4
        elif d == 'Saturday':
            day = 5
        elif d == 'Sunday':
            day = 6
        elif d == 'All':
            day = d
        else:
            print('\nSomething went wrong. Try Again\n')
    print(city, month, day)
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Times columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day_of_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Start End Trip'] = df['Start Station'] + ' - ' + df['End Station']
    common_combination = df['Combination Start End Trip'].mode()[0]
    print('Most commonly used combination:', common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel time'] = df['End Time'] - df['Start Time']
    print ('Total travel time: ', df['Travel time'].sum())

    # TO DO: display mean travel time
    print ('Mean travel time: ', df['Travel time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('counts of user types: \n', user_types)

    # TO DO: Display counts of gender
    if city == 'washington':
        print('No gender data available for washington')
    else:
        gender = df['Gender'].value_counts()
        print('counts of gender: \n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('No gender data available for washington')
    else:
        print('earliest year of birth: ', df['Birth Year'].min())
        print('most recent year of birth: ', df['Birth Year'].max())
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common year of birth:', common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        #code ask to print raw data, and the printing itself
        more_data = 1
        line_count = 5
        initial_counter =1
        while more_data == 1:
            if initial_counter == 1:
                check_input = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n ')
                initial_counter = 2
            else:
                check_input = input('\nWould you like to add 5 more lines? Enter yes or no.\n ')
            check = check_input.lower()
            if check == 'yes':
                print(df.head(line_count))
                line_count += 5
            elif check == 'no':
                more_data = 0
            else: print('Something went wrong. Try Again')
        print(df.head())
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
