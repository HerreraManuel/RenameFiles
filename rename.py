import os
import os.path
import sqlite3

os.chdir("X:\\Code\\Python\\RenameFiles\\img")
i = 1
connect = sqlite3.connect("X:\\Code\\Python\\RenameFiles\\pokedex.sqlite3")
cursor = connect.cursor()
for file in os.listdir():
    src = file
    if i == 152:
        break
    sql = """
    SELECT id, name
    FROM pokemon
    WHERE id=?;"""
    cursor.execute(sql, (i,))
    fetched_data = cursor.fetchone()
    update = src.lstrip("0")
    str_of_filename = ''.join(filter(lambda i : i.isdigit(), update))
    digit = int(str_of_filename)
    if digit == int(fetched_data[0]):
        poke_name = fetched_data[1]
        dest = poke_name + ".png"
        print(dest)
        os.rename(src, dest)
    i+=1