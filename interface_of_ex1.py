# this shows how to import modules 
'''
import modules_ex1
modules_ex1.greeting()
print(modules_ex1.read_student_data(2))
'''
'''
import modules_ex1 as em
em.greeting()
'''

# from modules_ex1 import greeting,read_student_data
from modules_ex1 import *
greeting()
print(read_student_data(2))
print(calculate_expenses(2))
