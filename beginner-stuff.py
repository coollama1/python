
#python allows you to import "modules", which are similar to libraries
import random
import sys
import os

print(' - 1 - \n')
first_name = "Derek"
last_name = "Smokeballs"
print(first_name, last_name)
# - python funfact #1: print() adds a new line after each call
# - python funfact #2: python adds spaces automatically after each
#   segment of the print statement (print(a ,b) - space is printed
#   aoutomatically after a)

print('\n - 2 - \n')

#cool math stuff
print("I can't believe you  can actually do this with python: 4^3 =", 4**3)
print("More amazing python technology: 36%19 =",36%19 )
print("Momy, look what python can do: 5/4 = ", 5/4, ",BUT, 5//4 =", 5//4)
print("Apparantly order matters?: 5 + 6 * 7 = ", 5+6*7, "BUT, (5 + 6) * 7 =", (5+6)*7)
quote = 'this is still a weird way of declaring strings'
print(quote, "using the power of backlash to prevent errors\/ ")

print('\n - 3 - \n')

multi_line_opness = '''why
is this even possible????'''
print(quote + multi_line_opness)

print('\n - 4 - \n')

#fancy c-style printing
#allows more control over printing (printing without automatic spacing)
print("%s%s%s" %('experimenting with python is so much fun\n', quote + "\n", multi_line_opness))

print('\n - 5 - \n')

#one way of printing without automatic newlines
print('whatever you\'re trying to print', end ="")
print()

print('\n - 6 - \n')

#python allows you to perform multiplication on strings
print("multiplying strings is cool\n" * 5)
random_multiplication_string = "multiplying strings is fun\n" * 5
print(random_multiplication_string)

print('\n - 7 - \n')

# LISTS AND STUFF ABOUT LISTS

#creating lists (like common lisp)
magic_list_of_things = ['Juicy Juice', 'Ripe Tomatoes', 'Long Bannanas',
                         'More Juicy Juice']

#calling items in the list is smilar to calling an item of an array in other
#languages
print(magic_list_of_things[0], "is better than", magic_list_of_things[3])

print('\n - 8 - \n')

#chaning values in a list
magic_list_of_things[2] = "Super Long Bannana"
print("Is it a long bannana?\nNo it's a", magic_list_of_things[2])

print('\n - 9 - \n')

#printing a range within a list
#list_name[from_index:to_index] - prints elements between from_index - to_index
#exluding the element at the to_index (to print final element, 
#set to_index = final_element_index + 1) <- (+anything greater than 1 also works)
print("%s%s" % ("Tell me your secret baby\n", magic_list_of_things[0:4]))

print('\n - 10 - \n')

#python list range can be stored in a string
part_of_the_magic_list = magic_list_of_things[1:3]
print(part_of_the_magic_list)

print('\n - 11 - \n')

#lists can also be stored in other lists
things_you_should_probably_do = [magic_list_of_things, 'do the dishes', 'get a life']
print(things_you_should_probably_do[0:3])

print('\n - 12 - \n')

#retrieving data from a 2-dimensional list (a list within a list)
#name_of_list = [first_list, second_list, third_list]
#name_of_list[1][2] - gives the 3rd element (at position [2]) of second_list
print("%s%s" % ("What do I need again?\n", things_you_should_probably_do[0][3]))

special_string = things_you_should_probably_do[0][2]
print("Yea daddy, give me that", special_string)
print(things_you_should_probably_do[0][0])

print('\n - 13 - \n')

#appending - adding items to the end of a list
things_you_should_probably_do.append('doubt your existence')
print(things_you_should_probably_do[0:4])

print('\n - 14 - \n')

#inserting an element into a specific index within the list
#name_of_list.insert(index, element)
things_you_should_probably_do.insert(0, 'become a pornstar')
print(things_you_should_probably_do[0:5])

print('\n - 15 - \n')

#remove - removes only one occurence of the element provided
#name_of_list.remove(x) - removes the first copy of (x) from name_of_list
#side-note: printing beyond list range doesn't cause an error (as in the
#example below)
new_list = ['Apples', 'Oranges', 'Oranges', 'Pears']
new_list.remove('Oranges')
print(new_list[0:4])

print('\n - 16 - \n')

#above side-note applies to string declaration as well
testing_this_weird_property = new_list[0:4]
print(testing_this_weird_property)

print('\n - 17 - \n')

#del - deleting an element at a specific index
del new_list[0]
print(new_list[0:2])

print('\n - 18 - \n')

#if list A is contained within list B, making changes to A will also cause
#changes to happen to B
list_a = ['super', 'bunny', 'ultra',   'time']
list_b = ['random', 'words', 'that', 'don\'t', 'make', 'sense']
list_c = [list_a, list_b]
print(list_c[0:2])
list_a.append('power')
list_a.remove('super')
del list_b[4]
list_b.append('make')
print(list_c[0:2])
#should print out: [['bunny', 'ultra', 'time', 'power'], ['random','words',
#'that', 'don't', 'sense', 'make']]
#important note - changes to list_a and list_b affect list_c

print('\n - 19 - \n')

#the above property does NOT apply to string/list concatenation
first_string = "how do you do? "
second_string = "well, I do just fine"
third_string = first_string + second_string
print(third_string)
first_string = "how do you do on this lovely day? "
print(third_string)

print('\n - 20 - \n')

#sort- arranges the elements within the list in ascending order (assuming all
#of the elements are of the same type)
#numbers are sorted by their values, strings/chars are sorted by their ascii
#values 
another_new_list = ['One thing', 'Another thing', 'More things']
print(another_new_list[0:3])
another_new_list.sort()
print(another_new_list) #this is apparantly an acceptable printing format
cool_list = [7,8,9,3,4,2.1,2,1]
print(cool_list)
cool_list.sort()
print(cool_list)
more_cool_things = ['A', 'Z', 'W', 'X', '\n', ' ',] #records '\n' as '\n' not
                                                    #a new line

print('\n - 21 - \n')

#name_of_list.reverse() - reverses the elements of name_of_list
more_cool_things.reverse()
print(more_cool_things)
more_cool_things.sort()
more_cool_things.reverse()
print(more_cool_things)

print('\n - 22 - \n')

#lists can be concatenated like strings
special_list = [1,2,3,4]
other_special_list = [5,7,3,1,2,-14]
more_specialness = special_list + other_special_list
print(more_specialness)
more_specialness.sort()
print(more_specialness)
more_specialness.remove(1)
print(more_specialness)
special_list.append(17)
print(more_specialness) #showing that the list domino effect does not apply to
                        #to concatenation(or string concat. as stated earlier)

print('\n - 23 - \n')

#finding the length of a list
special_list.remove(17) #reverting the lists back to its original size
more_specialness.insert(1,1)
print("Checking to see that math still works:",len(special_list),"+", \
len(other_special_list), "=", len(special_list) + len(other_special_list),\
"=", len(more_specialness))

print('\n - 24 - \n')

#max and min values can be retrieved from lists
print(more_specialness)
print("Min Value:", min(more_specialness))
print("Max Value:", max(more_specialness))

print('\n - 25 - \n')

#TUPLES AND TUPLE STUFF(surprisingly short)

#tupless are like lists, except they cannot be changed
sexy_tuple = (1,7,3,4,2,0)
print("Sexy Tuple:", sexy_tuple)
print(sexy_tuple[0:4])

print('\n - 26 - \n')

#converting list to tuple and tuple to lists (kind of useless)
sexy_list = list(sexy_tuple)
new_sexy_tuple = tuple(sexy_list)
print("Sexy List:", sexy_list, "\nSexy Tuple:", new_sexy_tuple)

print('\n - 27 - \n')

#length of a tuple (same as a list), so do min and max
print("Length of Sexy Tuple:", len(sexy_tuple))
print("Max of Sexy Tuple:", max(sexy_tuple), "\nMin of Sexy Tuple:",\
min(sexy_tuple))

print('\n - 28 - \n')

#tuple concatenation
super_new_sexy_tuple = sexy_tuple + new_sexy_tuple
print(super_new_sexy_tuple)

print('\n - 29 - \n')

#MAPS AND MAP STUFF

#maps (or dictionaries) declares a value with a unique key for each value
#similar to c++, maps are like an array/vector/list in which the indeces
#don't have to be numbers
family_nickname = {'Father' : 'King Douche', 'Mother' : 'Domestic Servant',
                    'Younger Brother' : 'Dork', 
                    'Olrder Brother' : 'Heavily In-Debt'}
print("My father is often referred to as", family_nickname['Father'])
print("My mother is unfortunately known as the", family_nickname['Mother'])

print('\n - 30 - \n')

#changing the values within the map
family_nickname['Father'] = "King Douche III"
print("Correction, my father is actually refered to as", \
       family_nickname['Father'])

print('\n - 31 - \n')

#removing/deleting values from the map
del family_nickname['Father']
print(family_nickname)
#print(family_nickname['mother']) - would produce an error b/c mother != Mother
#keys are case sensitive

print('\n - 32 - \n')

#to find the length of a map (number of values)
print("%s%s %s %s" % ("Excluding your dad, how many family members do you have\
again?\n","I have", len(family_nickname), "left"))

print('\n - 33 - \n')

#name_of_map.get(key) seems to work similarly to name_of_map[key]
print(family_nickname['Mother'])
print(family_nickname.get('Mother'))

print('\n - 34 - \n')

#retrieving a list of dictionary values/keys
print(family_nickname.keys())
print(family_nickname.values())

print('\n - 35 - \n')

#adding new values to maps
print("Family members before:",len(family_nickname))
family_nickname['Father'] = 'Lord Douche'
print(family_nickname)
print("Family members after:", len(family_nickname))