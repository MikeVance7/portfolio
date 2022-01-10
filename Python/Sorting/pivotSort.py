# 1. Name:
#       Michael Vance
# 
# 2. Assignment Name:
#       Lab 08: Sort
# 
# 3. Assignment Description:
#    	Create a script to read a JSON list and sort it    
#    	using the pivot method from last week.
#    	Add asserts where appropriate to catch bugs.
#    	    
# 5. What was the hardest part? Be as specific as possible.
#       Honestly, the hardest part was probably deciding where
# 		the best place and type of Asserts to add. I might
# 		be missing the point a bit (I hope not), but it seemed
# 		silly to me to add an assert to see if filepath
# 		existed in a try/catch block.
# 
# 6. How long did it take you to complete this assignment?
#		About 3 hours. With the psudocode already done,
#		it was pretty simple to convert it to Python.
# 		What took me longer was implementing feedback from
# 		last weeks assignment, and figuring out where to put
# 		useful asserts.





import json

try:
    filepath = input('File path:')
    file = open(filepath)
    rArray = json.load(file)
    file.close()
except:
    print('There was an error loading your file.\nPlease try again.')
    exit()


assert(rArray), "Array doesn't exist!"
tArray = rArray['array']


# Make sure the array isn't empty
if len(tArray) == 0:
	print("There is nothing to sort.")
	exit()



# Start at the end of the array
pivot = len(tArray) -1

#Loop through and find the largest value,
#then Swap that with the pivot.
while pivot > 0:
	# Create a variable for the current location,
	# and another for the largest value
	testValue = 0
	largeVal = 0



	# Check the values, and if the current one is larger,
	# Store it
	while testValue <= pivot:
		if tArray[testValue] > tArray[largeVal]:
			largeVal = testValue
		testValue += 1


	# Swap the largest value with the pivot value.
	# Be sure to preserve the value being swapped.

	# Store the pivot's current value, store the
	# largest value in pivot, then store what was
	# in pivot in the index being swapped.
	swapValue = tArray[pivot]
	tArray[pivot] = tArray[largeVal]
	tArray[largeVal] = swapValue

	# Make sure that the end result is the desired result.
	assert(tArray[pivot] >= tArray[largeVal]), "End result is incorrect."

	# Move the pivot point.
	pivot -= 1

assert(tArray[0] < tArray[(len(tArray) - 1)]), "Sorting Failed."
# Print Resulting array.
print(f'The values in {filepath} are:')
for i in tArray:
	print(f"\t{i}")