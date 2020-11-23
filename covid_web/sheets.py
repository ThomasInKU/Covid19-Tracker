import gspread
import datetime

from django import template
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:

    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                      "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Covid-19 Tracker Users").sheet1
        self.data = self.sheet.get_all_records()

    def find_username(self, username):
        try:
            cell = self.sheet.find(username)
            return cell.row
        except:
            return 0

    def next_available_row(self):
        str_list = list(filter(None, self.sheet.col_values(1)))
        return str(len(str_list) + 1)

    def next_available_col(self, row):
        str_list = list(filter(None, self.sheet.row_values(int(row))))
        return str(len(str_list) + 1)

    def create_new_user(self, username):
        if self.find_username(username) == 0:
            latestrow = self.next_available_row()
            insertrow = [username, str(datetime.datetime.now())]
            self.sheet.append_row(insertrow, table_range=f"A{latestrow}")
            return "Success!"
        else:
            return "Already have that username"

    def add_country(self, username, country):
        status = False
        row = self.find_username(username)
        if int(row) == 0:
            row = self.next_available_row()
            self.create_new_user(username)
        if self.sheet.row_values(row).__contains__(country): 
            return status
        col = self.next_available_col(row)
        if int(col) < 8:
            self.sheet.update_cell(row, col, country)
            success = True
        return status

    def call_countries(self, username):
        countries = []
        row = self.find_username(username)
        if int(row) != 0:
            for i in range(3, 8):
                if self.sheet.cell(row, i).value == "":
                    countries.append(self.sheet.cell(row, i).value)
        return countries

# database = Sheet()
# database.create_new_user("urn")
# database.find_username("Thee")
# database.add_country("urn","England")
