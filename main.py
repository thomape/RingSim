"""Main file for the RingSim app"""
import sqlite3
import ring_sim_db
from ring_sim_classes import Address, AddressBook, Ring


if __name__ == "__main__":
    

    test = ring_sim_db.DBConnRing()

    test.connect()

    newkv = {"test_k":"test_v"}
    test.create_ring(newkv)
