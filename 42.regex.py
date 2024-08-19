'''
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
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

print(match)

ma = re.finditer(pattern, text)
for j in ma:
    print(j)
print("-----")

pat = r'^S'

match2 = re.search(pattern, text)

print(match2)

pat = r'?Saurabh'

match3 = re.search(pattern, text)

print(match3)


# Replacement
text2 = "The cat is in the hat."
pattern3 = r"[a-z]+at"
matches3 = re.findall(pattern3, text2)
print(matches3)

new_text = re.sub(pattern3, "dog", text2)
print(new_text)
