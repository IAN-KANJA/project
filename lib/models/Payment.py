from __init__ import conn ,cursor
class payment:
        def __init__(self,first_name, last_name, gender,amountpaid ):
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
            self.gender = gender
            self.amountpaid = amountpaid


        def __repr__(self):
            return f"<payment{self.first_name} {self.last_name} {self.gender} {self.amountpaid}"
            
        @classmethod
        def create_table(cls):
            sql = """
                CREATE TABLE payment (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                gender TEXT,
                amountpaid INTERGER,
                )
            """    

        cursor.execute(sql)
        conn.commit()