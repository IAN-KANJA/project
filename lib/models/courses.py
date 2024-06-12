from __init__ import conn, cursor

class Courses:
    def __init__(self, first_course, duration):
        self.name_course = first_course
        self.duration = duration

    def __repr__(self):
        return f"<Courses {self.first_course} {self.duration}>"
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_course TEXT,
                duration TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def create(cls, first_course, duration):
        sql = """
            INSERT INTO courses (first_course, duration)
            VALUES (?, ?)
        """
        cursor.execute(sql, (first_course, duration))
        conn.commit()
        return cls(first_course, duration)
