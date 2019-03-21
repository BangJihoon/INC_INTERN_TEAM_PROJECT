create database kakao;

create table room(
	room_ID int PRIMARY KEY AUTO_INCREMENT,
	nickname varchar(30),
	manager varchar(30),
	consult_field varchar(30)
);

create table dialog(
	room_ID int PRIMARY KEY,
	chat_date varchar(30),
	chat_time varchar(30),
	chat_sender varchar(30),
	chat_msg varchar(1024), 
	attach_url varchar(1024)
);

