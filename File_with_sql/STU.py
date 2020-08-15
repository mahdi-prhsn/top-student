import sqlite3 as db
from datetime import datetime

#Here we made connection with database
conn = db.connect('lessons.db')

#Here we use 'c' as cursor to keep connection with database
c = conn.cursor()

def init():
    c.execute('''CREATE TABLE IF NOT EXISTS students(  
                name TEXT,
                family TEXT,
                code INTEGER,
                math REAL,
                physics REAL,
                chemistry REAL
                )''')
    conn.commit()
    c.close()
    

def add(name, family, code, math, physics, chemistry):
    c.execute('INSERT INTO students VALUES (:name, :family, :code, :math, :physics, :chemistry)', {'name': name, 'family':family, 'code':code, 'math':math, 'physics': physics, 'chemistry':chemistry})
    conn.commit()
    c.close()

def show(code):
    c.execute('SELECT name,family FROM students WHERE code = (:code)',{'code':code})
    result = c.fetchone()
    full_name = f'{result[0]} {result[1]}'
    c.execute('SELECT math,chemistry,physics FROM students WHERE code = (:code)',{'code':code})
    marks = c.fetchone()
    avg = round((marks[0]+marks[1]+marks[2]) / 3,2)
    return full_name, avg

def max_min(code):
    c.execute('SELECT name,family FROM students WHERE code = (:code)',{'code':code})
    result = c.fetchone()
    full_name = f'{result[0]} {result[1]}'
    c.execute('SELECT MAX(math,chemistry,physics) FROM students WHERE code = (:code)',{'code':code})
    maximum = c.fetchone()[0]
    c.execute('SELECT MIN(math,chemistry,physics) FROM students WHERE code = (:code)',{'code':code})
    minimum = c.fetchone()[0]
    return full_name, maximum, minimum

