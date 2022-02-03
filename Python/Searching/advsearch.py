# Author: Michael Vance








import json



#Prompt for the file path, then load it
try:
    filepath = input('what is the name of the file? ')
    file = open(filepath)
    rawWords = json.load(file)
    file.close()
except:
    print('There was an error loading your file.')
    print('Please try again.')
    exit()


#Read the JSON into a list
words = []
for x in rawWords['array']:
    words.append(x)

if not words:
    print('File is empty.')
    exit()
#Get a word to search for
search = input('What name are we looking for? ')



#Do an advanced search.

#Create two variables to control the search pattern.
start = 0
end = len(words) - 1

while start < (end - 1):
    searchL = (start + end)//2
    if words[searchL] == search:
        print(f"We found {search} in {filepath}")
        exit()
    elif search < words[searchL]:
        end = searchL
    else:
        start = searchL

if words[start] == search:
    print(f"We found {search} in {filepath}")
    exit()
elif words[end] == search:
    print(f"We found {search} in {filepath}")
    exit()
else:
    print(f"We did not find {search} in {filepath}")