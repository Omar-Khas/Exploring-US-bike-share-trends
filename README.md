# Exploring-US-bike-share-trends
In this project, I'll utilize Python to investigate data from bike sharing services in three major US cities: Chicago, New York City, and Washington. In this project, I used Pandas library to import US bike sharing data and create descriptive statistics to address interesting questions that can highlight some trends. I have built a script that accepts raw information and generates an interactive terminal experience to display these statistics.

The CSV files included in the repository are provided by [Motivate](https://www.motivateco.com/). The original data is larger but if you need them they're available in the following links:
- [Chicago's Data](https://ride.divvybikes.com/system-data)
- [New York's Data](https://ride.citibikenyc.com/system-data)
- [Washington's Data](https://ride.capitalbikeshare.com/system-data)

## The Dataset[^1]

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

### Statistics Computed
1. Popular times of travel (i.e., occurs most often in the start time)
    - most common month
    - most common day of week
    - most common hour of day
2. Popular stations and trip
    - most common start station
    - most common end station
    - most common trip from start to end (i.e., most frequent combination of start station and end station)
3. Trip duration
    - total travel time
    - average travel time
4. User info
    - counts of each user type
    - counts of each gender (only available for NYC and Chicago)
    - earliest, most recent, most common year of birth (only available for NYC and Chicago)
  
[^1]: This excerpt is from Udacity's Data Analysis Nanodegree
