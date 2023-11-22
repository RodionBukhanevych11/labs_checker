import json
import psycopg2


_CONFIG = json.load(open("src/config.json"))


class LabsCheckerDB:
    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, 
                            password=self.password, host=self.host)
        self.cursor = self.conn.cursor()

    def check_user(self, user: str) -> bool:
        self.cursor.execute(f"""SELECT user FROM {self.dbname};""")
        users = self.cursor.fetchall()
        print(users)
        if user in users:
            return True
        else:
            return False
        
    def check_password(self, user: str, password: str) -> bool:
        self.cursor.execute(f"""SELECT password FROM {self.dbname} WHERE user = {user};""")
        db_password = self.cursor.fetchall()
        if password == db_password:
            return True
        else:
            return False
    
    def register_user(self, username, password):
        self.cursor.execute(f"""INSERT INTO users (username, password)
                            VALUES ({username}, {password});""")

if __name__ == "__main__":
    labsCheckerDb = LabsCheckerDB(dbname=_CONFIG["dbname"],
                                  user=_CONFIG["user"],
                                  password='12345678',
                                  host=_CONFIG["dbhost"])

    