from datetime import date
from time import time, ctime
import calendar


def date_fn():
    """
       :input: no input


       :return: Today's date
    """

    today = date.today()
    str_today = str(today)
    today_day_of_the_week = calendar.day_name[today.weekday()]
    today_day = str_today[8:10]
    today_month = str_today[5:7]
    int_today_month = int(today_month)
    today_month_name = calendar.month_name[int_today_month]
    today_year = str_today[0:4]
    current_date = today_day_of_the_week + " " + today_day + " " + today_month_name + " " + today_year
    return current_date


def time_fn():
    """
        :input: no input
        :return: The current time in 24hr notation
    """
    t = time()
    date_time = ctime(t)
    str_date_time = str(date_time)
    today_time = str_date_time[11:16]
    current_time = today_time + "hrs"
    return current_time


def weather_fn():
    """
        :input:

        :return: The weather for the specified location for the current week
    """