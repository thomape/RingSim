import sqlite3
from sqlite3.dbapi2 import PARSE_COLNAMES

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

    def connect(self):
        try:
            return sqlite3.connect(self.name)
        except sqlite3.Error as e:
            pass


  # write CRUD operations below

    # Record CRUD
    def create_record(self, table):
        self.conn.execute("INSERT INTO {}",table)
        pass

    def read_record(self, table):
        self.conn.execute("SELECT * FROM {}", table)
        pass

    def update_record(self, table, record):
        self.conn.execute("INSERT INTO {} WHERE self.conn.name = {}", table, record)
        pass

    def delete_record(self, table, record):
        self.conn.execute("DROP FROM TABLE {} WHERE self.conn.name = {} ", table, record)
        pass

    # Table CRUD
    def create_table(self, table):
        self.conn()
        pass

    def read_table(self, table):
        pass

    def update_table(self, table):
        # this might need more defining of what type of modification is desired
        pass

    def delete_table(self, table):
        pass

    # Run any custom query that is desired
    def custom_query(self, table):
        pass
