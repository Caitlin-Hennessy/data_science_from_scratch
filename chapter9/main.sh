#!/bin/bash

cat words.txt | python grep.py "[0-9]" | python linecount.py

cat words.txt | python wordcounter.py 5
