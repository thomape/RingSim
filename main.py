# Main file for the RingSim app
import sqlite3
from Database import ring_sim_db
from ring_sim_classes import Address, AddressBook, Ring



#def test_db():

# table creation
#conn = sqlite3.connect('test.db')


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
# cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
# for row in cursor:
#     print ("ID = ", row[0])
#     print ("NAME = ", row[1])
#     print ("ADDRESS = ", row[2])
#     print ("SALARY = ", row[3], "\n")

#     print ("Operation done successfully")




#conn.close()




if __name__ == "__main__":

    earth = Address(('sol','vega','siruis', 'betelgeuse', 'polaris', 'mira','alpha centauri A'))
    earth.print_home()

    third = earth.get_digit(3)
    print(third)

    earth.print_address()

    ring = Ring('A')
    print(ring.get_symbol_set())

    #ring.set_home_symbol('a')
    #print(ring.get_symbol_set())

    conn = ring_sim_db.DBConnection()
    print(type(conn))

    conn.connect()










