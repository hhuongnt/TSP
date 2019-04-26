import argparse


def take_filename(cmd_line):
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
    data[0]: city name
    data[1]: latitude
    data[2]: longtitude
    """
    data = []
    try:
        content = [line.rstrip('\n').lstrip(' ') for line in open(filename)]
        for line in content:
            splited_line = line.split(',')
            data.append(splited_line)
        return data
    except FileNotFound():
        print ('File not found')


data = readfile('vietnam_cities.csv.json')
print (data[1])
