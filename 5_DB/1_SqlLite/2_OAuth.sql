-- Удаления таблиц
DROP TABLE Users;
DROP TABLE JWT;
DROP TABLE OAuth_Telegram;
DROP TABLE OAuth_Google;
DROP TABLE OAuth_GitHub;

-- Пользователи сайта
CREATE TABLE Users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT
);

-- Регистрация через email отправку письма
CREATE TABLE JWT(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT, -- Имяпользователя, уникальное
	email TEXT, -- Почта для получения письма, уникальная
	password_hesh TEXT, -- Хеш пароля два входа
	is_confirm INTEGER, -- Потдвердил почту или нет
	id_user INTEGER,
	FOREIGN KEY (id_user) REFERENCES Users(id)
);

CREATE TABLE OAuth_Telegram(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_telegram INTEGER, -- Уникальное
	first_name TEXT,
	last_name TEXT,
	username TEXT,
	photo_url TEXT,
	id_user INTEGER,
	FOREIGN KEY (id_user) REFERENCES Users(id)
);

CREATE TABLE OAuth_Google(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_google TEXT, -- 9 байтов нужен текст, уникальное
	email TEXT,
	verified_email INTEGER,
	name TEXT,
	given_name TEXT,
	family_name TEXT,
	picture TEXT,
	id_user INTEGER,
	FOREIGN KEY (id_user) REFERENCES Users(id)
);

CREATE TABLE OAuth_GitHub(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	login TEXT,
	id_github INTEGER,
	avatar_url TEXT,
	id_user INTEGER,
	FOREIGN KEY (id_user) REFERENCES Users(id)
);