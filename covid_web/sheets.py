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
        try:
            cell = self.sheet.find(username)
            return cell.row
        except:
            return 0

    def next_available_row(self):
        str_list = list(filter(None, self.sheet.col_values(1)))
        return str(len(str_list) + 1)

    def next_available_col(self,row):
        str_list = list(filter(None, self.sheet.row_values(int(row))))
        return str(len(str_list) + 1)

    def create_new_user(self, username):
        if self.find_username(username) == 0:
            latestrow = self.next_available_row()
            insertrow = [username, str(datetime.datetime.now())]
            self.sheet.append_row(insertrow, table_range=f"A{latestrow}")
        else:
            print("Already have that username")

    def add_country(self, username, country):
        success = False
        row = self.find_username(username)
        if int(row) != 0:
            col = self.next_available_col(row)
            if int(col) < 8:
                self.sheet.update_cell(row, col, country)
                success = True
        return success

    def call_countries(self,username):
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
