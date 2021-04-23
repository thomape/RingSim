"""All db access"""
import sqlite3
import json

class DBConnAddress():
    """Db access for address functionality"""
    instance = None
    conn = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(DBConnAddress)
            return cls.instance
        return cls.instance

    def __init__(self, db_name='ringsim.db'):
        self.name = db_name
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        """Attempt db connection"""
        try:
            return sqlite3.connect(self.name)
        except sqlite3.Error as error:
            print(error)

    def create_address(self, address):
        """Pass in paramater of type Address class instance."""
        values = address.get_complete_address()
        query = '''INSERT INTO ADDRESS
                    (symbol_1, symbol_2, symbol_3, symbol_4, symbol_5, symbol_6, symbol_7) 
                    VALUES(?,?,?,?,?,?,?);'''
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_address_id(self, address_id):
        """Pass in integer for address ID."""
        query = f"SELECT * FROM ADDRESS WHERE ID = '{address_id}'"

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchone()

        self.conn.commit()

        return db_address

    def read_address_home(self, home):
        """Pass in home symbol to return all records with that as home."""
        query = f"SELECT * FROM ADDRESS WHERE symbol_7 = '{home}'"

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchall()

        self.conn.commit()

        return db_address

    def read_all_address(self):
        """Returns all addresses"""
        query = "SELECT * FROM ADDRESS"

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchall()

        self.conn.commit()

        return db_address

    def update_address(self, address):
        """Pass in address object to change addressed based on id"""
        values = address.get_complete_address()
        self.conn.execute(f'''UPDATE ADDRESS SET symbol_1 = '{values[0]}', symbol_2 = '{values[1]}',
                          symbol_3 = '{values[2]}', symbol_4 = '{values[3]}', symbol_5 = '{values[4]}',
                          symbol_6 = '{values[5]}', symbol_7 = '{values[6]}' 
                          WHERE id = '{values[-1]}' ''')
        self.conn.commit()

    def delete_address_id(self, address_id):
        """Pass in an integeter value that is address id """
        self.conn.execute(f"DELETE FROM ADDRESS WHERE id = '{address_id}'")
        self.conn.commit()

    def delete_address(self, address):
        """Pass in address object to find"""
        self.conn.execute(f"DELETE FROM ADDRESS WHERE SYMBOL_7 = \
                          '{address[6]}' AND id = '{address[-1]}'")
        self.conn.commit()

    def address_exists(self, address):
        """Pass in paramater of type Address class instance."""
        values = address.get_complete_address()
        does_exist = False

        query = "SELECT * FROM ADDRESS WHERE"
        where = f''' symbol_1 = '{values[0]}' AND symbol_2 = '{values[1]}' AND
                symbol_3 = '{values[2]}' AND symbol_4 = '{values[3]}' AND symbol_5 = '{values[4]}'
                AND symbol_6 = '{values[5]}' AND symbol_7 = '{values[6]}';'''

        query = query + where

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchone()

        if db_address == values:
            does_exist = True

        self.conn.commit()

        return does_exist

    def address_id_exists(self, address_id):
        """Pass in integer for address ID."""
        does_exist = False

        query = f"SELECT * FROM ADDRESS WHERE id = '{address_id}'"

        db_address_id = self.cursor.execute(query)
        db_address_id = db_address_id.fetchone()

        if db_address_id is not None:
            if db_address_id[-1] == address_id:
                does_exist = True

        self.conn.commit()

        return does_exist

    def close_db(self):
        """Closes db connection."""
        self.conn.close()

class DBConnRing():
    """Db access for ring functionality"""
    instance = None
    conn = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(DBConnRing)
            return cls.instance
        return cls.instance

    def __init__(self, db_name='ringsim.db'):
        self.name = db_name
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):

        """Attempt db connection."""
        try:
            return sqlite3.connect(self.name)
        except sqlite3.Error as error:
            print(error)
    
    def create_ring(self, origin):
        """Pass in a tuple"""
        query = '''INSERT INTO rings(origin_key, origin_value)VALUES(?,?);'''

        self.cursor.execute(query, origin)
        self.conn.commit()

    def read_ring(self, origin):
        """Pass in string as origin"""
        query = f"SELECT origin_key, origin_value FROM rings WHERE origin_key = '{origin}';"

        selected_origin = self.cursor.execute(query)
        selected_origin = selected_origin.fetchall()

        self.conn.commit()

        target = dict((key, value) for key, value in selected_origin)
        return target

    def read_all_rings(self):
        """Will return all addresses in db"""
        query = "SELECT * FROM rings"

        db_ring = self.cursor.execute(query)
        db_ring = db_ring.fetchall()

        self.conn.commit()

        return db_ring

    def update_ring(self, origin):
        """Pass in a tuple with current key and new value"""
        query = f"UPDATE rings SET origin_value = '{origin[1]}' WHERE origin_key = '{origin[0]}';"

        self.cursor.execute(query)
        self.conn.commit()

    def delete_ring(self, origin):
        """Pass in string to delete based on key"""
        query = f"DELETE FROM rings WHERE origin_key = {origin};"
        self.cursor.execute(query)
        self.conn.commit()

    def ring_exist(self, origin):
        """Pass in origin string"""
        does_exist = False
        query = f"SELECT * FROM rings WHERE origin_key = '{origin}';"

        ring = self.cursor.execute(query)
        ring = ring.fetchone()

        if ring is not None:
            if ring[0] == origin:
                does_exist = True

        self.conn.commit()

        return does_exist

        
        
    