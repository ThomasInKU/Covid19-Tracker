import requests
from contextlib import closing
import csv

class CovidData:
    
    def select_url(self, data_type):
        if data_type == "totalconfirm":
            return "https://covid.ourworldindata.org/data/ecdc/total_cases.csv"
        elif data_type == "totaldeaths":
            return "https://covid.ourworldindata.org/data/ecdc/total_deaths.csv"
        elif data_type == "newconfirm":
            return "https://covid.ourworldindata.org/data/ecdc/new_cases.csv"
        elif data_type == "newdeaths":
            return "https://covid.ourworldindata.org/data/ecdc/new_deaths.csv"
        

    def today_data(self, country, data_type):
        arr = []
        with closing(requests.get(self.select_url(data_type), stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                arr.append(row)
            for i in range(len(arr[0])):
                if arr[0][i] == country:
                    country_index = i
            return arr[len(arr)-1][country_index]
    