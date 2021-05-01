
#!/usr/bin/python3
import csv, sys

total = len(sys.argv)
cmdargs = str(sys.argv)
# Pharsing args one by one 

print ("INPUT: %s" % str(sys.argv[1]))
print ("OUTPUT: %s" % str(sys.argv[2]))

fname = str(sys.argv[1])
data = csv.reader(open(fname), delimiter = ',')
#Skip the headers 
next(data)
next(data)
#Open the file to be written.
f = open(str(sys.argv[2]), 'w')

#Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Document>\n")
f.write("   <name>" + fname.rsplit( ".", 1 )[ 0 ] + '.kml' +"</name>\n")
for row in data:
    f.write("   <Placemark>\n")
    f.write("       <description>" + str(row[9]) + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + str(row[7]) + "," + str(row[6]) + "," + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")
f.write("</Document>\n")
f.write("</kml>\n")
f.close()
print("File Converted")
