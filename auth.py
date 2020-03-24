import sqlite3
con = sqlite3.Connection('email-db')
cur = con.cursor()

def create():
    username = input('Username? ')
    password = input('Password? ')
    cur.execute('PRAGMA foreign_keys = ON')
    table_if_exists = 'create table if not exists auth(id integer primary key AUTOINCREMENT,username varchar(25),password varchar(25),fname varchar(20),lname varchar(25))'
    cur.execute(table_if_exists)
    con.commit()
    uname_s_q = 'select * from auth where username="{}"'.format(username)
    cur.execute(uname_s_q)
    res = cur.fetchall()
    if len(res)==0:
        print("username available!")
        fname=input("First Name? ")
        lname=input("Last Name? ")
        create_acc = 'insert into auth(username,password,fname,lname) values(?,?,?,?)'
        tup_val = [(username),(password),(fname),(lname)]
        cur.execute(create_acc,tup_val)
        con.commit()
    else:
        print("Username not available, choose another one")
        create()

def search():
    uname = input('uname to search? ')
    uname_s_q = 'select * from auth'
    cur.execute(uname_s_q)
    print(cur.fetchall())

def login():
    uname = input("username : ")
    passwd = input("password : ")
    query = 'select * from auth where username = ?'
    cur.execute(query,[(uname)])
    res = cur.fetchall()
    if(len(res)==0):
        if(res[0][2]==passwd):
            return True
        return False
    else:
        return False
print(login())