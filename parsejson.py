import sys,json

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

print str(data["data"][str(sys.argv[2])])

