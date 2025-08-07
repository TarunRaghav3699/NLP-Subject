import string

# # Python code to read input_text.txt

with open("input_text.txt", "r") as file, open("lowercase_output.txt", "w") as outputfile:
    for i in range(20):
        line = file.readline()
        if not line:
            break
        content = line.strip().lower()
        print(content)
        outputfile.write(content + "\n") 



# Open the lowercase_output.txt file and read content
with open("lowercase_output.txt", "r") as infile:
    text = infile.read()

# Remove punctuation and digits
cleaned_text = ''
for char in text:
    if char not in string.punctuation and not char.isdigit():
        cleaned_text += char

# Remove extra spaces
cleaned_text = ' '.join(cleaned_text.split())

# Write the cleaned text to a new file
with open("cleaned_output.txt", "w") as outfile:
    outfile.write(cleaned_text)

print("Cleaned text saved successfully!")
