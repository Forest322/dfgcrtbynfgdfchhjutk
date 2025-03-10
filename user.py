import sqlite3
import hashlib

db_name = 'data.db'
 

def create_user_table():
    SQL = """ 
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT
        )
    """
    con = sqlite3.connect(db_name)
    con.execute(SQL)

class User:
    def __hash__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash


    @staticmethod
    def get_user_by_username(username):
            SQL = "SELECT * FROM user WHERE username = ?"
            con = sqlite3.connect(db_name)
            q = con.execute(SQL, [username])
            data = q.fetchone()
            return User(*data)
    
    @staticmethod
    def hashed_password(password: str):
         return hashlib.sha256(password.encode()).hexdigest()


    @staticmethod
    def create(username, password):
        password_hash = User.password(password)

        SQL = """" 
            INSERT INTO user (username, password_hash)
            VALUES (?, ?)
        """
        con = sqlite3.connect(db_name)
        con.execute(SQL, [username, password_hash])
        con.commit()