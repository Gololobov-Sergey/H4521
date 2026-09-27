import sqlite3
import hashlib

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ===== CREATE =========
# cur.execute("CREATE TABLE user (login TEXT, password TEXT);")
# connection.commit()


# ===== INSERT =========
# login = input("Enter login : ")
# password = input("Enter password : ")
# m = hashlib.sha256()
# m.update(b"{password}")
# passhash = m.hexdigest()
# cur.execute(f"INSERT INTO user (login, password) VALUES ('{login}', '{passhash}');")
# connection.commit()
# print("User added")

# ===== SELECT =========
# cur.execute(f"SELECT * FROM user;")
# # cur.execute(f"SELECT rowid, login, password FROM user;")
# # cur.execute(f"SELECT * FROM user WHERE login = 'olga';")
# connection.commit()
# res = cur.fetchall()
# print(res)

# ===== UPDATE ========
# m = hashlib.sha256()
# m.update(b"serg")
# passhash = m.hexdigest()
# cur.execute(f"UPDATE user SET password = '{passhash}' WHERE rowid = 1")
# connection.commit()


# ===== DELETE =====
cur.execute("DELETE FROM user WHERE rowid = 4")
connection.commit()


connection.close()
