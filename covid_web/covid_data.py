import requests, json
import requests
from contextlib import closing
import csv
import time
import pandas as pd

class CountryCovidData:
    
    country = {"Zimbabwe": 0, "Zambia": 1, 
                "Yemen": 2, 
                "Western Sahara": 3, 
                "Wallis and Futuna": 4, 
                "Vietnam": 5, 
                "Venezuela": 6, 
                "Uzbekistan": 7, 
                "Uruguay": 8, 
                "Ukraine": 9, 
                "Uganda": 10, 
                "USA": 11, 
                "UK": 12, 
                "UAE": 13, 
                "Turks and Caicos Islands": 14, 
                "Turkey": 15, 
                "Tunisia": 16, 
                "Trinidad and Tobago": 17, 
                "Togo": 18, 
                "Timor-Leste": 19, 
                "Thailand": 20, 
                "Tanzania": 21, 
                "Tajikistan": 22, 
                "Taiwan": 23, 
                "Syrian Arab Republic": 24, 
                "Switzerland": 25, 
                "Sweden": 26, 
                "Swaziland": 27, 
                "Suriname": 28, 
                "Sudan": 29, 
                "St. Barth": 30, 
                "Sri Lanka": 31, 
                "Spain": 32, 
                "South Sudan": 33, 
                "South Africa": 34, 
                "Somalia": 35, 
                "Solomon Islands": 36, 
                "Slovenia": 37, 
                "Slovakia": 38, 
                "Sint Maarten": 39, 
                "Singapore": 40, 
                "Sierra Leone": 41, 
                "Seychelles": 42, 
                "Serbia": 43, 
                "Senegal": 44, 
                "Saudi Arabia": 45, 
                "Sao Tome and Principe": 46, 
                "San Marino": 47, 
                "Saint Vincent and the Grenadines": 48, 
                "Saint Pierre Miquelon": 49, 
                "Saint Martin": 50, 
                "Saint Lucia": 51, 
                "Saint Kitts and Nevis": 52, 
                "S. Korea": 53, 
                "Réunion": 54, 
                "Rwanda": 55, 
                "Russia": 56, 
                "Romania": 57, 
                "Qatar": 58, 
                "Portugal": 59, 
                "Poland": 60, 
                "Philippines": 61, 
                "Peru": 62, 
                "Paraguay": 63, 
                "Papua New Guinea": 64, 
                "Panama": 65, 
                "Palestine": 66, 
                "Pakistan": 67, 
                "Oman": 68, 
                "Norway": 69, 
                "Nigeria": 70, 
                "Niger": 71, 
                "Nicaragua": 72, 
                "New Zealand": 73, 
                "New Caledonia": 74, 
                "Netherlands": 75, 
                "Nepal": 76, 
                "Namibia": 77, 
                "Myanmar": 78, 
                "Mozambique": 79, 
                "Morocco": 80, 
                "Montserrat": 81, 
                "Montenegro": 82, 
                "Mongolia": 83, 
                "Monaco": 84, 
                "Moldova": 85, 
                "Mexico": 86, 
                "Mayotte": 87, 
                "Mauritius": 88, 
                "Mauritania": 89, 
                "Martinique": 90, 
                "Marshall Islands": 91, 
                "Malta": 92, 
                "Mali": 93, 
                "Maldives": 94, 
                "Malaysia": 95, 
                "Malawi": 96, 
                "Madagascar": 97, 
                "Macedonia": 98, 
                "Macao": 99, 
                "MS Zaandam": 100, 
                "Luxembourg": 101, 
                "Lithuania": 102, 
                "Liechtenstein": 103, 
                "Libyan Arab Jamahiriya": 104, 
                "Liberia": 105, 
                "Lesotho": 106, 
                "Lebanon": 107, 
                "Latvia": 108, 
                "Lao People's Democratic Republic": 109, 
                "Kyrgyzstan": 110, 
                "Kuwait": 111, 
                "Kenya": 112, 
                "Kazakhstan": 113, 
                "Jordan": 114, 
                "Japan": 115, 
                "Jamaica": 116, 
                "Italy": 117, 
                "Israel": 118, 
                "Isle of Man": 119, 
                "Ireland": 120, 
                "Iraq": 121, 
                "Iran": 122, 
                "Indonesia": 123, 
                "India": 124, 
                "Iceland": 125, 
                "Hungary": 126, 
                "Hong Kong": 127, 
                "Honduras": 128, 
                "Holy See (Vatican City State)": 129, 
                "Haiti": 130, 
                "Guyana": 131, 
                "Guinea-Bissau": 132, 
                "Guinea": 133, 
                "Guatemala": 134, 
                "Guadeloupe": 135, 
                "Grenada": 136, 
                "Greenland": 137, 
                "Greece": 138, 
                "Gibraltar": 139, 
                "Ghana": 140, 
                "Germany": 141, 
                "Georgia": 142, 
                "Gambia": 143, 
                "Gabon": 144, 
                "French Polynesia": 145, 
                "French Guiana": 146, 
                "France": 147, 
                "Finland": 148, 
                "Fiji": 149, 
                "Faroe Islands": 150, 
                "Falkland Islands (Malvinas)": 151, 
                "Ethiopia": 152, 
                "Estonia": 153, "Eritrea": 154, 
                "Equatorial Guinea": 155, 
                "El Salvador": 156, 
                "Egypt": 157, 
                "Ecuador": 158, 
                "Dominican Republic": 159, 
                "Dominica": 160, 
                "Djibouti": 161, 
                "Diamond Princess": 162, 
                "Denmark": 163, 
                "DRC": 164, 
                "Côte d'Ivoire": 165, 
                "Czechia": 166, 
                "Cyprus": 167, 
                "Curaçao": 168, 
                "Cuba": 169, 
                "Croatia": 170, 
                "Costa Rica": 171, 
                "Congo": 172, 
                "Comoros": 173, 
                "Colombia": 174, 
                "China": 175, 
                "Chile": 176, 
                "Channel Islands": 177, 
                "Chad": 178, 
                "Central African Republic": 179, 
                "Cayman Islands": 180, 
                "Caribbean Netherlands": 181, 
                "Canada": 182, 
                "Cameroon": 183, 
                "Cambodia": 184, 
                "Cabo Verde": 185, 
                "Burundi": 186, 
                "Burkina Faso": 187, 
                "Bulgaria": 188, 
                "Brunei": 189, 
                "British Virgin Islands": 190, 
                "Brazil": 191, 
                "Botswana": 192, 
                "Bosnia": 193, 
                "Bolivia": 194, 
                "Bhutan": 195, 
                "Bermuda": 196, "Benin": 197, 
                "Belize": 198, 
                "Belgium": 199, 
                "Belarus": 200, 
                "Barbados": 201, 
                "Bangladesh": 202, 
                "Bahrain": 203, 
                "Bahamas": 204, 
                "Azerbaijan": 205, 
                "Austria": 206, 
                "Australia": 207, 
                "Aruba": 208, 
                "Armenia": 209, 
                "Argentina": 210, 
                "Antigua and Barbuda": 211, 
                "Anguilla": 212, 
                "Angola": 213, 
                "Andorra": 214, 
                "Algeria": 215, 
                "Albania": 216, 
                "Afghanistan": 217 }

    def __init__(self):
        self.data = self.get_data()
    
    def get_result(self, case, country):
        if(self.country_name_isvalid(country)):
            country_code = self.find_country_code(country)
            return self.data[country_code][case]
        else:
            return "Please select your country"
        
    def get_data(self):
        country_covid_api = "https://corona.lmao.ninja/v2/countries?sort=country"
        return requests.get(country_covid_api).json()

    def find_country_code(self, country_name):
        return self.country[country_name]
    
    def country_name_isvalid(self, country_name):
        name_is_valid = country_name in self.country.keys()
        return name_is_valid
    
    def get_country_dic(self, country):
        code = self.find_country_code(country)
        return self.data[code]
    
    def print_dic(self, country):
        dic = self.get_country_dic(country)
        for pair in dic.items():
            print(pair)


class WorldCovidData:
    
    def __init__(self):
        self.world_today = self.get_data("world")
        
    def get_data(self, typee):
        world_covid_api = "https://corona.lmao.ninja/v2/all"
        response = requests.get(world_covid_api) 
        return response.json()
        
    def get_result(self, case):
        return self.world_today[case]

# cd = CountryCovidData()
# print(cd.get_result("cases", "Thailand"))