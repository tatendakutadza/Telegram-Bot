from datetime import date
from time import time, ctime
import calendar
from bs4 import BeautifulSoup
import requests


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
        :input: 'weather-forecast.com' web page with weather information on Zimbabwe.
        :return: Current weather in Zimbabwe at that time.

    """

    zim_weather = requests.get('https://www.weather-forecast.com/countries/Zimbabwe').text
    zim_weather_soup = BeautifulSoup(zim_weather, 'lxml')

    zim_current_weather = zim_weather_soup.find_all('li', class_='b-list-table__item')

    city_name = []
    city_temperature = []
    zim_current_weather_list = []

    for item in zim_current_weather:
        city_name.append(item.a.text)
        city_temperature.append(item.find('span', class_='temp').text)

    for i in range(len(city_name)):
        index_string = city_name[i] + ": " + city_temperature[i] + "°C"
        zim_current_weather_list.append(index_string)

    return '\n'.join(zim_current_weather_list)


def trending_songs_fn():
    """
        Input: Hot 100 songs from the billboard website.
        Return: The top 100 songs on the billboard in text.
    """

    billboard_hot_100_songs = requests.get('https://www.billboard.com/charts/hot-100').text
    billboard_hot_100_songs_soup = BeautifulSoup(billboard_hot_100_songs, 'lxml')
    billboard_hot_100_songs_today = billboard_hot_100_songs_soup.find_all('li',
                                                                          class_='chart-list__element display--flex')

    song_rank = []
    song_name = []
    artist_name = []
    trending_songs_list = []

    for item in billboard_hot_100_songs_today:
        song_rank.append(item.find('span', 'chart-element__rank__number').text)
        song_name.append(item.find('span', 'chart-element__information__song text--truncate color--primary').text)
        artist_name.append(item.find('span', 'chart-element__information__artist text--truncate color--secondary').text)

    size = len(artist_name)

    for index in range(size):
        song_rank_current_index = song_rank[index]
        artist_name_current_index = artist_name[index]
        song_name_current_index = song_name[index]
        index_string = song_rank_current_index + ". " + artist_name_current_index + ": " + song_name_current_index
        trending_songs_list.append(index_string)

    return '\n'.join(trending_songs_list)


def hot_albums_fn():

    """
        Input: Top 200 albums from the billboard top 200 albums chart.
        Return: The top 50 albums on the billoard chart.
    """

    billboard_top_200_albums = requests.get('https://www.billboard.com/charts/billboard-200').text
    billboard_top_200_albums_soup = BeautifulSoup(billboard_top_200_albums, 'lxml')
    hot_200_albums = billboard_top_200_albums_soup.find_all('li', class_='chart-list__element display--flex')

    album_rank = []
    album_name = []
    artist_name = []
    hot_albums = []

    for item in hot_200_albums:
        album_rank.append(item.find('span', 'chart-element__rank__number').text)
        album_name.append(item.find('span', 'chart-element__information__song text--truncate color--primary').text)
        artist_name.append(item.find('span', 'chart-element__information__artist text--truncate color--secondary').text)

    for index in range(50):
        album_rank_current_index = album_rank[index]
        artist_name_current_index = artist_name[index]
        album_name_current_index = album_name[index]
        index_string = album_rank_current_index + ". " + artist_name_current_index + ": " + album_name_current_index
        hot_albums.append(index_string)

    return '\n'.join(hot_albums)


def vacancy_mail_ict_jobs():
    """
        Input: Vacancy Mail web page with the list of jobs.
        Return: The jobs on that page.
    """

    vacancy_mail_jobs = requests.get('http://vacancymail.co.zw/categories/ict-computer-jobs-in-zimbabwe/').text
    vacancy_mail_jobs_soup = BeautifulSoup(vacancy_mail_jobs, 'lxml')
    ict_job_titles = vacancy_mail_jobs_soup.find_all('div', class_='job-list-item-title container-fluid')
    ict_job_description = vacancy_mail_jobs_soup.find_all('div', class_='col-md-12')
    ict_job_posted_by = vacancy_mail_jobs_soup.find_all('div', class_='pull-left')

    counter = 0
    job_title = []
    reconciled_job_title = []
    posting_company = []
    description = []
    ict_job_listing = []
    output_job_title = []
    output_posting_company = []

    for item in ict_job_titles:
        job_title.append(item.find('h1', 'job-title-h1').text)

    for item in ict_job_description:
        if item.find('p') is not None:
            description.append(item.find('p').text)

    for item in ict_job_posted_by:
        posting_company.append(item.find('strong').text)

    for item in job_title:
        head, sep, tail = item.partition(' \n ')
        reconciled_job_title.append(head)

    print(len(reconciled_job_title))

    for index in range(len(reconciled_job_title)):
        output_job_title_str = "\nJob:\n" + reconciled_job_title[index]
        output_posting_company_str = "Company:\n" + posting_company[index]
        output_job_title.append(output_job_title_str)
        output_posting_company.append(output_posting_company_str)

    while counter <= 9:
        ict_job_listing.append(output_job_title[counter])
        ict_job_listing.append(output_posting_company[counter])
        ict_job_listing.append('Description:')
        ict_job_listing.append(description[counter])
        counter += 1

    return '\n'.join(ict_job_listing)
