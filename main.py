from datetime import date, datetime


def get_birthdays_per_week(users):

    from_date = datetime(2023, 12, 26)
    if from_date.month < 12:
        month_days = (date(year=from_date.year, month=from_date.month+1, day=from_date.day) - date(year=from_date.year, month=from_date.month, day=from_date.day)).days
    elif from_date.month == 12:
        month_days = (date(year=from_date.year, month=from_date.month-1, day=from_date.day) - date(year=from_date.year, month=from_date.month-2, day=from_date.day)).days

    if (from_date.day + 7) < int(month_days):
        till_date = datetime(year=from_date.year, month=from_date.month, day=from_date.day+7).date()
    elif (from_date.day + 7) == int(month_days):
        till_date = datetime(year=from_date.year, month=from_date.month, day=month_days).date()
    elif (from_date.day + 7) > int(month_days) and from_date.month == 12:
        till_date = datetime(from_date.year+1, month=1, day=from_date.day+7 - month_days).date()
    elif (from_date.day + 7) > int(month_days):
        till_date = datetime(year=from_date.year, month=from_date.month+1, day=from_date.day+7 - month_days).date()

    my_dict = {}

    for user_dict in users:
        user_names = user_dict['name'].split()
        dict_value_names = user_names[0]
        birthdays = user_dict['birthday']
        birthdays = datetime(year=from_date.year, month=birthdays.month, day=birthdays.day).date()
        dict_key_weekday = birthdays.strftime('%A')

        range_of_days_next_month = [i for i in range(1, till_date.day)]

        if birthdays.month == from_date.month and birthdays.day >= from_date.day or birthdays.month == from_date.month+1 and birthdays.day in range_of_days_next_month:
            if dict_key_weekday == 'Sunday' or dict_key_weekday == 'Saturday':
                dict_key_weekday = 'Monday'
            if dict_key_weekday not in my_dict:
                my_dict[dict_key_weekday] = []
            my_dict[dict_key_weekday].append(dict_value_names)
        elif birthdays.month != from_date.month:
            if dict_key_weekday == 'Sunday' or dict_key_weekday == 'Saturday':
                dict_key_weekday = 'Monday'
            if dict_key_weekday not in my_dict:
                my_dict[dict_key_weekday] = []
            my_dict[dict_key_weekday].append(dict_value_names)
    return my_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
