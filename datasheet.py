import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list) + 1)


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
my_list = [['1', '2', '3', '4', '5', '6', '7', '8']]
sheet = client.open("PowersenseDatabase")
worksheet = sheet.worksheet("Test")
next_row = next_available_row(worksheet)
worksheet_page = worksheet.get_all_values()

# print('Input:')
# num_row = input()
# st_num_row = str(num_row)
# rows = 'A' + st_num_row
#
# print(rows)

worksheet.update("A{}".format(next_row), my_list)
worksheet_df = pd.DataFrame(worksheet_page)
print(worksheet_df)
# print(worksheet.get_all_values())
