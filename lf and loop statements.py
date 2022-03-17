# salary = float(input("Enter salary: "))
# year = int(input("Enter year of service: "))
# bonus_amt = (5/100)*salary
#
# if year > 5:
#     print("You are qualified for a bonus of: ", bonus_amt)
# else:
#     print("You are not qualified for a bonus, sorry: ")



#while loop

# i = 0
# while i < 6:
#     print(i)
#     i+=1


#Python for loops
#A for loop is used for iterating over a sequence (that is either a list, tuple, dictionary, set, or a string)
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#Example
#Print each name in names list:

# names = ("leo", "benedict", "stanley", "oma")
# for name in names:
#     print(name)

#The loop does not require an indexing variable to set a beforehand

#Looping through a string
#Even strings are iterable objects, they contain a sequence of characters:
#Example
#Loop through the letters in the word "stanley"

# for x in "vincent":
#     print(x)

# The break statement
# with the break statement we can stop the loop before it has looped through all the items:
# Example
# Exit the loop when we get to letter "c":

# for x in "vincent":
#     if x == "c":
#         break
#     print(x)

#The continue statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Example

# for x in "vincent":
#     if x == "c":
#         continue
#     print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function
# The range( function returns a seqence of numbers, starting from 0 by default, and increment by 1 (by default), and ends at a specified numbers
# Example
# Using the range() function:

# for x in range(6):
#     print(x)

#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding
#a parameter: range(2, 6), which  means values from 2 to 6 (but not including 6):
#Example
#using the start parameter:

# for x in range(4,6):
#     print(x)

#the range() function defaults to increment the sequence by 1, however it is possible to specify the increment value
#by adding a third parameter. range(2, 30, 3).
#Example
#Increment the sequence with 3(default is 1)

# for x in range(2, 31, 2):
#     print(x)

#Else in the loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
#example

#print all numbers from 0 to 5, and print a message when the loop has ended:

# for x in range(6):
#     print(x)
# else:
#     print("Finally finished")

#Note: The else block will not be excuted if the loop is stopped by a break statement.

# for x in range(6):
#     if x == 4:
#         break
#     print(x)
# else:
#     print("Finally finished")


#Nested Loops
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#example
#print each first group names for every second group names

# first_group_of_names = ["leo", "benedict", "oma", "stanley", "vincent"]
# second_group_of_names = ["jason", "david", "lamido", "patience", "praise"]
# for name in first_group_of_names:
#     for nam in second_group_of_names:
#         print(name, nam)

#another example

# name = input("Please enter your name: ")
# for x in name:
#     if "b" in name.casefold():
#         print("You have b in your name, why?")
#         break
#     else:
#         print("nice job")
#         break


#Task 1: Calculating Century


#attempt 1

#year = int(input("Enter year: "))
# century = year / 100
# cent = year // 100
# if century == cent:
#     print(century)
# elif century > cent:
#     print(cent + 1)

#attempt 2

# year = int(input("Enter year: "))
# century = (year-1) // 100+1
# print(century)

#attempt 3
# year = int(input("Enter year: "))
# def century(year):
#     return (year-1) // 100+1
#
# print(century(year))

#Task 2: Calculating Leap Year

# year = int(input("Enter year: "))
# leap_year = year % 4
# if leap_year == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")






