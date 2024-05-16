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
    print('Hi!\nLet\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    day = 0 
    month = 0
    
    user_input_for_city = input("Please choose a city from ( chicago, new york city, washington) to display it's data...\n----= ").lower()
    while True:
        if user_input_for_city not in CITY_DATA:
            user_input_for_city = input("Sorry wrong Value!!! Please choose correct city...\n---= ").lower()

        else:
            break



    # get user input for month (all, january, february, ... , june)
    filteration = input("do you want to fiter by month or day or both?\n---= ").lower()
    while True:
        if filteration == "month":
                            
            month = input("Please choose a month from ( january,february,...., june) to display it's data or choose 'all' to display all months data...\n----= ").lower()
            valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
            while True:
                if month not in valid_months and month != "all":
                    month = input("Sorry wrong Value!!! Please choose correct month...\n---= ").lower()
    
                else:
                    break
            break
        elif filteration == "day":
            day = input("Please choose a day from ( saturday,sunday,...., friday) to display it's data or choose 'all' to display all days data...\n----= ").lower()
            valid_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday','thursday','friday']
            while True:
                if day not in valid_days and day != "all":
                    day = input("Sorry wrong Value!!! Please choose correct day...\n---= ").lower()
                else:
                    break
            break
        elif filteration =="both":
            month = input("Please choose a month from ( january,february,...., june) to display it's data or choose 'all' to display all months data...\n----= ").lower()
            valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
            while True:
                if month not in valid_months and month != "all":
                    month = input("Sorry wrong Value!!! Please choose correct month...\n---= ").lower()
    
                else:
                    break 
                
            day = input("Please choose a day from ( saturday,sunday,...., friday) to display it's data or choose 'all' to display all days data...\n----= ").lower()
            valid_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday','thursday','friday']
            while True:
                if day not in valid_days and day != "all":
                    day = input("Sorry wrong Value!!! Please choose correct day...\n---= ").lower()
                else:
                    break
            break
        else:
            filteration = input("Sorry wrong Value!!! Please choose correct filteration...\n---= ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)

    print('_'*40)
    
    return user_input_for_city, month, day


def data_load(user_input_for_city, month, user_input_for_day_of_week):
    """ye
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load the file of data in a dataframe
    df = pd.read_csv(CITY_DATA[user_input_for_city])

    #turn starttime column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #extract month and day of week from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #filter the months if valid
    
    if month != 0:
        if month != 'all':
            # using the index of months lists to show the required int
            valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
            user_input_for_month = valid_months.index(month) + 1
    
            # filter by month to create new dataframe
           ch df = df[df['month'] == user_input_for_month]

    #filter the day of week if valid
    if user_input_for_day_of_week != 0:
        if user_input_for_day_of_week != 'all':
            # filter by month to create new dataframe
            df = df[df['day_of_week'] == user_input_for_day_of_week.title()]
    return df

def time_statistics(df):
    """displays the most frequent times of travel"""
    print('\ncalculating the most frequent times of travel...\n')
    start_time = time.time()

    #display the most common month
    most_common_month = df['month'].mode()[0]
    print('The Most Common Month:', most_common_month)

    #display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The Most Common day:', most_common_day)

    #display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The Most Common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display the most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The Most Commonly Used Start Station:', most_common_start_station)


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The Most Commonly Used End Station:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = (df['Start Station']+'-'+df['End Station']).mode()[0]
    print('The Most frequent combination of start station and end station:', most_common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_statistics(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time:', total_travel_time, 'seconds' )

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time:', mean_travel_time, 'seconds' )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_statistics(df,user_input_for_city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('counts of user types:', counts_of_user_types)


    # Display counts of gender
    if user_input_for_city != 'washington':
        Gender_statistics = df['Gender'].value_counts()
        print(' Gender statistics:',  Gender_statistics)

    # Display most common year of birth
        the_most_common_birth_year = df['Birth Year'].mode()[0]
        print(' The Most Common Birth Year:', the_most_common_birth_year)

    # Display most recent year of birth
        the_most_recent_birth_year = df['Birth Year'].max()
        print(' The Most Recent Birth Year:', the_most_recent_birth_year)

    # Display the earliest year of birth
        the_earliest_birth_year = df['Birth Year'].min()
        print(' The Earliest Birth Year:', the_earliest_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def users_data_information(df):
    #Displaying 5 rows of data....
    
    answer = input('\nWould you like to see some raw data?\n---= ')
    while True:
        if answer.lower() == 'yes':
            row_number = 0
            while True:
                print(df.iloc[row_number: row_number+5])
                row_number += 5
                ask = input('need to see more 5 raws?\n---= ')
                if ask.lower() != 'yes':
                    break
            break
        elif answer.lower() == "no":
            break
        
        else:
            answer = input('\nPlease enter correct answer...?\n--= ')

def main():
    while True:
        user_input_for_city, user_input_for_month, user_input_for_day_of_week = get_filters()
        df = data_load(user_input_for_city, user_input_for_month, user_input_for_day_of_week)

        time_statistics(df)
        station_statistics(df)
        trip_duration_statistics(df)
        user_statistics(df,user_input_for_city)
        users_data_information(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

