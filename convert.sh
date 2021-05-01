#!/bin/bash
for file in *.csv
do
  python3 ./converter.py "$file" "${file}.kml"
done