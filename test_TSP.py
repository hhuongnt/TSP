#!/usr/bin/env python
import argparse
from math import pow, sqrt


def take_filename():
    """
    Read commandline and return the argument as filename
    """
    parser = argparse.ArgumentParser(prog='tsp')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    filename = args.filename
    return filename


def get_node_city(filename):
    """
    Read the input file and return 3 values in the data list
    @parameters:
    data[0]: [city name, latitude, longtitude]
    """
    node_data = []
    try:
        content = [line.rstrip('\n').lstrip(' ') for line in open(filename)]
        for line in content:
            splited_line = line.split(',')
            node_data.append(splited_line)
        return node_data
    except FileNotFoundError:
        print ('File not found')


class Node:
    def __init__(self, latitude, longtitude, city_name):
        self.lati = float(latitude)
        self.longti = float(longtitude)
        self.city_name = city_name


class Graph:
    def __init__(self, distance):
        self.distance = distance
        self.list_node = []


    def add_node(node):
        self.list_node.append(node)


    def get_distance(start_city, end_city):
        lati_distance = end_city.lati - start_city.lati
        longti_distance = end_city.longti - start_city.longti
        distance = sqrt(pow(lati_distance,2) + pow(longti_distance,2))
        return distance
