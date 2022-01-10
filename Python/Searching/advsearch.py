# 1. Name:
#       Michael Vance
# 2. Assignment Name:
#       Lab 06: Advanced Search
# 3. Assignment Description:
#       Create a program to search a list.
#       Instead of doing a linear search, create a
#       more advanced search that starts in the middle
#       and works its way towards where it should be.
# 4. Algorithmic Efficiency
#       I have no idea. I hope it is closer to O(log n)
#       because it uses comparisons to search rather
#       than checking the whole list every time.
# 5. What was the hardest part? Be as specific as possible.
#       Figuring out how to keep track of where I am in the
#       list and cover all cases. I didn't get around to the
#       'start' and 'end' method for quite a while. As it is,
#       I am sure there is a better way to handle the little
#       end case scenario, I just don't have the time to
#       figure it out.
# 6. How long did it take you to complete this assignment?
#       I would say about ~5 or 6 hours. Of course, part of
#       that was developing the psudocode for it, as I didn't
#       have last week's assignment, and I didn't want to look
#       at the solution until I had it done.








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