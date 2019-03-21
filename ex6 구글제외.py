
from selenium import webdriver
import requests, json
import pandas,time
from selenium.webdriver.common.keys import Keys

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

# 채팅방 하나씩 순회
for chat_room in chat_list:
    chat_room.click()
    driver.switch_to_window(driver.window_handles[1])
    # 상담자
    user_text = driver.find_element_by_xpath('//*[@id="kakaoWrap"]/div[1]/div[1]/div[1]/div/div/strong').text
    user_text = user_text.split('\n')
    chat_user = user_text[1]
    # 담당자
    chat_manager = driver.find_element_by_class_name('tit_profile').text
    scroll_count = 30
    while scroll_count > 0: # 50번 반복
        time.sleep(0.1)
        elem = driver.find_element_by_tag_name('body')  # 바디였어!! 스크롤은 바디였어!!! - if 이미지 뜨면 처리해야함
        elem.click()
        elem.send_keys(Keys.HOME)
        scroll_count-=1
    elem.click()
    elem.send_keys(Keys.HOME)

    # print('보낸이 \t날짜 \t시간 \t메세지 \t첨부url')
    chats_by_date = driver.find_elements_by_xpath('//*[@id="room"]/div/div')     # 날짜별 박스들 잡기
    for chat_by_date in chats_by_date:
        chat_date = chat_by_date.find_element_by_class_name('emph_date')    # 날짜별 박스 안에 날짜뽑기

        chats = chat_by_date.find_elements_by_class_name('item_chat')       # 박스 안에 대화상자들 뽑기
        print('--------------- 날짜 : '+ chat_date.text+'-----------------')
        for chat in chats:
            print('이름: ' + chat_user)
            print('상담자 : ' + chat_manager)
            print('날짜: ' + chat_date.text)
            try:
                print('시간 : '+ chat.find_element_by_class_name('txt_time').text)
            except Exception:
                pass
            print('내용: ' + chat.find_element_by_class_name('set_chat').text)  # 메시지 출력
            try:
                print('첨부 : '+ chat.find_element_by_class_name('link_pic').get_attribute('href'))
            except Exception:
                pass
            print('-----------------')
    driver.close()
    driver.switch_to_window(main_window)
    i+=1

# 보냄 : #room > div > div:nth-child(3) > div:nth-child(2) > div.wrap_cont > strong
# 날짜 : #room > div > div:nth-child(2) > div.bg_line > em > span
# 시간 : #room > div > div:nth-child(2) > div.item_chat.item_save > div.wrap_cont > span > span
# 대화 : #room > div > div:nth-child(3) > div:nth-child(4) > div.wrap_cont > div > div > div > p > span
# 첨부 : #room > div > div:nth-child(3) > div:nth-child(3) > div > div > a.link_pic
