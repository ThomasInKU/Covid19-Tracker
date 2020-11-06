import requests, json
import requests
from contextlib import closing
import csv
import time
import pandas as pd

class WorldCovidData:

    def __init__(self):
        self.world_today = self.get_data("world")
        
    def get_data(self, typee):
        world_covid_api = "https://corona.lmao.ninja/v2/all"
        response = requests.get(world_covid_api) 
        return response.json()
        
    def today_world_total_data(self, case):
        return self.world_today[case]
