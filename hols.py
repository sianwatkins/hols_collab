sian

import pandas as pd
import os


def format_table(hotel):
    # formats date and renames months into date format, makes new column
    dictionary = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05',
                  'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11',
                  'December': '12'}
    hotel['arrival_date_month'] = hotel['arrival_date_month'].apply(lambda x: dictionary[x])
    hotel["date"] = hotel["arrival_date_year"].astype(str) + "-" + \
                    hotel["arrival_date_month"].astype(str) + "-" + hotel["arrival_date_day_of_month"].astype(str)
    hotel['date'] = pd.to_datetime(hotel['date'], format='%Y-%m-%d')

    return hotel


def delete_cancelled(hotel):
    # function to delete cancelled bookings
    indexnames = hotel[hotel['is_canceled'] == 1].index
    new_hotel = hotel.drop(indexnames)
    print(new_hotel)
    return new_hotel


def user_interface():
    # user inputs the date they want to search
    year = input("Year of booking (YYYY): ")
    if year.isdigit():
        result = int(year)
    else:
        print("Invalid, try again")
        user_interface()
        return year
    month = input("Month of booking (MM): ")
    if month.isdigit():
        result2 = int(month)
    else:
        print("Invalid, try again")
        user_interface()
        return month
    day = input("Day of booking (DD): ")
    if day.isdigit():
        result3 = int(day)
    else:
        print("Invalid, try again")
        user_interface()
        return day
    import datetime
    user_date = datetime.datetime(result, result2, result3)
    print(user_date.strftime('%Y-%m-%d'))
    return user_date


def select_7days(user_date, new_hotel):
    date_from = pd.Timestamp(user_date)
    date_to = pd.Timedelta(days=7)
    print("Selecting dates {date_to} greater than {date_from}")
    hotel2 = pd.DataFrame(new_hotel[
                              (new_hotel['date'] > date_from) &
                              (new_hotel['date'] < date_from + date_to)
                              ])
    print(hotel2)
    os.mkdir('booking_folder')
    hotel2.to_csv('booking_folder\past7days.csv', index=False)
    return hotel2


def group(user_date):
    adults = hotel2.groupby(['date', 'adults']).count()
    adults.rename(columns={'hotel': 'freq_of_adults_on_date'}, inplace=True)
    adults = adults.loc[:, adults.columns.intersection(['freq_of_adults'])]
    adults.reset_index(inplace=True)

    babies = hotel2.groupby(['babies', 'date']).count()
    babies.rename(columns={'hotel': 'freq_of_babies_on_date'}, inplace=True)
    babies = babies.loc[:, babies.columns.intersection(['freq_of_babies'])]
    babies.reset_index(inplace=True)

    children = hotel2.groupby(['children', 'date']).count()
    children.rename(columns={'hotel': 'freq_of_children_on_date'}, inplace=True)
    children = children.loc[:, children.columns.intersection(['freq_of_children'])]
    children.reset_index(inplace=True)

    new = adults.merge(babies, on='date').merge(children, on='date')
    print(new)
    new.to_csv('booking_folder\\booking_demographic.csv', index=False)
    return new


hotel = pd.read_csv('C:\\Users\\siane\\OneDrive\\Documents\\DRS Internship\\hotel_bookings.csv')

hotel = format_table(hotel)
new_hotel = delete_cancelled(hotel)
user_date = user_interface()
hotel2 = select_7days(user_date, new_hotel)
new = group(user_date)
