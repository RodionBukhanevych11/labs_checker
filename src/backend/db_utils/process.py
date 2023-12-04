import json
import psycopg2


_CONFIG = json.load(open("src/config.json"))


class LabsCheckerDB:
    def __init__(self, dbname, user, password, table_name, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.table_name = table_name
        self.host = host
        self.connect()

    def connect(self):
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, 
                            password=self.password, host=self.host)
        self.cursor = self.conn.cursor()

    def check_user(self, username: str) -> bool:
        self.cursor.execute(f"""SELECT username FROM {self.table_name};""")
        usernames = self.cursor.fetchall() # users turns into a list of tuples
        if (username,) in usernames: # we must compare not username but this wierd tuple to users just because of the behaviour of fetchall() 
            return True
        else:
            return False
        
    def check_password(self, username: str, password: str) -> bool:
        self.cursor.execute(f"""SELECT password FROM {self.table_name} WHERE username = '{username}';""")
        db_password = self.cursor.fetchone()
        if (password,) == db_password:
            return True
        else:
            return False
    
    def register_user(self, username: str, password: str):
        self.cursor.execute(f"""INSERT INTO {self.table_name} (username, password)
                            VALUES ('{username}', '{password}');""")
        self.conn.commit()

if __name__ == "__main__":
    labsCheckerDb = LabsCheckerDB(dbname=_CONFIG["db_name"],
                    user=_CONFIG["db_user"],
                    password=_CONFIG["db_password"],
                    table_name=_CONFIG["db_table_name"],
                    host=_CONFIG["db_host"])

    