drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title text not null,
	txtblock text not null,
	CHECK(txtblock <> '' and title <> '')
);

drop table if exists users;
create table users (
        uid integer primary key autoincrement,
        username text not null unique,
	pass password not null,
	question text not null,
	answer text not null
);

insert into users (username, pass, question, answer)
values 
("icm", "def", "Your name", "Isaac");
