# Main file for the RingSim app
import sqlite3
import ring_sim_db
from ring_sim_classes import Address, AddressBook, Ring


if __name__ == "__main__":

    earth = Address(('sol','vega','siruis', 'betelgeuse', 'polaris', 'mira','alpha centauri A'))
    earth.print_home()

    #third = earth.get_digit(3)
    #print(third)

    earth.print_address()

    ring = Ring('A')
    print(ring.get_symbol_set())

    #ring.set_home_symbol('a')
    #print(ring.get_symbol_set())

    conn = ring_sim_db.DBConnection()
    conn.connect()

    try:
        conn.create_record(earth)
    except:
        print("Failed to create a new record")
    

    # this is returning a cursor object that sqlite creates
    # there needs to be a way to match it to an Address object
    # hello = Address(('hello','vega','siruis', 'betelgeuse', 'polaris', 'mira','alpha centauri A'))
    # world = Address(('world','vega','siruis', 'betelgeuse', 'polaris', 'mira','alpha centauri A'))
    # dude = Address(('dude','vega','siruis', 'betelgeuse', 'polaris', 'mira','alpha centauri A'))

    # places = [hello, world, dude]

    # for place in places:
    #     conn.create_record(place)

    test2 = conn.read_record_home('alpha centauri A')
    for x in test2:
        print(x)








