import os
import json
import re

#initialize a word dictionary
words = {}

#function to search for words based on the clue
def search_word(clue, letters=None):

    #if letters are provided, filter the words based on the letters
   # characters = list(letters) if letters else None    
    
    if letters:
        #this is a dictionary comprehension that filters the words based on the letters. all is a built-in function that 
        # returns True if all the characters in the word are in the letters list
        limitedwords = {key: value for key, value in words.items() if all(char in key for char in letters)}
        return [key for key in limitedwords if clue.fullmatch(key)]
    else:
        #search for the clue in the words dictionary    
        return [key for key in words if clue.fullmatch(key)]

#this is same as teh below
#   results = []   
#   for key in words:
#        if clue.search(key):
#            results.append(key)
#    return results

#you can do this as well, using list comprehension to find matches
#return [key for key in words if clue_pattern.fullmatch(key)]

#load the words from the json file
filepath = os.path.join(os.path.dirname(__file__), 'templates\words.json')

#check if the file exists and is a valid json file.
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
        #add ^ and $ to the clue to match the whole word
        clue = f'^{clue}$'
        try:
        #compile the clue into a regex pattern
            regex = re.compile(clue, re.IGNORECASE)        
            return regex
        #handle invalid regex patterns
        except re.error as e:
            print(f'Invalid regex pattern: {e}')   
    return None 

#main code
clue = getvalidclue()
#check if a valid clue was entered

letters = input("Enter the letters that need to be in the word. If none, hit enter: ")
letters = list(letters) if letters else None  

if clue is not None:
    if letters:
        results = search_word(clue, letters)
    else:   
        results = search_word(clue)
    if results:
        print(f'Results:\n{results}')        
    else:
        print('No results found.')
else:
    print('No search performed.')