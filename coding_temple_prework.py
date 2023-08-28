# Question 1
## Write a function to print "hello_USERNAME!"

def greeting(name):
    print(f'Hello_{name.title()}!')


# Question 2
## Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for n in range(1,100,2):
        print(n)


# Question 3
## Please write a Python function, max_num_in_list to return the max number of a given list

def max_num_in_list(list):
    asc_list = sorted(list)
    return asc_list[-1]


# Question 4
## Write a function to return if the given year is a leap year

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


# Question 5
## Write a function to check to see if all numbers in list are consecutive numbers.

def is_consecutive(a_list):
    x = 0
    y = 1
    end = len(a_list)
    for num in a_list:
        while y < end:
            if a_list[x]+1 == a_list[y]:
                x += 1
                y += 1
            else:
                return False
    return True