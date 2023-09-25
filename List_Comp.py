# The basic outline of this problem is to read the file, look for integers 
# using the re.findall(), looking for a regular expression of '[0-9]+' and
# then converting the extracted strings to integers and summing up the integers.
# NOTE: This program achieves the same result as the Regex_Sum.py file, however,
# this method uses list comprehension to format the regex into one line.

import re
print(sum([int(line) for line in re.findall('[0-9]+',open('regex_sum_42.txt').read())]))
