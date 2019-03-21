# 1번방에 1~100까지 자동 메세지 보내기
from selenium import webdriver
import time


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

chat_list = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div').find_elements_by_tag_name('li')
main_window = driver.window_handles[0]  # 부모창

chat_list[0].click()
driver.switch_to_window(driver.window_handles[1])
for i in range(1,100):
    driver.find_element_by_id('chatWrite').send_keys(i) # 아이디 보안상 삭제함
    driver.find_element_by_xpath('//*/fieldset/button').click()
    time.sleep(1)

driver.close()