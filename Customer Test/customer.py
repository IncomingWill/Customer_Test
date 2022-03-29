# Title: Customer Class
# Program created by William Schaeffer
# CPS 313
# P. 607, Exercise 3, Customer Test Program
# 03.22.22

# This file will implement the customer subclass of person

# imports for base class

import person

# Customer Class

class Customer(person.Person):

# method for initializing data attributes
    # This initializing function accepts the persons's (customer's base class)
    # name, address, and telephone number as arguments. 
        # It then accepts the Customer's customer number and mailing list (true or false)

    def __init__(self, name, addr, telephone, id, mail_list):
        
        person.Person.__init__(self, name, addr, telephone)         #initialize base class attributes

        self.__customer_number = id                                 #initialize Customer attributes
        self.__mailing_list = mail_list

# mutator methods

    def set_customer_number(self, id):
        self.__customer_number = id

    def set_address(self, mail_list):
        self.__mailing_list = mail_list

# accessor methods
    
    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_address(self):
        return self.__mailing_list

# additional methods

    # display object state
    
    def __str__(self):
        return f'Name: {self.get_name()}\nAddress: {self.get_address()}\nTelephone: {self.get_telephone_number()}\
        \nCustomer Number: {self.__customer_number}\nMailing List: {self.__mailing_list}\n'
