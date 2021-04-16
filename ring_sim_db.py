import sqlite3

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

    def create_record(self, address):
        """Pass in paramater of type Address class instance."""
        values = address.get_complete_address()
        query = '''INSERT INTO ADDRESS 
                    (symbol_1, symbol_2, symbol_3, symbol_4, symbol_5, symbol_6, symbol_7) 
                    VALUES(?,?,?,?,?,?,?);'''
        self.cursor.execute(query,values)
        self.conn.commit()

    def read_record_ID(self, address_ID):
        """Pass in integer for address ID."""
        query = f"SELECT * FROM ADDRESS WHERE ID = '{address_ID}'"

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchone()

        self.conn.commit()

        return db_address

    def read_record_home(self, home):
        """Pass in home symbol to return all records with that as home."""
        query = f"SELECT * FROM ADDRESS WHERE symbol_7 = '{home}'"

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchall()

        self.conn.commit()

        return db_address

    def read_all(self):
        query = "SELECT * FROM ADDRESS"

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchall()

        self.conn.commit()

        return db_address
        
    def address_exists(self, address):
        """Pass in paramater of type Address class instance."""
        values = address.get_complete_address()
        does_exist = False

        query = "SELECT * FROM ADDRESS WHERE"
        where = f''' symbol_1 = '{values[0]}' AND symbol_2 = '{values[1]}' AND symbol_3 = '{values[2]}' 
                    AND symbol_4 = '{values[3]}' AND symbol_5 = '{values[4]}' AND symbol_6 = '{values[5]}' 
                    AND symbol_7 = '{values[6]}';''' 
 
        query = query + where

        db_address = self.cursor.execute(query)
        db_address = db_address.fetchone()

        if(db_address == values):
            does_exist = True

        self.conn.commit()

        return does_exist

    def address_ID_exists(self, address_ID):
        """Pass in integer for address ID."""
        does_exist = False

        query = f"SELECT * FROM ADDRESS WHERE id = '{address_ID}'"

        db_address_ID = self.cursor.execute(query)
        db_address_ID = db_address_ID.fetchone()

        if(db_address_ID != None):
            if(db_address_ID[-1] == address_ID):
                does_exist = True

        self.conn.commit()

        return does_exist

    def delete_record_ID(self, address_ID):
        """Pass in an integeter value that is address id """
        self.conn.execute(f"DELETE FROM ADDRESS WHERE id = '{address_ID}'")
        self.conn.commit()


    def delete_record_address(self, address):
        """Pass in address object to find"""
        self.conn.execute(f"DELETE FROM ADDRESS WHERE SYMBOL_7 = '{address[6]}' AND id = '{address[-1]}'")
        self.conn.commit()
        
    def update_record(self, address):
        values = address.get_complete_address() 
        """Pass in address object to change addressed based on id"""
        self.conn.execute(f'''UPDATE ADDRESS SET symbol_1 = '{values[0]}', symbol_2 = '{values[1]}', symbol_3 = '{values[2]}',  
                                symbol_4 = '{values[3]}', symbol_5 = '{values[4]}', symbol_6 = '{values[5]}', symbol_7 = '{values[6]}' 
                                WHERE id = '{values[-1]}' ''')
        self.conn.commit()
        

    def close_db(self):
        self.conn.close()

