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
   
    
    cityarr = [ "chicago", "new york city", "washington"]
    montharr = [ "january", "february", "march", "april", "may", "june", "all"]
    dayarr = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    
    while True:
        try:
            cityNum = int(input("Enter number to analyze for a city: \n 1- Chicago \n 2- New York City \n 3- Washington \n"))
            city = cityarr[cityNum-1]
            break
        except ValueError:
            print("\n Invalid city!! Try Again!\n")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            monthNum = int(input("Enter number to analyze for a month: \n 1- January \n 2- February \n 3- March \n 4- April \n 5- May \n 6- June \n 7- All\n"))
            month = montharr[monthNum-1]
            break
        except ValueError:
            print("\n Invalid month!! Try Again!\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            dayNum = int(input("Enter number to analyze for a day:  \n 1- Monday \n 2- Tuesday \n 3- Wednesday \n 4- Thursday \n 5- Friday \n 6- Saturday \n 7- Sunday \n 8- All\n"))
            day = dayarr[dayNum-1]
            break
        except ValueError:
            print("\n Invalid day!! Try Again!\n")
            continue

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is : " + str(most_common_month))
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is : " + str(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour is: " + str(most_common_hour))   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("\nThe most commonly used start station is : " + str(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("\nThe most commonly used end station is : " + str(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df['Start Station'] + "-->" + df['End Station']
    combination = combine_stations.value_counts().idxmax()
    print ('The most frequent combination of start station and end station trip \n{} \n-->\n{}'.format(combination.split('-->')[0], combination.split('-->')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean travel time: " + str(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print(user_types_count)

    # TO DO: Display counts of gender
    try:
        if 'Gender' in df.columns:
            gender_count = df['Gender'].value_counts()
            print(gender_count)
        else:
            print("No gender info!!!") 
    except KeyError:
        print("No data available!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        try:
            earliest_year = df['Birth Year'].min()
            print("\nEarliest year of birth: " + str(int(earliest_year)))       
            recent_year = df['Birth Year'].max()
            print("\nMost recent year of birth: " + str(int(recent_year)))     
            common_birth_year = df['Birth Year'].mode()[0]         
            print("\nMost common year of birth: " + str(int(common_birth_year)))             
        except KeyError:
            print("\nNo data available for this month.")
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_raw_data(df):
    raw_data = input('Do you want to see raw data? Enter yes or no.\n')
    no = 0
    
    while True:
        if raw_data.lower() != 'no':    
            print(df.iloc[no : no + 5])           
            no +=5          
            raw_data = input('\nDo you want to see raw data? Enter yes or no.\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
