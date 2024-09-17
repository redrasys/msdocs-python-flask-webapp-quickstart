import os
import json
import re

from itertools import permutations

#initialize a word dictionary
words = {}

#function to search for words based on the clue
def search_word(clue):

    perms = {''.join(p) for p in permutations(clue)}
    results = []

    print(sorted(perms))

    for perm in perms:
        if perm in words.keys():
            results.append(perm)

    return results

#load the words from the json file
filepath = os.path.join(os.path.dirname(__file__), 'templates\words.json')

#check if the file exists and is a valid json file
try:
    with open(filepath) as f:
        words = json.load(f)
except FileNotFoundError as e:
    print(f'File not found: {filepath}')
except json.JSONDecodeError as e:
    print(f'Invalid JSON file: {e}')

#function to get a valid clue from the user
def getvalidclue():
    while True:
        clue = input('Enter the word clue or Type "exit" to exit: ')    
        if clue == '':
            print('Please enter a clue.')
            continue
        elif clue.lower()=='exit':
            print('Exiting...')
            break            
        return clue        
    return None   

#main code
clue = getvalidclue()
#check if a valid clue was entered
if clue is not None:
    results = search_word(clue)
    if results:
        print(f'Results:\n{results}')        
    else:
        print('No results found.')
else:
    print('No search performed.')