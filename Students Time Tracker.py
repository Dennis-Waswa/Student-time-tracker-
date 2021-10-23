# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:22:14 2020

@author: Dennis Waswa
"""

course_file = open('courses.txt', 'a') #creates an empty text file and open with append to add data 


def sum_Seconds(): #calculate total time in seconds for all courses
    import re

    output = [] #empty list for appending time spend per course 
    with open('courses.txt') as f: #open textfile for 
        for line in f: #loop through lines in the text file 
            match = re.search(r'\d+.?\d*', line) #find digits in each line
            if match:
                output.append(float(match.group())) #append matched digits to the output list 

    return sum(output) #return the sum of all digits/seconds in the output list 


def count_line(): #function for counting the number of lines in the textfile 
    file = open("courses.txt", "r") #to count the lines, open text file in read mode
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"] #remove the spaces at the end of each line
    line_count = len(nonempty_lines) #count all lines
    file.close() #close file 

    return line_count #return number of lines in the text file 


def total_hours(): #convert seconds to hours 
    x = sum_Seconds() #call first function which has sum in seconds and assign to variable x
    hours = x / 3600 #convert seconds to hours 
    return round(hours, 2) #return hours rounded off to two decimal points


def welcome_screen():#message when the student logs in 
    print("Welcome !")
    print(f"You have spent a total of {total_hours()} hours in learning")
    print(f"There are {count_line()} lines in of study-data in your log file")


welcome_screen() #prints the welcome message plus total hours spend on courses and the number of lines in the textfile 


def add_content(s, d): #add content into the file, s for subject and d for time duration 
    
    course_file.write(s + ' ' + d + '\n') #join subject and time duration and divide inputs to lines using \n
    print("OK, added to log") 


def display_c(dis): #for last transaction and total time spend per course 
    if isinstance(dis, int): #checks for intergers in lines
        file = open("courses.txt") #open textfile 
        lines = file.readlines() #display all lines in the file 
        last_lines = lines[-dis:] #diplay the last line in the textfile 
        x = last_lines[::-1] #check lines of the textfile from the back because of not knowin how long the line is 
        for item in x: #loop through lines 
            print(item) #print all items in line
    elif isinstance(dis, str): #condition to return strin if not digit  
        x = dis #assign display to variable x 
        f = open('courses.txt') #open textfile to loop through lines 
        for line in f: #loop through each line in textfile 
            if x in line: #extract digits from lines
                z = int(line[line.find(x) + len(x):]) #finds digits in line for each course. digits are the time 
                hours = round((z / 3600), 2) #calculates time spend per course inn hours 
                print(f"Total time spent for {dis} is {hours} hours")


def bye(): #lets user know the file has been save 
    message = "Saved status to courses.txt! \nBye!"
    print(message)


while True: #infinite while loop for passing different conditions for input 
    command = input().split() #user input is split from command, subject, duration 
    if 'quit' in command: #If user command is quit, the programm quits and saves students input
        bye() #lets the student know file has been save and closed
        break

    elif 'add' in command: #add command expects student to add course and duration 
        add_content(command[1], command[2])

    elif 'display' in command: #displays the time spend per course 
        display_c(command[1])
    else:
        print("Command does not exist!") #returned if nonexisting command is passed 

course_file.close()

