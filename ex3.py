# json 잡아서 필요데이터만 저장하기
from selenium import webdriver
import gspread , requests, json,pprint
from oauth2client.service_account import ServiceAccountCredentials

# 구글 시트 연동
api = 'gspread.json'
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(api,scope)
gc = gspread.authorize(credentials)
wks = gc.open("TEST")
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

j = 1;
chat_list = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div').find_elements_by_tag_name('li')
main_window = driver.window_handles[0]  # 부모창

# 채팅방 하나씩 잡기
chat_list[1].click()
driver.switch_to_window(driver.window_handles[1])

# 채팅방에서 json 경로로 이동
xUrl = driver.current_url.split('/')
idUrl = xUrl[len(xUrl)-1]
chatlogs_Url = 'https://center-pf.kakao.com/api/profiles/_EvRij/chats/'+ idUrl +'/chatlogs'
driver.get(chatlogs_Url)
text = driver.find_element_by_tag_name('body').text
pprint.pprint(text)
dict = json.loads(text)

# 이름 ,날짜, 텍스트, 담당자, 이미지 등
for h in dict['items']:
    print(h['message'], h['send_at'],h['author']['nickname'])
