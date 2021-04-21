"""Main file for the RingSim app"""
import sqlite3
import ring_sim_db
import app_gui
from ring_sim_classes import Address, AddressBook, Ring
import tkinter as tk
import tkinter.font as tkFont

if __name__ == "__main__":
    

    test = ring_sim_db.DBConnRing()

    test.connect()

    maybe = test.read_ring('test_k')
    print(type(maybe))
    print(maybe)

    hi = test.read_all_rings()

    hello = test.ring_exist('test_k')
    print(hello)

    print(hi)

    test.update_ring(("test_k", "hehhsdsadfs"))

    root = tk.Tk()
    app = app_gui.AppGui(root)
    root.mainloop()


