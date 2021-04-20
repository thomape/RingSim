"""All Classes for RingSim"""

class Address():
    """Base address class"""

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

    # Getters and Setters
    def get_complete_address(self):
        """Returns complete address"""
        return self.complete_address

    def get_home(self):
        """The home symbol is know as the last of 7 symbols."""
        return self.complete_address[6]

    def get_digit(self, position):
        """Pass in integer to return specific location of symbol."""
        return self.complete_address[position - 1]

    def get_address_id(self):
        """Returns id of address"""
        return self.complete_address[-1]

    def set_complete_address(self, complete_address):
        """Pass in tuple to create new address."""
        self.complete_address = complete_address

    # Basic methods
    def print_address(self):
        """Prints address"""
        print(self.complete_address)

    def print_home(self):
        """Prints home symbol"""
        print(self.complete_address[6])

class AddressBook(Address):
    """Inherits from address"""
    # This will only be used if you want to manipulate multiple address for an
    # instance of the app. It can be used like a local db instead of querying the db frequently
    # will implement last, not sure if needed.

class Ring():
    """Base class for Ring object"""
    __symbol_set = {"base" : ("Es", "Cla", "Shi", "O", "UL", "Wex",
                              "Fin", "Pi", "Sa", "Zi", "Tar", "Desh",
                              "Cor", "Jyn", "Ra", "Nas", "Han", "Rey",
                              "Jo", "Jav", "Vel", "En", "Kech", "Bo",
                              "Ste", "Va", "Ta", "Bre", "Rush", "Yar",
                              "De", "Ka", "Pro", "The", "Gil", "Les", "Mu")}

    def __init__(self, origin):
        if origin is None:
            self.origin = {}
        else:
            self.origin = origin
            self.__symbol_set.update(origin)

    def get_base_symbol_set(self):
        """Returns the base symbols"""
        return self.__symbol_set["base"]

    # Get/Set for Point of Origin
    def get_origin(self):
        """Returns the origin dict"""
        return self.origin

    def set_origin(self, origin):
        """Pass in dictionary with "origin" key and string name"""
        self.origin = origin
        self.__symbol_set.update(origin)

    # Get/Set for complete set
    def get_complete_set(self):
        """Returns the entire set"""
        return self.__symbol_set
   