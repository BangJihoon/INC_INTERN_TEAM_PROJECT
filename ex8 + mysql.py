from selenium import webdriver
import time,requests
from selenium.webdriver.common.keys import Keys
import mysql1 as sql

# 크롬 드라이버로 채팅방 열기
driver = webdriver.Chrome('C:/chromedriver')
driver.implicitly_wait(3)
driver.get('https://center-pf.kakao.com/_EvRij/chats')    # 상담 채팅 url (추후 변경해줘야함)
driver.find_element_by_id('loginEmail').send_keys('skuinc.internship@skuniv.ac.kr')     # 아이디
driver.find_element_by_id('loginPw').send_keys('!@#$intern12')                          # 비번
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/button').click()           # 로그인


num = 1;
chat_list = driver.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[3]/div/div').find_elements_by_tag_name('li')
main_window = driver.window_handles[0] # 부모창

chat_items = []

# 모든 채팅방 열기
for chat_room in chat_list:
    #채팅방 하나 클릭
    chat_room.click()
    windows = len(driver.window_handles)
    print(windows)

    # 창 변환 _ 열린이미지 창을 count하여, 새롭게 열린 채팅방으로 switch
    driver.switch_to_window(driver.window_handles[num])

    # 상담자
    nickName = driver.find_element_by_xpath('//*[@id="kakaoWrap"]/div[1]/div[1]/div[1]/div/div/strong').text
    nickName = nickName.split('\n')[1]

    # 담당자
    chat_manager = driver.find_element_by_class_name('tit_profile').text

    # 스크롤 올리는 while문 현재는 10번만 올림
    scroll_count = 10
    while scroll_count > 0:
        time.sleep(0.3)
        element = driver.find_element_by_tag_name('body')
        element.click()
        element.send_keys(Keys.HOME)  # home키를 누르게 하여 스크롤 올림
        scroll_count -= 1
    # 스크롤 중 이미지가 열린 경우, 창 개수를 count함
        if windows + 1 == len(driver.window_handles):
            num += 1
            windows = len(driver.window_handles)
            print('num ======= ' + str(num))

    # 채팅방에서 item_chat (모든 대화) 가져오기
    chats = driver.find_elements_by_class_name('item_chat')

    # 날짜 가져오기
    chat_date = driver.find_element_by_class_name('bg_line').text.split(' ')[0]

    chat_time = ""

    for chat in chats:

        if(chat_date != driver.find_element_by_class_name('bg_line').text.split(' ')[0]):
            chat_date = driver.find_element_by_class_name('bg_line').text.split(' ')[0]

        # 메세지 가져오기
        chat_msg = chat.find_element_by_class_name('set_chat').text
        print(nickName)     # 닉네임 출력
        print(chat_msg)     # 메시지 출력

        # 이미지 태그가 있는지 없는지 확인하는 try/except문
        img_url = ''
        try:
            print(chat.find_element_by_class_name('link_pic').get_attribute('href'))
            img_url = chat.find_element_by_class_name('link_pic').get_attribute('href')
            filename = img_url.split('/')[-1]
            r = requests.get(img_url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            img_url = upload_file.saveImage(filename)

        except Exception:
            pass

        # 시간 태그가 있는지 없는지 확인하는 try/except문
        try:
            chat_time = chat.find_element_by_class_name('txt_time').text
        except Exception:
            pass
        print(chat_time)
        print('=========================')

        # 디비 저장 : nickname,날짜,시간,담당자, 메세지, 첨부url
        sql.save_msg(nickName,chat_date,chat_time,chat_manager,chat_msg,img_url)

    # num += 1
    driver.close()
    driver.switch_to_window(main_window)