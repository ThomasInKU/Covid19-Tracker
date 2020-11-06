import requests, json
import requests
from contextlib import closing
import csv
import time
import pandas as pd

class CovidData:
    
    def __init__(self):
        self.world_today = self.get_data()
        self.url = ""
        
    def get_url(self, type):
        if type == "world":
            return "https://corona.lmao.ninja/v2/all"
        
    def get_data(self, type):
        if type == "world":
            url = get_url("world")
        response = requests.get(url) 
        return response.json()
        
    def today_world_total_data(self, case):
        return self.world_today[case]

 
