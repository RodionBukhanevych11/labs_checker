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
        conn = psycopg2.connect(dbname=self.dbname, user=self.user, 
                            password=self.password, host=self.host)
        self.cursor = conn.cursor()

    def check_user(self, user: str) -> bool:
        self.cursor.execute(f"SELECT user FROM {self.dbname}")
        users = self.cursor.fetchall()
        if user in users:
            return True
        else:
            return False
        
    def check_password(self, user: str, password: str) -> bool:
        self.cursor.execute(f"SELECT password FROM {self.dbname} WHERE user = {user}")
        db_password = self.cursor.fetchall()
        if password == db_password:
            return True
        else:
            return False
        

if __name__ == "__main__":
    labsCheckerDb = LabsCheckerDB(dbname=_CONFIG["dbname"],
                                  user=_CONFIG["user"],
                                  password=_CONFIG["password"],
                                  host=_CONFIG["db_host"])

    