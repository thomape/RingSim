# All classes for Ring Sim

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

    def __init__(self, home_symbol):
        self.home_symbol = home_symbol

    def get_home_symbol(self):
        return self.home_symbol
    
    def get_symbol_set(self):
        #return self.symbol_sets[self.home_symbol]
        pass

    def add_symbol_set(self):
        pass

    def del_symbol_set(self):
        pass