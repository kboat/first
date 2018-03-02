#!/usr/bin/python3

'''
    addStudent.py - Add student to a gradebook of check for their averages.
    Created by: Emmanuel Boateng
    Created on: 20171129
    Changes:
        20171129 - Added input, lists, and dictionaries.
        20171129 - Added if statements and comments.
'''

students = {

}

add_name = input('Do you want to add a student? (y/n/q): ')

add_name = add_name.title()

if add_name == 'Y':
    name1 = input("Please enter the student's name: ")
    print('Adding ...')
    grade = [input("Please enter the student's grades. i.e(100, 30, 55, 79)")]
    students[name1] = grade
    print('Successfully added ' + name1.title() + ' to the gradebook')

elif add_name == 'N':
    ans = input('Would you like to check the average of a student? (y/n): ')
    ans = ans.title()
    if ans == 'Y':
        names = input("Please enter the student's name: ")
        names = names.title()
        chk = []
        for name in students.keys():
            chk.append(name)

        if names in chk:
            per = students[names]
            avg1 = sum(per)
            avg2 = len(per)
            o_avg = avg1 / avg2
            print(names.title() + ', the average of your test scores are: ' + str(o_avg))
elif add_name == 'Q':
    quit
