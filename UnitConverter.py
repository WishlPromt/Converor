import json
import os
import pyperclip
import time as timelib


with open('units_convert.json') as file:
    data = json.load(file)

with open('time_zones_converter.json') as file:
    data_time = json.load(file)


last_convert = ''


def unit_converter(value, first_unit, second_unit):

    try:
        value = float(value)
        return value * data[first_unit][second_unit]
    except:
        return 'Program can\'t convert this'


def time_converter(time, f_time_zone, s_time_zone):

    time = time.split(':')

    try:
        converted_time = str(int(time[0]) + data_time[f_time_zone][s_time_zone]) + ':' + time[1]
        return converted_time

    except:
        return('Program can\'t convert this')



def commands(command):
    if command == 'clr':
        os.system('cls' if os.name == 'nt' else 'clear')
        return None

    elif command == 'c':
        pyperclip.copy(last_convert)
        return 'Unit was copied'

    elif command == 'q':
        quit()
        return None


def input_command():
    global last_convert

    command = input()
    commands_list = []


    for item in command.split(' '): commands_list.append(item)


    if 3 > len(commands_list) >= 1 and commands_list[0] != 'cur':
        for command in commands_list:
            output = commands(command)
            if output != None:
                print(output)


    elif len(commands_list) == 3 and commands_list[0].find(':') == -1:
        result = unit_converter(commands_list[0], commands_list[1], commands_list[2])
        last_convert = str(result)
        print(result)

    elif len(commands_list) == 3 and commands_list[0].find(':') != -1:
        result = time_converter(commands_list[0], commands_list[1], commands_list[2])
        last_convert = result
        print(result)

    elif len(commands_list) == 2 and commands_list[0] == 'cur':
        s_time =timelib.gmtime()[4]
        if s_time < 10:
            s_time = '0'+ str(s_time)
            print(s_time)
        result = time_converter(str(timelib.gmtime()[3] + 5) + ':' + str(s_time), 'ekb', commands_list[1])
        last_convert = result
        print(result)

    else:
        print('Ты долбаеб')

    input_command()

input_command()
