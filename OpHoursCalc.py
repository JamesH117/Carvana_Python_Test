# By James Hauser II
# Also uploaded to github account: https://github.com/JamesH117


# work_hours format example:[datetime.time, datetime.time]
# work_days format example: ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
# loading_time example (in minutes): 180
# departue_time datetime.datetime object example: 2018-08-13 10:00
# same_day_load_optional: True/False

import datetime
import calendar


valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def input(work_hours, work_days, loading_time, departure_datetime, same_day_load_mandatory):

    # Validate input parameters
    check_work_hours(work_hours)
    check_work_days(work_days)
    check_loading_time(loading_time)
    check_departure_datetime(departure_datetime)
    check_same_day_load_mandatory(same_day_load_mandatory)

    departure_day_num = departure_datetime.weekday()
    departure_day_name = calendar.day_name[departure_day_num]
    departure_time = departure_datetime.time()

    time_spent_loading = loading_time
    multi_day_start = departure_datetime

    start_load_datetime = None
    # Don't need to go back more than 6 days
    for i in range(0, 7):
        if start_load_datetime != None:
            break

        current_date = (departure_datetime.date() - datetime.timedelta(days=i))
        current_day = calendar.day_name[current_date.weekday()].lower()

        if current_day in work_days:
            if same_day_load_mandatory:

                start_time = None

                # Departure time is before work hours of last day, can't load today
                if i == 0 and departure_time <= work_hours[0]:
                    continue

                # Same day as departure_day # If departure is during work hours, see if we can start loading that day
                elif i == 0 and departure_time <= work_hours[1]:
                    start_time = (departure_datetime - datetime.timedelta(minutes=loading_time)).time()

                # Any full workday before departure_datetime
                else:
                    start_time = (datetime.datetime.combine(current_date, work_hours[1]) - datetime.timedelta(minutes=loading_time)).time()

                if start_time != None and start_time >= work_hours[0]:
                    start_load_datetime = datetime.datetime.combine(current_date, start_time)

            # We can load across multiple days
            else:
                # We are done loading, set correct start time for loading
                if time_spent_loading == 0:
                    start_load_datetime = multi_day_start
                else:
                    # If we are on a day that is not departure date, move our start time to end of work day hours
                    if i > 0:
                        multi_day_start = datetime.datetime.combine(current_date, work_hours[1])
                    # If we are on departure date on last work day, make sure our start time is end of day if departure outside work hours
                    elif i == 0 and multi_day_start.time() >= work_hours[1]:
                        multi_day_start = datetime.datetime.combine(current_date, work_hours[1])
                    # Departure is before work hours on last day, can't load today
                    elif i == 0 and multi_day_start.time() <= work_hours[0]:
                        continue


                    time_left = (multi_day_start - datetime.datetime.combine(current_date, work_hours[0])).total_seconds() / 60

                    if time_left <= time_spent_loading:
                        time_spent_loading -= time_left
                        multi_day_start -= datetime.timedelta(minutes=time_left)
                    else:
                        multi_day_start -= datetime.timedelta(minutes=time_spent_loading)
                        time_spent_loading = 0;

    if start_load_datetime != None:
        return start_load_datetime.strftime("%Y-%m-%d %H:%M")
    return start_load_datetime


def check_work_hours(work_hours):
    if not isinstance(work_hours, list):
        raise TypeError("Work hours needs to be a list.")
    if not (len(work_hours) == 2):
        raise Exception("Work hours needs to be a list of size 2.")
    if type(work_hours[0]) is not datetime.time or type(work_hours[1]) is not datetime.time:
        raise Exception("Work hours inside list need to be 'datetime.time' objects.")
    return 1

def check_work_days(work_days):
    if not isinstance(work_days, list):
        raise TypeError("Work days needs to be a list.")
    if (len(work_days) > 7):
        raise Exception("Input is greater than maximum possible work days of 7")
    for day in work_days:
        if not isinstance(day, str):
            raise TypeError("Work days need to be strings")
        if day.lower() not in valid_days:
            raise Exception("All days need to be fully spelt out and correct; Invalid day found: [" +day+ "]")

def check_loading_time(loading_time):
    if not isinstance(loading_time, int):
        raise TypeError("loading time needs to be an integer of minutes.")
    if loading_time == 0:
        raise Exception("Loading time can not be 0.")
    if loading_time < 0:
        raise Exception("Loading time can not be less than 0.")

def check_departure_datetime(departure_datetime):
    if type(departure_datetime) is not datetime.datetime:
        raise TypeError("departure datetime needs to be a 'datetime.datetime' object.")

def check_same_day_load_mandatory(same_day_load_mandatory):
    if type(same_day_load_mandatory) is not bool:
        raise TypeError("Same day load mandatory needs to be a 'bool' object.")



def test_1():
    work_hours = [datetime.time(8, 00), datetime.time(14, 00)]
    work_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    loading_time = 180
    departure_time = datetime.datetime(2018, 8, 15, 14, 0)
    same_day_load = False
    return input(work_hours, work_days, loading_time, departure_time, same_day_load)

def test_2():
    work_hours = [datetime.time(8, 00), datetime.time(14, 00)]
    work_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    loading_time = 180
    departure_time = datetime.datetime(2018, 8, 15, 14, 0)
    same_day_load = True
    return input(work_hours, work_days, loading_time, departure_time, same_day_load)

def test_3():
    work_hours = [datetime.time(12, 00), datetime.time(18, 00)]
    work_days = ["monday", "wednesday", "friday"]
    loading_time = 180
    departure_time = datetime.datetime(2018, 8, 15, 10, 0)
    same_day_load = False
    return input(work_hours, work_days, loading_time, departure_time, same_day_load)

def test_4():
    work_hours = [datetime.time(8, 00), datetime.time(14, 00)]
    work_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    loading_time = 210
    departure_time = datetime.datetime(2018, 8, 14, 10, 0)
    same_day_load = False
    return input(work_hours, work_days, loading_time, departure_time, same_day_load)

def test_5():
    work_hours = [datetime.time(8, 00), datetime.time(14, 00)]
    work_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    loading_time = 210
    departure_time = datetime.datetime(2018, 8, 14, 10, 0)
    same_day_load = True
    return input(work_hours, work_days, loading_time, departure_time, same_day_load)

print(test_1())
print(test_2())
print(test_3())
print(test_4())
print(test_5())
