from datetime import date, datetime


def get_birthdays_per_week(users):
    cur_date = date.today()
    user_dict = {}

    if not users:
        return {}

    for user in users:
        cur_year = cur_date.year

        # here we check if current date is quite close to the end of the year and if Persons bday is next year but closer than 7 days
        # then we add 1 year to the cur year to have correct comparisson
        if (cur_date - datetime(year=cur_date.year, month=12, day=31).date()).days < 6:
            if (user['birthday'].replace(year=cur_date.year + 1) - cur_date).days < 7:
                cur_year += 1

        time_delta = (user['birthday'].replace(year=cur_year) - cur_date).days

        if 7 > time_delta >= 0:
            coming_bday_day_name = user['birthday'].replace(year=cur_year).strftime('%A')
            if coming_bday_day_name in ['Saturday', 'Sunday']:
                coming_bday_day_name = 'Monday'
            user_dict[coming_bday_day_name] = user_dict.setdefault(coming_bday_day_name, []) + [user['name']]

        users = user_dict

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")