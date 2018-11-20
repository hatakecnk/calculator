#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Mau Ngapain Liat-liat? Recode? Gak Berkah Hidup Lu
#• * = kali
#• + = tambah
#• / = bagi
#• % = Persen
#• e : 2.718281...
#• pi : 3.141592...
#• sine : sin(rad)
#• cosine : cos(rad)
#• tangent : tan(rad)
#• remainder : XmodY
#• square root : sqrt(n)

import math
import sys
import os


def calc(term):
    # This part is for reading and converting arithmetic terms.
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e'] 

    # This part is for reading and converting function expressions.
    term = term.lower()
    
    for function in functions:            
        if function in term:
            withmath = 'math.' + function
            term = term.replace(function, withmath)

    try:

        # here goes the actual evaluating.
        term = eval(term)

    # here goes to the error cases.
    except ZeroDivisionError:

        print("Can't divide by 0.  Please try again.")

    except NameError:

        print('Invalid input.  Please try again')

    except AttributeError:

        print('Please check usage method and try again.')
        
    return term


def result(term):
    """
        input:  term of type str
        output: none
        purpose: passes the argument to the function calc(...) and 
                prints the result onto console.
    """
    print("\n" + str(calc(term)))


def main():
    """
        main-program
        purpose: handles user input and prints 
                 information to the console.
    """
os.system("clear")
os.system("figlet xNot_Found | lolcat")
os.system("echo Calculator Simple by xNot_Found | lolcat")
print ("""\033[1;31;1mType quit To Exit Tool""")

if sys.version_info.major >= 3:
        while True:
            k = input("\nInput your command: ")
            if k == 'quit':
                break
            result(k)

else:
        while True:
            k = raw_input("\nInput your command: ")
            if k == 'quit':
                break
            result(k)


if __name__ == '__main__':
    main()
    os.system("figlet See You | lolcat")