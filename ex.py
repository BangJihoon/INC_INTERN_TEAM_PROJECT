# 크롤링 및 구글스프레드시트 연동
from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# api로 접속
api = 'gspread.json'
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(api,scope)

gc = gspread.authorize(credentials)

# 스프레드시트 열기
wks = gc.open("TEST")

# 워크시트열기
wk0 = wks.get_worksheet(0)

driver = webdriver.Chrome('C:/chromedriver')

# 웹 자원 로드를 위해 3초 대기
driver.implicitly_wait(3)

# 평생교육원 채팅방 url 호출
driver.get('https://center-pf.kakao.com/_EvRij/chats')

# 로그인하기
# 아이디/패스워드 입력하기
driver.find_element_by_id('loginEmail').send_keys('skuinc.internship@skuniv.ac.kr') # 아이디 보안상 삭제함
driver.find_element_by_id('loginPw').send_keys('!@#$intern12') # 비번은 보안상 삭제함

# 로그인 버튼 클릭하기
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/button').click()

num = 1;
chat_list = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div').find_elements_by_tag_name('li')
main_window = driver.window_handles[0]  # 부모창

# 리스트 길이 찾기
for i in chat_list:
    x=1
    i.click()
    driver.switch_to_window(driver.window_handles[1])
    chats = driver.find_elements_by_class_name('item_chat')
    for chat in chats:
        wk0.update_cell( x,num, chat.text)
        x+=1
        print(chat.text)
        print('-----------------------------------')
    num += 1
    driver.close()
    driver.switch_to_window(main_window)



