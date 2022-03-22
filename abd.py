from flask import Flask, jsonify, request

import sqlite3

from sql import insert, updates, delete
from sql import getall

app =Flask(__name__)
@app.get('/')
def vk():
    return "homepage"

@app.post('/h')
def vk1():
    data= request.get_json()
    insert(data)
    print(data)
    return 'DATA IS RETRIEVED'

@app.post('/v')
def vk2():
    data= getall()
    return (jsonify(data))

@app.patch('/upd')
def update():
    data = request.get_json();
    updates(data);
    print(data);
    return("Updated"); 

@app.patch('/pat/<inputId>')
def patchmethod(inputId):
    data = request.get_json()
    users = data     

    #print(inputId)
    #print (f'The users data is{users}')

    if inputId in users.values():
        users["Id"] = 1000
        print(f"The data after updating is{users}")
        res = "Data updated"
        return res
    print(f"The data after creation is {users}")
    res = "Data created"


@app.delete("/delete/<roll_no>")
def deletes(roll_no):
    delete(roll_no);
    return("deleted")

@app.delete('/del/<inputId>')
def deletemethod(inputId):
    data = request.get_json()
    users = data 

    #print(inputId)
    #print (f'The users data is{users}')

    if inputId in users.values():
        del users["Id"]
        #print(f"The data after deleting is{users}")
        print(f"the data is deleted {users}")
        res = "Data deleted"
        
        return res
    res = "Data not found"
    return res

app.run(debug=True)