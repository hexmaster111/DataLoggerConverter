#!/bin/bash
#I could probbably do this with python but this is EZ

cd Input

for file in *.csv
do
  python3 ./../converter.py "$file" "../Output/${file}.kml"
done
