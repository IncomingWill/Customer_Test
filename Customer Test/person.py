# Title: Person Class
# Program created by William Schaeffer
# CPS 313
# P. 607, Exercise 3, Customer Test Program
# 03.22.22

# This file will implement the person class

# imports

# Person Class

class Person:

# method for initializing data attributes
    # This initializing function accepts the person's 
    # name, address, and telephone number as arguments. 

    def __init__(self, name, addr, telephone):
        self.__name = name
        self.__address = addr
        self.__telephone_number = telephone

# mutator methods

    def set_name(self, name):
        self.__name = name

    def set_address(self, addr):
        self.__address = addr

    def set_telephone_number(self, telephone):
        self.__telephone_number = telephone

# accessor methods
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone_number(self):
        return self.__telephone_number

# additional methods

    # display object state
    
    def __str__(self):
        return f'Name: {self.__name}\nAddress: {self.__address}\nTelephone Number: {self.__telephone_number}\n'
