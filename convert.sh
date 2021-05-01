#!/bin/bash
#I could probbably do this with python but this is EZ
for file in *.csv
do
  python3 ./converter.py "$file" "${file}.kml"
done