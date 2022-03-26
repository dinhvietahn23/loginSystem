import sqlite3
from tkinter import messagebox
from string import ascii_letters, digits

db = sqlite3.connect("login.db")
cursor = db.cursor()
cursor.execute('create table if not exists login(username TEXT, password TEXT)')

def login(username, password):
    login_session = cursor.execute("select * from login where username = ? and password = ? ", (username, password))
    if login_session.fetchone() is not None:
        messagebox.showinfo('info', 'login success')
    elif not check_username_login(username):
        messagebox.showwarning('warning', "Username dosen't exist \n Please try again")
    elif not check_password_login(username, password):
        messagebox.showwarning('warning', "Wrong password \n Please try again")


def check_username_login(username):
    row = cursor.execute("select * from login where username = ?", [username])
    return True if row.fetchone() is not None else False


def check_password_login(username, password):
    return True if cursor.execute("select username from login where password = ? and username = ?",
                                  [password, username]).fetchone() else False


def sign_up(username, password):
    if check_duplicate_username(username):
        messagebox.showwarning("warning", "Username is exist, please use another name")
    elif not check_password_valid(password):
        messagebox.showwarning("warning", "Password contains only alphabet and number")
    else:
        cursor.execute("insert into login(username, password) values(?,?)", [username, password])
        cursor.connection.commit()
        messagebox.showinfo('info', 'Register success')


def check_duplicate_username(username):
    row = cursor.execute("select * from login where username = ?", [username])
    return True if row.fetchone() is not None else False


def check_password_valid(password):
    return False if set(password).difference(ascii_letters + digits) else True


#sign_up("abc","abc")
#login("abc","abc")