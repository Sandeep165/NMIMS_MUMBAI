def cap_last(s):
    new_s = ""
    for i in range(len(s)):
        try:
            if s[i+1] == " ":
                new_s += s[i].upper()
            else:
                new_s += s[i]
        except:
            new_s += s[i].upper()

    print(new_s)

cap_last("Name")
cap_last("My Name is Abegail")
cap_last("This is awesome")


'''
lst = []

for i in str:
    i = i[0:-1]+i[-1].upper()
    lst.append(i)
    " ".join(lst)
'''

'''

Mubashir needs your help to find the Simple Numbers in a given range.

A number X, that has an N amount of digits (which we'll enumerate as d1, d2, ..., dN), is Simple if the following equation holds true:

X = d1^1 + d2^2 + ... + dN^N
Examples of Simple Numbers:
89 = 8^1 + 9^2

135 = 1^1 + 3^2 + 5^3
Create a function which returns a list of all the Simple Numbers that exist within a given range between a and b (both numbers are inclusive).

Generate a list of the individual digits of the number.
Filter the list so that only "simple numbers" are kept.
To find out if a number is "simple":
Take the digits of the number.
For each digit, calculate digit ^ (index_of_the_digit + 1).
Sum the results of the calculations above and compare with the original number. If they're equal, the number is "simple".
Examples
simple_numbers(1, 10) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9]

simple_numbers(1, 100) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

simple_numbers(90, 100) ➞ [ ]




Create a function that takes a list lst of numbers and moves all zeros to the end, preserving the order of the other elements.

Examples
move_zeros([1, 0, 1, 2, 0, 1, 3]) ➞ [1, 1, 2, 1, 3, 0, 0]

move_zeros([0, 1, None, 2, false, 1, 0]) ➞ [1, None, 2, false, 1, 0, 0]

move_zeros(['a', 0, 0, 'b', 'c', 'd', 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ➞ ['a', 'b', 'c', 'd', 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

--------------------------------------------------------------------------------------------------------------------------------------------------------


Given an array of integers lst and an integer n, find out a pair of numbers [x, y] from a given array such that x * y = n .

If the pair is not found, return None.

Examples
simple_pair([1, 2, 3], 3) ➞ [1, 3]

simple_pair([1, 2, 3], 6) ➞ [2, 3]

simple_pair([1, 2, 3], 9) ➞ None



Mubashir is not good in python programming. By mistake, he swapped keys and data values in the dictionary.

Given a dictionary, return a dictionary with the original values and the list of keys. See below example for a better understanding:

Given Dictionary
dict = {
  "Mubashir": "Name",
  "31": "Age",
  "Male": "Sex",
  "Pilot": "Job",
  "Matt": "Name",
  "40": "Age",
  "Programmer": "Job"
}
Modified Dictionary
dict = {
  "Name": ["Mubashir", "Matt"],
  "Age": ["31", "40"],
  "Sex": ["Male"],
  "Job": ["Pilot", "Programmer"]
}
dict.item()

'''