import os
import string

dictionary = {}


def yes_or_no():
    answer = 'maybe'
    while not answer in 'yn':
        answer = input('Yes or No? ')
        answer = answer.lower()
        answer = answer[0]
        if not answer in 'yn':
            print('Choose "yes" or "no" only')
    if answer == 'y':
        return(True)
    else:
        return(False)

def read_file(file):
    with open(file,'r')as instream:
        for line in instream:
            name,number = line.strip().split()
            update_info(name,number)
        
def update_info(name,number):
    global dictionary
    if name in dictionary:
        if number not in dictionary:
            dictionary[name].append(number)
    else:
        dictionary[name] = [number]

def add_phone_number():
    stop = False
    while (not stop):
        print('Do you have some information to add?')
        if yes_or_no():
            person1 = input('What is the person\'s name?')
            number2 = input('What is the person\'s number?')
            update_info(person1,number2)
        else:
            print_personal_info()
            stop = True

def print_personal_info():
    global dictionary
    for name,number in dictionary.items():
        #print(name)
        uni = set(number)
        for number in uni:
            #print(number)

def output_file(file):
    lines = set()
    with open(file,'w')as outstream:
        outstream.write('Name\tNumber\n')
        for name,numbers in dictionary.items():
            for number in numbers:
                outstream.write(f'{name}\t{number}\n')
                
def main(infile,outfile):
    read_file(infile)
    add_phone_number()
    output_file(outfile)
    print_personal_info()
