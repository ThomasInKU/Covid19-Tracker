import requests
from contextlib import closing
import csv
import time

class CovidData:
    
    def __init__(self):
        self.current_country = ""
        self.total_case = self.get_data("totalconfirm")
        self.total_deaths = self.get_data("totaldeaths")
        self.new_case = self.get_data("newconfirm")
        self.new_deaths = self.get_data("newdeaths")
    
    def select_url(self, data_type):
        if data_type == "totalconfirm":
            return "https://covid.ourworldindata.org/data/ecdc/total_cases.csv"
        elif data_type == "totaldeaths":
            return "https://covid.ourworldindata.org/data/ecdc/total_deaths.csv"
        elif data_type == "newconfirm":
            return "https://covid.ourworldindata.org/data/ecdc/new_cases.csv"
        elif data_type == "newdeaths":
            return "https://covid.ourworldindata.org/data/ecdc/new_deaths.csv"
        
    def get_data(self, data_type):
        arr = []
        with closing(requests.get(self.select_url(data_type), stream=True)) as r:
            f = (line.decode('utf-8') for line in r.iter_lines())
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                arr.append(row)
        return arr
    
    def today_total_confirm_data(self, country, data_type):
        print(f'len = {len(self.total_case[0])}')
        for i in range(len(self.total_case[0])):
            if self.total_case[0][i] == country:
                country_index = i
        return self.total_case[len(self.total_case)-1][country_index]
    

# gd = CovidData()
# start = time.time()
# print(gd.today_total_confirm_data("World","totalconfirm"))
# stop = time.time()
# print(f'time1 = {stop-start}')
# start = time.time()
# print(gd.today_total_confirm_data("World","totalconfirm"))
# stop = time.time()
# print(f'time2 = {stop-start}')