# Main file for the RingSim app
import sqlite3

class Address():

    address_length : int

    def __init__(self, complete_address) -> None:
        is_empty = False

        if complete_address == ():
            is_empty = True


        if is_empty:
            self.home = None
            self.complete_address = ()
        else:
            self.home = complete_address[len(complete_address) - 1]
            self.complete_address = complete_address

        self.address_length = (len(self.complete_address) - 1)
    
    # Getters and Setters
    def get_complete_address(self):
        return self.complete_address
    
    def get_home(self):
        return self.complete_address[self.address_length]

    def get_digit(self, position):
        return self.complete_address[position - 1]
 
    def set_complete_address(self, complete_address):
        self.complete_address = complete_address
    
    def set_home(self, home):
        self.complete_address[self.address_length] = home

    # Basic methods
    def print_address(self):
        print(self.complete_address)

    def print_home(self):
        print(self.complete_address[self.address_length])

class AddressBook(Address):
    # This class will be a collection of all entered address

    # Functions include
    # Adding address
    # Deleting address
    # Read entire book
    # This would need to be backedup in a Db

    pass

class Ring():

    symbol_sets = {'A' : ('A','B','C'), 
                    'a' : ('a','b','c'),
                    '1' : ('1','2','3'),
                    '1#' : (1,2,3)}

    def __init__(self, home_symbol) -> None:
        self.home_symbol = home_symbol

    def get_home_symbol(self):
        return self.home_symbol
    
    def get_symbol_set(self):
        #return self.symbol_sets[self.home_symbol]
        pass

    def add_symbol_set():
        pass

    def del_symbol_set():
        pass



def test_db():
    
    # table creation
    conn = sqlite3.connect('test.db')


    # conn.execute('''CREATE TABLE COMPANY
    #      (ID INT PRIMARY KEY     NOT NULL,
    #      NAME           TEXT    NOT NULL,
    #      AGE            INT     NOT NULL,
    #      ADDRESS        CHAR(50),
    #      SALARY         REAL);''')

    
    # Insert operatiom

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #     VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #     VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #     VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #     VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    # conn.commit()
    # print ("Records created successfully")


    #select operation
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ADDRESS = ", row[2])
        print ("SALARY = ", row[3], "\n")

        print ("Operation done successfully")




    conn.close()




if __name__ == "__main__":

    earth = Address(('sol','vega','siruis', 'betelgeuse', 'polaris', 'mira','alpha centuri A'))
    earth.print_home()

    third = earth.get_digit(3)
    print(third)

    earth.print_address()

    ring = Ring('A')
    print(ring.get_symbol_set())

    #ring.set_home_symbol('a')
    #print(ring.get_symbol_set())

    test_db()

#test   


    

    
    

