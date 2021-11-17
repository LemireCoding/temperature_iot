import mysql.connector

from flask import request, jsonify
class DBUtil:
    def __init__(self):
        try:
            self.config_file = "my.conf"
            self.connex = mysql.connector.connect(option_files=self.config_file)
        except mysql.connector.Error as e:
            print(e)
            self.close()

    def execute_select_query(self, table_name, search=None):
        return_set = []
        cursor = self.connex.cursor(dictionary=True)
        if search is None:
            cursor.execute("select * from {}".format(table_name))
        else:

            sql = "SELECT * FROM {}".format(table_name) + search
            cursor.execute(sql)

        for x in cursor:
            return_set.append(x)

        cursor.close()
        return return_set

    def execute_insert_query(self, objectToAdd):

        insert = "INSERT INTO temp (datetime, temp, humidity) VALUES (%s, %s, %s)"
        cursor = self.connex.cursor()
        add = (objectToAdd.datetime,objectToAdd.temp,objectToAdd.humidity)

        cursor.execute(insert, add)
        emp_no = cursor.lastrowid  # Get the last inserted ID (if applicable)
        self.connex.commit()
        cursor.close()
        return emp_no
