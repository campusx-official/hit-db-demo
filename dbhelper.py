import mysql.connector
import sys
class DBhelper:

    def __init__(self):
        # connect to database
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="",database="hit-db-demo")
            # create cursor
            self.mycursor = self.conn.cursor()
            print("Connected to database")
        except Exception as e:
            print("Cant connect to database. Try after some time")
            sys.exit(0)

    def register(self,name,email,password):

        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')
            """.format(name,email,password))
            self.conn.commit()
        except Exception as e:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))

        data = self.mycursor.fetchall()

        return data



