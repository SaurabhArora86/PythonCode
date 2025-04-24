'''
[]  Represent a character class
^   Matches the beginning of string 
$   Matches the end of the string
.   Matches any character except newline
?   Matches zero or one occurrence of preceding character or group
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
'''
import re
text = "My name is Saurabh Arora and I am a good learner. Please dont call me Daurabh"

pattern = r'[A-Z]aurabh'

match = re.search(pattern, text)

# print(match)

ma = re.finditer(pattern, text)
for j in ma:
    print(j)
print("-----")


# Below will give none as it matches with the first character of the string
pat = r'^S'

match2 = re.search(pat, text)

print(match2)

# pat2 = r'?Saurabh'

# match3 = re.search(pat2, text)

# print(match3)


# Test strings
text1 = "color"
text2 = "colour"

# Pattern: 'colou?r' matches both 'color' and 'colour'
pat = r'colou?r'

# Search in the strings
match1 = re.search(pat, text1)
match2 = re.search(pat, text2)

# Print the match objects
print(match1)  # This will match 'color'
print(match2)  # This will match 'colour'

# Replacement
text2 = "The cat is in the hat."
pattern3 = r"[a-z]+at"
matches3 = re.findall(pattern3, text2)
print(matches3)

new_text = re.sub(pattern3, "dog", text2)
print(new_text)
