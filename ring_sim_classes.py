# All classes for Ring Sim

class Address():

    address_length : int

    def __init__(self, complete_address):
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
        """The home symbol is know as the last of 7 symbols."""
        return self.complete_address[6]

    def get_digit(self, position):
        """Pass in integer to return specific location of symbol."""
        return self.complete_address[position - 1]

    def get_address_length(self,address):
        pass

    def get_address_ID(self):
        return self.complete_address[-1]
 
    def set_complete_address(self, complete_address):
        """Pass in tuple to create new address."""
        self.complete_address = complete_address

    # Basic methods
    def print_address(self):
        print(self.complete_address)

    def print_home(self):
        print(self.complete_address[6])

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