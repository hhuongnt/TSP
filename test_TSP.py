#!/usr/bin/env python
import argparse


def take_filename():
    """
    Read commandline and return the argument as filename
    """
    parser = argparse.ArgumentParser(prog='tsp')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    filename = args.filename
    return filename


def readfile(filename):
    """
    Read the input file and return 3 values in the data list
    @parameters:
    data[0]: [city name, latitude, longtitude]
    """
    data = []
    try:
        content = [line.rstrip('\n').lstrip(' ') for line in open(filename)]
        for line in content:
            splited_line = line.split(',')
            data.append(splited_line)
        return data
    except FileNotFoundError:
        print ('File not found')


print (take_filename())
