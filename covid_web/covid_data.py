import requests, json
import requests
from contextlib import closing
import csv
import time
import pandas as pd

class CovidData:
    
    def __init__(self):
        self.today = self.get_data()
        
    def get_data(self):
        url = "https://corona.lmao.ninja/v2/all"
        response = requests.get(url) 
        return response.json()
        
    def today_total_data(self, case):
        return self.today[case]

url = "https://corona.lmao.ninja/v2/all"
response = requests.get(url) 
print(response.json())