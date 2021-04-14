import sqlite3
from sqlite3.dbapi2 import PARSE_COLNAMES, register_adapter

class DBConnection():

    instance = None
    conn = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(DBConnection)
            return cls.instance
        return cls.instance

    def __init__(self, db_name='ringsim.db'):
        self.name = db_name
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        try:
            return sqlite3.connect(self.name)
        except sqlite3.Error as e:
            pass


  # write CRUD operations below

    # Record CRUD
    def create_record(self, address):
        values = address.get_complete_address()
        query = '''INSERT INTO ADDRESS 
                    (symbol_1, symbol_2, symbol_3, symbol_4, symbol_5, symbol_6, symbol_7) 
                    VALUES(?,?,?,?,?,?,?);'''
        self.cursor.execute(query,values)
        self.conn.commit()

    def read_record(self, address):
        values = address.get_complete_address()
        query = "SELECT * FROM ADDRESS WHERE"
        where = f''' symbol_1 = '{values[0]}' AND symbol_2 = '{values[1]}' AND symbol_3 = '{values[2]}' AND symbol_4 = '{values[3]}' AND symbol_5 = '{values[4]}' AND symbol_6 = '{values[5]}' AND symbol_7 = '{values[6]}';''' 
                    #.format(values[0],values[1],values[2],values[3],values[4],values[5],values[6])
        
        query = query + where

        address2 = self.cursor.execute(query)
        #print(address2.fetchone())
        self.conn.commit()

        return address2


    def update_record(self, table, address):
        self.conn.execute("INSERT INTO {} WHERE self.conn.name = {}", address)
        pass

    def delete_record(self, table, address):
        self.conn.execute("DROP FROM TABLE {} WHERE self.conn.name = {}", address)
        pass

