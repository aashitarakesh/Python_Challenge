# Create a Python script to automate the analysis of any passage 

# * Import a text file filled with a paragraph of your choosing.

# * Assess the passage for each of the following:

# * Approximate word count

# * Approximate sentence count

# * Approximate letter count (per word)

# * Average sentence length (in words)

# Import Modules
import os
import csv
import re


# Set path for paragraph
txtpath = os.path.join("raw_data", "paragraph_1.txt")

# Open txt File 
with open(txtpath) as txtfile:
    txtreader = txtfile.read()

#Calculate Approximate Word Count
word_count = len(re.findall(r'\w+', txtreader))

# Calculate Approximate Sentence Count
sentence_count = len(re.split("(?<=[.!?]) +", txtreader))

# Calculate Average Letter Count
letter_count = len(txtreader.replace(" ", ""))
average_letter_count = round((letter_count/word_count) ,1)

# Calculate Average Sentence Length
average_sentence_count = round((word_count/sentence_count) ,1)

# Print Analysis to Terminal
print("Paragraph Analysis")
print("-------------------------------------")

print(f'Approximate Word Count:  {word_count}')
print(f'Approximate Sentence Count  {sentence_count}')
print(f'Average Letter Count  {average_letter_count}')
print(f'Average Sentence Length  {average_sentence_count}')

