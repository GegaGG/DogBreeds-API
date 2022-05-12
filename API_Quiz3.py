#Gega Gongadze
import requests
import json
import sqlite3

Breed =  input("შეიყვანეთ სასურველი  ძაღლის ჯიში ინგლისურად! : " )

URL = f'https://dog.ceo/api/breed/{Breed}/images'

R = requests.get(URL)
print(R.status_code)
print(R.headers)

res = json.loads(R.text)
print(json.dumps(res, indent= 4))

conn = sqlite3.connect("Dogs_Breed.db")
cursor = conn.cursor()

dataB = '''CREATE TABLE IF NOT EXISTS  DOGBREEDS(Breed VARCHAR(45), image VARCHAR(100)
)
'''
cursor.execute(dataB)
print("Table Was Created")


insert =''' insert into DOGBREEDS(Breed, image) values (?,?)
 '''

values = (Breed, len(res['message']))
cursor.execute(insert, values)
print("Table was written")

conn.commit()