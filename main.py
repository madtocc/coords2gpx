outputFile = open("output.gpx","w")
outputFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
outputFile.write('<gpx version="1.1" creator="madtocc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/0">\n')
inputFile = open ("input.txt", "r")
n = 0
while True:
    line = inputFile.readline()
    if not line:
        break
    splitted = ''.join(line.strip()).split(',')
    outputFile.write('<wpt lat="{0}" lon="{1}">\n'.format(splitted[1], splitted[0]))
    outputFile.write('<name>M{0}</name>\n'.format(str(n)))
    outputFile.write('</wpt>\n')
    n+=1
inputFile.close() 
outputFile.write('</gpx>')
outputFile.close() 