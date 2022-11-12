import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US Bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    city = input('Please type in the city you want to analyze; Chicago, New York City, or Washington:\n').lower()
    trials = 0  # check if more than 3 trials -> alert the user to spelling
    while city not in cities:
        print("Please enter a correct city!\n")
        trials += 1
        if trials == 3:  # Every 3 times display a hint
            print("HINT: CHECK YOUR SPELLING!")
            trials = 0
        city = input("Please type in the city you want to analyze; Chicago, New York City, or Washington:\n").lower()
    month = "all"
    day = "all"
    # get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    days = ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    cmp = input('How do you like to filter your data?\nChoose between month or day (type all for no filter):\n').lower()
    check = 0
    while check == 0:
        if cmp == "month":
            print("Please type in a month that is in the list below\n(type the word \'all\' to choose all months)\n")
            cmp = input("[JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE]\n").lower()
            while cmp not in months:
                trials += 1
                if trials == 3:  # Every 3 times display a hint
                    print("HINT: CHECK YOUR SPELLING!")
                    trials = 0
                print("Please use only one of the following months!\n(type the word \'all\' to choose all months):\n")
                cmp = input("[JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE]\n").lower()
            month = cmp
            check = 1
        elif cmp == "day":
            cmp = input(
                'Please type in the day of the week you want to filter by (type the word \'all\' to choose all days):\n').lower()
            while cmp not in days:
                trials += 1
                if trials == 3:  # Every 3 times display a hint
                    print("HINT: CHECK YOUR SPELLING!")
                    trials = 0
                cmp = input("Please enter a correct day!").lower()
            day = cmp
            check = 1
        elif cmp == "all":
            month = cmp
            day = cmp
            check = 1
        else:
            trials += 1
            if trials == 3:  # Every 3 times display a hint
                print("HINT: CHECK YOUR SPELLING!")
                trials = 0
            print("Please enter a correct filter!\n")
            cmp = input(
                'How do you like to filter your data?\nChoose between month or day (type all for no filter): ').lower()
    print('-' * 40)
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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating the most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month  # create a month column
    common_month = df['month'].mode()[
        0]  # [0] cuz mode returns a series that has index. we don't want the index displayed
    print('Most common Month:', common_month)

    # display the most common day of week
    df['day of week'] = df['Start Time'].dt.day_name()
    common_day = df['day of week'].mode()[0]
    print('Most common Day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most common stations and trip."""

    print('\nCalculating the most common Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_stats = df['Start Station'].mode()[0]
    print('Most common Start Station:', common_start_stats)

    # display most commonly used end station
    common_end_stats = df['End Station'].mode()[0]
    print('Most common End Station:', common_end_stats)

    # display most frequent combination of start station and end station trip
    comb = df.value_counts(['Start Station', 'End Station'])

    # I'm using rstrip() here to remove the number of occurrences of the combination because I think it's unnecessary
    # to_string() is used because I don't want to display the data type to the user
    print("Most common Combination of Stations: \n", comb[0:1].to_string().rstrip("0123456789"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time around the year is:\n", df['Trip Duration'].sum())

    # display mean travel time
    print("The average travel time around the year is:\n", round(df['Trip Duration'].mean(), 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    if 'Gender' in df:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("Here's the count of the different user types:\n", user_types.to_string())

        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("Here's the count of user's gender:\n", gender_counts.to_string())

        # Display earliest, most recent, and most common year of birth
        eldest = int(df['Birth Year'].min())
        young = int(df['Birth Year'].max())
        common_yob = int(df['Birth Year'].mode()[0])
        print("The most senior user was born in:\n", eldest)
        print("The youngest user was born in:\n", young)
        print("The most common year of birth among the users is:\n", common_yob)
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('Gender stats cannot be calculated because Washington\'s data doesn\'t include a gender column')
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw = input("Would you like to see some raw data?(Yes/No)\n").lower()  # by raw I mean raw data
        raw_counter = 0
        raw_check = 1
        while raw_check == 1:
            if raw in ("yes", "y"):
                raw_df = df[raw_counter: (raw_counter + 5)]
                raw_counter += 5
                print(raw_df)
                raw = input("Would you like to see some raw data again?(Yes/No)\n").lower()
            elif raw in ("no", "n"):
                raw_check = 0
            else:
                print("Please enter a correct input!")
                raw = input("Would you like to see some raw data?(Yes/No)\n").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart in ("yes", "y"):
            main()
        elif restart in ("no", "n"):
            break
        else:
            print("Please enter a correct input!")
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()


if __name__ == "__main__":
    main()
