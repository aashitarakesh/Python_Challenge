# Create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# Import Modules
import os
import csv

# Set up Variables
vote_count = 0
candidate_list = []
unique_candidate_list = set()
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set path for election_data
csvpath = os.path.join("Resources", "election_data.csv")

# Open csv File 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip Headers
    next(csvreader)

    # Count Total number of votes 
    for row in csvreader:
        vote_count += 1

        # Calculate Total number of votes each candidate won
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1 
        elif row[2] == "O'Tooley":
            otooley_votes +=1

        # Set candidate names to a List
        candidate_list.append(row[2])
        
    # Create a set from candidate list to remove duplicates       
    unique_candidate_list = list(set(candidate_list))

    # Calculate Percentage of votes each candidate won
    khan_percent = khan_votes/vote_count
    correy_percent = correy_votes/vote_count
    li_percent = li_votes/vote_count
    otooley_percent = otooley_votes/vote_count

    # Find winner of election using dictionary comprehension
    candidate_key =["Khan", "Correy", "O'Tooley", "Li"] 
    votes_values = [khan_votes, correy_votes, otooley_votes, li_votes]
    dict_candidates_votes = {candidate_key[i]: votes_values[i] for i in range(len(candidate_key))}
    winner = max(dict_candidates_votes, key=dict_candidates_votes.get)

    # Print Election Results to Terminal
    print("Election Results")
    print("-------------------------------------")
    print(f'Total Votes : {vote_count}')
    print("-------------------------------------")
    print(f'Complete List of Candidates : {unique_candidate_list}')
    print("-------------------------------------")
    print(f'Khan: {khan_percent:.3%}  ({khan_votes})')
    print(f'Correy: {correy_percent:.3%}  ({correy_votes})')
    print(f'Li: {li_percent:.3%}  ({li_votes})')
    print(f"O'Tooley: {otooley_percent:.3%}  ({otooley_votes})")
    print("-------------------------------------")
    print(f'Winner: {winner}')
    print("-------------------------------------")

# Specify the file to write to 
output_path = os.path.join("Analysis", "Election_Results.txt")

# Export a txt file with Election Results
with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("-------------------------------------\n")
    txtfile.write(f'Total Votes : {vote_count}\n')
    txtfile.write("-------------------------------------\n")
    txtfile.write(f'Complete List of Candidates : {unique_candidate_list}\n')
    txtfile.write("-------------------------------------\n")
    txtfile.write(f'Khan: {khan_percent:.3%}  ({khan_votes})\n')
    txtfile.write(f'Correy: {correy_percent:.3%}  ({correy_votes})\n')
    txtfile.write(f'Li: {li_percent:.3%}  ({li_votes})\n')
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}  ({otooley_votes})\n")
    txtfile.write("-------------------------------------\n")
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write("-------------------------------------\n")

