import requests
from contextlib import closing
import csv

class CovidData:
    
    total_confirmed_cases_url = "https://covid.ourworldindata.org/data/ecdc/total_cases.csv"
    total_deaths_url = "https://covid.ourworldindata.org/data/ecdc/total_deaths.csv"
    new_confirmed_case_url = "https://covid.ourworldindata.org/data/ecdc/new_cases.csv"
    new_deaths_url = "https://covid.ourworldindata.org/data/ecdc/new_deaths.csv"

    def today_data(self, country, data_type):
        arr = []
        with closing(requests.get(data_type, stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                arr.append(row)
            for i in range(len(arr[0])):
                if arr[0][i] == country:
                    country_index = i
            return arr[len(arr)-1][country_index]