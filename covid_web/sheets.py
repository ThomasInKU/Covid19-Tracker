import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Covid-19 Tracker Users").sheet1
    data = sheet.get_all_records()

    def find_username(self, username):
        cell = self.sheet.find(username)
        return cell.row

    def create_new_user(self, username):
        latestrow = self.sheet.row_count
        insertrow = [username, datetime.datetime.now()]
        self.sheet.append_row(insertrow, table_range=f"A{latestrow}")

    def add_country(self, username, country):
        success = False
        row = self.find_username(username)
        for i in range(0, 5):
            if self.sheet.cell(row, i).value == "":
                self.sheet.update_cell(row, i, country)
                success = True
        return success

    def call_countries(self,username):
        countries = []
        row = self.find_username(username)
        for i in range(0, 5):
            if self.sheet.cell(row, i).value == "":
                countries.append(self.sheet.cell(row, i).value)
        return countries
