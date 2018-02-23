#!/usr/bin/env/python3
""" Usage: python3 dankmemes.py "lol" "haha" "rip" | pbcopy"""
import sys,subprocess, re
positive = '({})'.format(sys.argv[1])
negative = '({})'.format(sys.argv[2])
lines = sys.argv[3].split()
output = ""
for char in lines:
    figged = subprocess.run(
        ['figlet', '-f', 'banner', char],
        universal_newlines=True,
        stdout=subprocess.PIPE,
        check=True)
    figged = figged.stdout
    figged = figged.replace(' ', positive).replace('#', negative)
    output += figged
print(output)
