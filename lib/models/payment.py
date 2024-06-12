
import sqlite3


conn = sqlite3.connect('db/school.db')
cursor = conn.cursor()

class Payment:
    def __init__(self, first_name, last_name, gender, amount):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.amount = amount

    def __repr__(self):
        return f"<Payment {self.first_name} {self.last_name} {self.gender} {self.amount}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                gender TEXT,
                amount TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def create(cls, first_name, last_name, gender, amount):
        sql = """
            INSERT INTO payments (first_name, last_name, gender, amount)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (first_name, last_name, gender, amount))
        conn.commit()
        return cls(first_name, last_name, gender, amount)
