replace_word = "###"

# Read the content of the file first
with open("fileioexamplefile.txt", "r") as file:
    lines = file.readlines()

# Modify the content (replace "RRR" with "###")
with open("fileioexamplefile.txt", "w") as file:
    for line in lines:
        modified_line = line.replace("RRR", replace_word)
        file.write(modified_line)  # Write the modified line back to the file
