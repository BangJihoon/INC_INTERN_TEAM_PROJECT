# json 으로 잡아서 시트에 저장
# 크롤링 및 구글스프레드시트 연동
from selenium import webdriver
import gspread , requests, json,pprint
from oauth2client.service_account import ServiceAccountCredentials
import pandas,time
from selenium.webdriver.common.keys import Keys

# 구글 시트 연동 (api로 들어가서 시트열기)
api = 'gspread.json'
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(api,scope)
gc = gspread.authorize(credentials)
wks = gc.open("TEST")

# 크롬 드라이버로 채팅방 열기
driver = webdriver.Chrome('C:/chromedriver')
driver.implicitly_wait(3)
driver.get('https://center-pf.kakao.com/_EvRij/chats')
driver.find_element_by_id('loginEmail').send_keys('skuinc.internship@skuniv.ac.kr')     # 아이디
driver.find_element_by_id('loginPw').send_keys('!@#$intern12')                          # 비번
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/button').click()

# 채팅방 들어가기
chat_list = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div').find_elements_by_tag_name('li')
main_window = driver.window_handles[0]  # 부모창

x = 0    # 워크시트 번호
worksheet_list = wks.worksheets()       # 워크시트 가져오기

for chat_room in chat_list:
    chat_room.click()
    driver.switch_to_window(driver.window_handles[1])

# 데이터 출력 및 넣기
    # 워크시트 열기 & 만들기
    wk0 = wks.get_worksheet(x)  # 워크시트 순차적으로 열기

    wk0.update_cell(1, 1, '발신자')
    wk0.update_cell(1, 2, '날짜')
    wk0.update_cell(1, 3, '시간')
    wk0.update_cell(1, 4, '메세지')
    wk0.update_cell(1, 5, '첨부파일-경로')
    i = 2

    # 채팅방에서 chatlog로 이동
    xUrl = driver.current_url.split('/')
    idUrl = xUrl[len(xUrl) - 1]
    chatlogs_Url = 'https://center-pf.kakao.com/api/profiles/_EvRij/chats/' + idUrl + '/chatlogs'

# 채팅로그 json으로 가져오기
    driver.get(chatlogs_Url)
    text = driver.find_element_by_tag_name('body').text
    dict = json.loads(text)

    for h in dict['items']:
        # 유닉스 밀리초를  타임스템프로 변환
        ms_time = pandas.to_datetime(h['send_at'], unit='ms')
        print(h['author']['nickname'],ms_time,h['message'])

        wk0.update_cell(i, 1, h['author']['nickname'])
        wk0.update_cell(i, 2, str(ms_time.date()))  # 타임스탬프 date 속성
        wk0.update_cell(i, 3, str(ms_time.time()))  # 타임스탬프 time 속성
        wk0.update_cell(i, 4, h['message'])
        if h['attachment'] == True:
            wk0.update_cell(i, 5, h['attachment']['url'])
        i+=1
    driver.close()
    driver.switch_to_window(main_window)
    x+=1    # 워크시트 번호
# driver.close()






