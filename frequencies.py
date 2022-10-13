"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter
def frequencies(items):
    strlist = []
    frequencies = {}
    for i in items:
        strlist.append(str(i))
    frequencies = Counter(strlist)
    return frequencies
