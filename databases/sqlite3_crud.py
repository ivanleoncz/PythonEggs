import datetime
import sqlite3


class Crud:

    def __init__(self):
        self.conn = sqlite3.connect("crud_db.sqlite3")


    def build(self):
        try:
            cursor = self.conn.cursor()
            drop_table_if = """ DROP TABLE IF EXISTS Employees """
            cursor.execute(drop_table_if)
            create_table = """ CREATE TABLE Employees
                (
                    Id INTEGER PRIMARY KEY,
                    FullName TEXT,
                    Role TEXT,
                    CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                    UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            cursor.execute(create_table)
            self.conn.commit()
        except Exception as e:
            return e


    def create(self, name, role):
        try:
            cursor = self.conn.cursor()
            create_record = """ INSERT INTO Employees
                (FullName, Role) VALUES ('{0}', '{1}') """.format(name, role)
            cursor.execute(create_record)
            row_id = cursor.lastrowid
            self.conn.commit()
            return row_id
        except Exception as e:
            return e


    def read(self, employee_id=None):
        try:
            cursor = self.conn.cursor()
            query = None
            if employee_id is None:
                query = """ SELECT * FROM Employees """
            else:
                query = """ SELECT * FROM Employees
                            WHERE Id='{0}' """.format(employee_id)
            cursor.execute(query)
            data = cursor.fetchall()
            if len(data) > 0:
                data = [row for row in data[0]]
            self.conn.commit()
            return data
        except Exception as e:
            return e


    def update(self, name, role, employee_id):
        try:
            ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            cursor = self.conn.cursor()
            update_record = """ UPDATE Employees
                SET FullName='{0}', Role='{1}', UpdateTime='{3}'
                WHERE Id='{2}' """.format(name, role, employee_id, ts)
            cursor.execute(update_record)
            self.conn.commit()
            check_update = self.read(employee_id)
            if check_update[3] < check_update[4]:
                return 0
            else:
                return 1
        except Exception as e:
            return e


    def delete(self, employee_id):
        try:
            cursor = self.conn.cursor()
            delete_record = """ DELETE FROM Employees
                                WHERE Id='{0}' """.format(employee_id)
            cursor.execute(delete_record)
            self.conn.commit()
            check_delete = self.read(employee_id)
            if len(check_delete) == 0:
                return 0
            else:
                return 1
        except Exception as e:
            return e
