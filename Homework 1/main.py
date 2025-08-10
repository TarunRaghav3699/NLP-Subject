import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd




# Task 1: Reading and Writing Files
# Python code to read input_text.txt and remove whitespace (strip) and lowercase them and write 'em in lowercase_output.txt
with open("input_text.txt", "r") as file, open("lowercase_output.txt", "w") as outputfile:
    for i in range(20):
        line = file.readline()
        if not line:
            break
        content = line.strip().lower()
        # print(content)
        outputfile.write(content + "\n") 




# Task 2: Text Cleaning
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




# Task 3: Tokenization and Analysis
# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Read cleaned text
with open("cleaned_output.txt", "r") as file:
    text = file.read()

# Tokenize into words
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Counts
total_tokens_before = len(tokens)
total_tokens_after = len(filtered_tokens)
vocabulary_size = len(set(filtered_tokens))

# Display results
print(f"Total tokens before stopword removal: {total_tokens_before}")
print(f"Total tokens after stopword removal: {total_tokens_after}")
print(f"Vocabulary size (unique words): {vocabulary_size}")




# TASK 4: Word Frequency Analysis
# Count word frequency
word_counts = Counter(filtered_tokens)

# Top 20 words
top_20 = word_counts.most_common(20)
print("Top 20 most common words:")
for word, count in top_20:
    print(f"{word}: {count}")

# Save full frequency table to CSV
df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
df = df.sort_values(by="Frequency", ascending=False)
df.to_csv("word_frequency.csv", index=False)

print("\nWord frequency table saved to word_frequency.csv")