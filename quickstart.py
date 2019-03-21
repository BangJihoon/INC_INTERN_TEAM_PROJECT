import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# api로 접속
api = 'gspread.json'
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(api,scope)

gc = gspread.authorize(credentials)

# 스프레드시트 열기
wks = gc.open("TEST")
# wks = gc.open_by_key('1koTY_kuvDVdoRF3u6Vs53OwRJhLvI-F_oPTjabdKjBY')
# wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1koTY_kuvDVdoRF3u6Vs53OwRJhLvI-F_oPTjabdKjBY/edit#gid=0")

# 워크시트열기
wk0 = wks.get_worksheet(0)
#wk0 = wks.worksheet('시트1')
#wk0 = wks.sheet1
#worksheet_list = wks.worksheets()

# 워크시트에 기록하기
wk0.update_cell(1, 1, "asdasd")
