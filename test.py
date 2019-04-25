def readfile(filename):
    """
    Read the input file and return 3 values in the data list
    @parameters:
    data[0]: city name
    data[1]: latitude
    data[2]: longtitude
    """
    data = []
    content = [line.rstrip('\n').lstrip(' ') for line in open(filename)]
    for line in content:
        splited_line = line.split(',')
        data.append(splited_line)
    return data

data = readfile('vietnam_cities.csv.json')
print (data[1])
