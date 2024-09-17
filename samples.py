import os
import json
import re

words = {}

def search_word(clue):
    results = []
    clue = f'^{clue}$'
    regex = re.compile(clue, re.IGNORECASE)
    for key in words:
        if regex.search(key):
            results.append(key)
    return results

filepath = os.path.join(os.path.dirname(__file__), 'templates\words.json')

with open(filepath) as f:
    words = json.load(f)

clue = input('Enter the word clue: ')

results = search_word(clue)
print('Results: ', results)
