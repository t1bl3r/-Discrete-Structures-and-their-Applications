# CS220 - Programming Assignment 1 : Boolean Logic
# author - Asa Ben-Hur and Nirmal Prajapati

# NOTE:
# You must use small single letters for your variable names, for eg. a, b, c
# You may use parenthesis to group your expressions such as 'a and (b or c)'

# Implement the following four functions:
# truth_table, count_satisfying, is_tautology and are_equivalent

# Submission:
# Submit this file using the checkin system on the course web page.



######## Do not modify the following block of code ########
# ********************** BEGIN *******************************

from functools import partial
import re


class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q) :
    return not p or q

@Infix
def iff(p, q) :
    return (p |implies| q) and (q |implies| p)


# You must use this function to extract variables
# This function takes an expression as input and returns a sorted list of variables
# Do NOT modify this function
def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

# *********************** END ***************************




############## IMPLEMENT THE FOLLOWING FUNCTIONS  ##############
############## Do not modify function definitions ##############


# This function calculates a truth table for a given expression
# input: expression
# output: truth table as a list of lists
# You must use extract_variables function to generate the list of variables from expression
# return a list of lists for this function
def truth_table(expression):
    variables = extract_variables(expression)
    rows = 2 ** len(variables)
    width = len(variables)
    list1 = list()
    for ii in range(rows):
      current = bin(ii)[2:].zfill(width)
      thisList = list()
      for letter in str(current):
         if letter == '1':
           letter = 'True'
           thisList.append(letter)
         else:
           letter = 'False'
           thisList.append(letter)
      for xx in range(len(variables)):
         exec(variables[xx] + ' = ' + thisList[xx])
     
      thisList.append(eval(expression))
      list1.append(thisList)
      
    for xx in range(rows):
      for ii in range(len(variables)):
        if list1[xx][ii] == 'True':
           list1[xx][ii] = True
        if list1[xx][ii] == 'False':
           list1[xx][ii] = False
      
    return list1[::-1]

# count the number of satisfying values
# input: expression
# output: number of satisfying values in the expression
def count_satisfying(expression):
    list1 = truth_table(expression)
    count = 0
    for xx in range(len(list1)):
       list2 = list1[xx]
       if (list2[len(list2)-1] == True):
         count = count + 1
         
    return count

# if the expression is a tautology return True,
# False otherwise
# input: expression
# output: bool
def is_tautology(expression):
    list1 = truth_table(expression)
    count = 0
    for xx in range(len(list1)):
       list2 = list1[xx]
       if (list2[len(list2)-1] == True):
         count = count + 1
    if (count == len(list1)):
       return True
    return False

# if expr1 is equivalent to expr2 return True,
# False otherwise
# input: expression 1 and expression 2
# output: bool
def are_equivalent(expr1, expr2):
    variables1 = extract_variables(expr1)
    variables2 = extract_variables(expr2)
    if (variables1 != variables2):
       return False
    list1 = truth_table(expr1)
    list2 = truth_table(expr2)
    if (list1 != list2):
       return False
    
    return True

