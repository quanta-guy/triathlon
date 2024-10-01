import sqlite3
from sqlite3 import Error
import pandas as pd


def sql_connection():
    """Create a connection with SQLite database specified
        by the mytest.db file
    :param con: the connection object
    :return: connection object or Error"""
    try:
        db = sqlite3.connect('mytest.db')
        return db
    except Error:
        print(Error)



def insert_data(con, entities):
    """Insert records into the table"""
    query = """INSERT INTO employees (id,Title,Author,Genre, Publication_date,
            Price) VALUES(?,?,?,?,?,?)"""

    try:
        cur = con.cursor()
        cur.execute(query, entities)
        con.commit()
        print("The record added successfully")
    except Error:
        print(Error)



def select_all(con):
    """Selects all rows from the table to display"""
    try:
        cur = con.cursor()
        cur.execute('SELECT * FROM bookstore')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    except Error:
        print(Error)

""" 
def update_data(con, salary, id):
    Update the table with given new values
    try:
        cur = con.cursor()
        cur.execute("UPDATE employees SET salary = ?  WHERE id = ?", (salary,
                                                                      id))
        con.commit()
        print("The record updated successfully")
    except Error:
        print(Error)
 """

def delete_record(con, surname):
    """Delete the given record"""
    query = "DELETE FROM bookstore WHERE id = ?;"
    try:
        cur = con.cursor()
        cur.execute(query, (surname,))
        con.commit()
        print("The record delated successfully")
    except Error:
        print(Error)

#get all data
def read_db(genre:str='',author:str='',id:int=None):
    data=pd.read_csv(r'D:\Work\Others\Triatholon\database\triathlon_dummy.csv')
    if genre!='' and author!='':
        filtered_data=data.query(f"genre={genre}").query(f"author={author}")
    
    elif genre!='' :
        filtered_data=data.query(f"genre={genre}")
    elif   author!='':
        filtered_data=data.query(f"author={author}")
    else:
        filtered_data=data
    if id!=None:
        filtered_data=data.query(f"id={id}")
        return filtered_data.to_dict()
    response=filtered_data.to_dict()
    return response


"""     con=sql_connection()
    data=select_all(con) """