from django.db import models
import psycopg2

# Create your models here.

def insert_user(age, name, dob):
    conn = psycopg2.connect("dbname='Test' user='postgres' host='localhost' password='sra123'")
    cursor = conn.cursor()
    command = f'insert into users values({age}, \'{name}\', \'{dob}\')'
    cursor.execute(command)
    conn.commit()
    conn.close()

def fetch_data():
    conn = psycopg2.connect("dbname='Test' user='postgres' host='localhost' password='sra123'")
    cursor = conn.cursor()
    command = f'select * from users'
    cursor.execute(command)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data
