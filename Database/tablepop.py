__author__ = 'zwx'
"""
Populates a table with data from a Python tuple.
"""
import mysql.connector
from database import login_info

if __name__ =="__main__":

    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()

    data = (
            ("Ellie", "Elephant", 2350),
            ("Gerald", "Gnu", 1400),
            ("Gerald", "Giraffe", 940),
            ("Leonard", "Leopard", 280),
            ("Sam", "Snake", 24),
            ("Steve", "Snake", 35),
            ("Zorro", "Zebra", 340)
            )

    cursor.execute(""" CREATE TABLE IF NOT EXISTS animal(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    family VARCHAR(50),
    weight INTEGER) ENGINE = MYISAM;
    """)

    cursor.execute("DELETE IGNORE FROM animal")
    for t in data:
        cursor.execute("""
        INSERT INTO animal (name, family, weight)
        VALUES (%s, %s, %s)""", t)

    db.commit()
    print("Finished")