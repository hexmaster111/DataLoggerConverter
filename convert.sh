#!/bin/bash
for file in *.csv
do
  ./converter.py "$file" "${file}.csv"
done