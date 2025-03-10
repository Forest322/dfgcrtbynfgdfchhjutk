import sqlite3
import datetime

db_name = "data.db"


def create_post_table():
    SQL = """
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY,
            title TEXT,
            descripton TEXT,
            at_publish TEXT,
            author_id INTEGER 
        )
    """
    con = sqlite3.connect(db_name)
    con.execute(SQL)


class Post:
    def __init__(self, id, title, description, at_publish, author_id):
        self.id = id
        self.description = description
        self.at_publish = at_publish
        self.author_id = author_id
        self.title = title

    @staticmethod
    def create(title, description, author_id):
        at_publish = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        SQL = """ 
            INSERT INTO post (title, description, at_publish, author_id)
            WHERE (?, ?, ?, ?)
        """
        con = sqlite3.connect(db_name)
        con.execute(SQL, [title, description, at_publish, author_id])
        con.commit()

    @staticmethod
    def get_post_by_author_id(author_id):
        SQL = """
            SELECT * FROM post WHERE author_id = ?
        """
        con = sqlite3.connect(db_name)
        q = con.execute(SQL, [author_id])
        data = q.fetchall()
        return [Post(*row) for row in data]

    @staticmethod
    def get_all():
        SQL = """
            SELECT * FROM post """
        con = sqlite3.connect(db_name)
        q = con.execute(SQL)
        data = q.fetchall()
        return [Post(*row) for row in data]
