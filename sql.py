import sqlite3

con =sqlite3.Connection("data.db",check_same_thread =False)

def getall():
    query = "select * from st75"
    cur = con.cursor()
    cur.execute(query)
    all_data = cur.fetchall()
    con.commit()
    return (all_data)

def insert(data):
    query1 = "create table if not exists st75 (Id varchar(25),Name varchar(25),roll_no varchar(25),Mark varchar(25))"
    params = (data["Id"],data["Name"],data["roll_no"],data["Mark"])
    query = "insert into st75 values(?,?,?,?)"
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query,params)
    con.commit()

def updates(data):
    query= f'update st75 set Name ="{data["Name"]}" where roll_no="{data["roll_no"]}" '; 
    cur=con.cursor();
    cur.execute(query);
    con.commit();   

def delete(roll_no):
    query= f'delete from st75 where roll_no= "{roll_no}"';
    cur = con.cursor();
    cur.execute(query);
    con.commit();    