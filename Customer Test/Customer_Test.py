# Title: Customer Test Program
# Program created by William Schaeffer
# CPS 313
# P. 607, Exercise 3, Customer Test Program
# 03.22.22

# This program will test the person class and its customer subclass

# import for class

import person
import customer

# Main Function

def main():
   
    person_1 = person.Person('William Schaeffer', '1403 Lincoln Ave', '608.515.0533')

    customer_1 = customer.Customer('Susan Meyers', '1234 Cherry St', '920.555.1122', '1111', True)
    customer_2 = customer.Customer('Mark Jones', '2345 Acorn Ln', '414.333.2211', 2222, False)
    customer_3 = customer.Customer('Joy Rogers', '3456 Sunny Cir', '262.444.3311', 3333, False)

    customer_list = [customer_1, customer_2, customer_3]

    print('This is a person from the person class: ')
    print()
    print(person_1)

    print('Here are the customers from the customer class: ')
    print()

    for c in range(len(customer_list)):
        print(f'Customer {c + 1}:')
        print(customer_list[c])
        print()

if __name__ == '__main__':
    main()                                                      # call main function


