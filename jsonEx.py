import json,pprint

# 테스트용 JSON 문자열
jsonString = '''{
  "items": [
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238409000,
      "id": "1889963521143146496",
      "type": 1,
      "author_id": "_EvRij",
      "message": "56",
      "prev_id": "1889963511437522944",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238410000,
      "id": "1889963530085429248",
      "type": 1,
      "author_id": "_EvRij",
      "message": "57",
      "prev_id": "1889963521143146496",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238411000,
      "id": "1889963541233864704",
      "type": 1,
      "author_id": "_EvRij",
      "message": "58",
      "prev_id": "1889963530085429248",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238505000,
      "id": "1889964331600111617",
      "type": 1,
      "author_id": "_EvRij",
      "message": "asd",
      "prev_id": "1889963541233864704",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238512000,
      "id": "1889964387082373120",
      "type": 1,
      "author_id": "_EvRij",
      "message": "sdfgh",
      "prev_id": "1889964331600111617",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238907000,
      "id": "1889967700205045760",
      "type": 1,
      "author_id": "_EvRij",
      "message": "1",
      "prev_id": "1889964387082373120",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238908000,
      "id": "1889967709734531072",
      "type": 1,
      "author_id": "_EvRij",
      "message": "2",
      "prev_id": "1889967700205045760",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238909000,
      "id": "1889967718509012992",
      "type": 1,
      "author_id": "_EvRij",
      "message": "3",
      "prev_id": "1889967709734531072",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238910000,
      "id": "1889967727971340288",
      "type": 1,
      "author_id": "_EvRij",
      "message": "4",
      "prev_id": "1889967718509012992",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238911000,
      "id": "1889967737349820416",
      "type": 1,
      "author_id": "_EvRij",
      "message": "5",
      "prev_id": "1889967727971340288",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238912000,
      "id": "1889967746275280896",
      "type": 1,
      "author_id": "_EvRij",
      "message": "6",
      "prev_id": "1889967737349820416",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238913000,
      "id": "1889967755326617600",
      "type": 1,
      "author_id": "_EvRij",
      "message": "7",
      "prev_id": "1889967746275280896",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238914000,
      "id": "1889967764235319296",
      "type": 1,
      "author_id": "_EvRij",
      "message": "8",
      "prev_id": "1889967755326617600",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238916000,
      "id": "1889967773429227520",
      "type": 1,
      "author_id": "_EvRij",
      "message": "9",
      "prev_id": "1889967764235319296",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238917000,
      "id": "1889967782707034112",
      "type": 1,
      "author_id": "_EvRij",
      "message": "10",
      "prev_id": "1889967773429227520",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238918000,
      "id": "1889967793360539648",
      "type": 1,
      "author_id": "_EvRij",
      "message": "11",
      "prev_id": "1889967782707034112",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238919000,
      "id": "1889967802420226048",
      "type": 1,
      "author_id": "_EvRij",
      "message": "12",
      "prev_id": "1889967793360539648",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238920000,
      "id": "1889967811857410048",
      "type": 1,
      "author_id": "_EvRij",
      "message": "13",
      "prev_id": "1889967802420226048",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238921000,
      "id": "1889967821000996865",
      "type": 1,
      "author_id": "_EvRij",
      "message": "14",
      "prev_id": "1889967811857410048",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238922000,
      "id": "1889967830136213504",
      "type": 1,
      "author_id": "_EvRij",
      "message": "15",
      "prev_id": "1889967821000996865",
      "chat_id": "4734047852163186"
    },
    {
      "attachment": {
        
      },
      "manager": {
        "id": "996324314",
        "name": "skuincinternship"
      },
      "profile_id": "_EvRij",
      "author": {
        "status_message": "",
        "user_type": 1,
        "deactivated_at": 0,
        "nickname": "skuincinternship",
        "original_profile_image_url": "http://p.talk.kakao.co.kr/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i.jpg",
        "created_at": 1545982467000,
        "active": true,
        "profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_110x110_c.jpg",
        "id": "_EvRij",
        "uuid": "@internship",
        "full_profile_image_url": "http://th-p.talk.kakao.co.kr/th/talkp/wk1G6ITOXX/R7Y02aFMZKcbYJm1fYdQRk/rycr8i_640x640_s.jpg"
      },
      "supplement": {
        "muid": 996324314
      },
      "send_at": 1546238924000,
      "id": "1889967840202524672",
      "type": 1,
      "author_id": "_EvRij",
      "message": "16",
      "prev_id": "1889967830136213504",
      "chat_id": "4734047852163186"
    }
  ],
  "has_next": false,
  "has_prev": true
}'''

# JSON 디코딩
dict = json.loads(jsonString)

# Dictionary 데이타 체크
for h in dict['items']:
    print(h['message'], h['send_at'],h['author']['nickname'])