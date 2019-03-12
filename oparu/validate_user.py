from passlib.hash import pbkdf2_sha256
import sqlite3

# def hash_password():
# TODO: make db construct/debug script 

conn = sqlite3.connect('users.db')
c = conn.cursor()
    
def add_user(user, passw):
    hash = pbkdf2_sha256.hash(passw)
    login = (user, hash)

    print(hash)
    c.execute("INSERT INTO user_login (USERNAME, PASSH) VALUES(?,?)", login)
    c.execute("SELECT * FROM user_login")
    print(c.fetchall())
    conn.commit()

def is_users():
    c.execute("SELECT COUNT(*) FROM user_login")

    if c.fetchone()[0] == 0:
        return ["New user"]
    else:
        return ["Continue", "New user"]

def get_users():
    c.execute("SELECT USERNAME from user_login")
    print(c.fetchone())
    # TODO: return list of current users

