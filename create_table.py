import sqlite3

connection = sqlite3.connect("wallet.db")
cursor = connection.cursor()

create_table = "create table if not exists tbl_user (id integer primary key, username text, password text)"
cursor.execute(create_table)

create_table = (
    "create table if not exists tbl_category (id integer primary key, name text)"
)
cursor.execute(create_table)

create_table = "create table if not exists tbl_transaction (id integer primary key, name text, description text, date text, user_id integer not null, category_id integer not null, foreign key (user_id) references tbl_user (id), foreign key (category_id) references tbl_category (id))"
cursor.execute(create_table)

connection.commit()
connection.close()
