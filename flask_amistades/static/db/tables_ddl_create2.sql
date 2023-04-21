use flask_mysql_coding_dojo;

create table friendships(
id int not null auto_increment primary key,
user_id int not null,
friend_id int not null,
created_at datetime,
updated_at datetime
);