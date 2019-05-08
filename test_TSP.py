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



def get_city_data(filename):
    """
    Read the input file and return 3 values in the data list
    @parameters:
    data[0]: [city name, latitude, longtitude]
    """
    city_data = []
    try:
        content = [line.rstrip('\n').lstrip(' ') for line in open(filename)]
        for line in content:
            splited_line = line.split(', ')
            city_data.append(splited_line)
        return city_data
    except KeyError:
        print ('File not found')


def get_node_cities(dict, city_data):
    for city in city_data:
        node = Node(city[0], city[1], city[2])
        dict.add_node(node)
    return dict


class Node:
    """
    Object have 3 attributes: city_name, latitude, longtitude
    """
    def __init__(self, city_name, latitude, longtitude):
        self.city_name = city_name
        self.latitude = latitude
        self.longtitude = longtitude


class Graph:
    def __init__(self, list_node):
        self.list_node = []


    def add_node(self, node):
        self.list_node.append(node)


    def get_distance(self, node1, node2):
        """
        Get distance between two cities
        @parameters:
        node1: start_city
        node2: end_city
        """
        lati_distance = abs(float(node2.lati) - float(node1.lati))
        longti_distance = abs(float(node2.longti) - float(node1.longti))
        distance = sqrt(pow(lati_distance,2) + pow(longti_distance,2))
        return distance


    def find_path(self, list_node):
        path_of_cities = []
        total_distance = 0
        start_city = node_cities.pop(0)
        while node_cities:
            dictionary_of_cities = {}
            for city in node_cities:
                distance = Graph.get_distance(start_city, city)
                dictionary_of_cities[city] = distance
        return dictionary_of_cities

filename = take_filename()
city_data = get_city_data(filename)
list_node = []
dict = Graph(list_node)
get_node_cities(dict, city_data)
print (dict.list_node)
